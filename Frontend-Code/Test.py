from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf
import cv2
from keras.preprocessing.image import img_to_array,load_img
from keras.layers import Conv3D,ConvLSTM2D,Conv3DTranspose
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import load_model
import argparse
from PIL import Image
import imutils


from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        model=Sequential()

        model.add(Conv3D(filters=128,kernel_size=(11,11,1),strides=(4,4,1),padding='valid',input_shape=(227,227,10,1),activation='relu'))
        model.add(Conv3D(filters=64,kernel_size=(5,5,1),strides=(2,2,1),padding='valid',activation='relu'))
        model.add(ConvLSTM2D(filters=64,kernel_size=(3,3),strides=1,padding='same',dropout=0.4,recurrent_dropout=0.3,return_sequences=True))
        model.add(ConvLSTM2D(filters=32,kernel_size=(3,3),strides=1,padding='same',dropout=0.3,return_sequences=True))
        model.add(ConvLSTM2D(filters=64,kernel_size=(3,3),strides=1,return_sequences=True, padding='same',dropout=0.5))
        model.add(Conv3DTranspose(filters=128,kernel_size=(5,5,1),strides=(2,2,1),padding='valid',activation='relu'))
        model.add(Conv3DTranspose(filters=1,kernel_size=(11,11,1),strides=(4,4,1),padding='valid',activation='relu'))

        model.compile(optimizer='adam',loss='mean_squared_error',metrics=['accuracy'])

        model.load_weights("saved_model_final.h5")

        cap = cv2.VideoCapture(file_path)
        print(cap.isOpened())

        flag=0
        while cap.isOpened():
            imagedump=[]
            ret,frame=cap.read()
            for i in range(10):
                ret,frame=cap.read()
                
                if not hasattr(frame,'shape'):
                    flag=1
                    break
                
                image = imutils.resize(frame,width=640,height=360)

                frame=cv2.resize(frame, (640,360), interpolation = cv2.INTER_AREA)
                gray=0.2989*frame[:,:,0]+0.5870*frame[:,:,1]+0.1140*frame[:,:,2]
                gray=(gray-gray.mean())/gray.std()
                gray=np.clip(gray,0,1)
                imagedump.append(gray)
                
            if flag==1:
                break

            imagedump=np.array(imagedump)

            imagedump.resize(227,227,10)
            imagedump=np.expand_dims(imagedump,axis=0)
            imagedump=np.expand_dims(imagedump,axis=4)

            output=model.predict(imagedump)

            loss=mean_squared_loss(imagedump,output)
            print(loss)

            if frame.any()==None:
                print("none")
            
            if cv2.waitKey(10) & 0xFF==ord('q'):
               break
            if (loss>0.000662 and loss<0.000685) or (loss>0.00070 and loss<0.000708):                
                print('Abnormal Event Detected')
                cv2.putText(image,"Abnormal Event",(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4,cv2.LINE_AA)

            cv2.imshow("video",image)

        cap.release()
        cv2.destroyAllWindows()

def mean_squared_loss(x1,x2):
            difference=x1-x2
            a,b,c,d,e=difference.shape
            n_samples=a*b*c*d*e
            sq_difference=difference**2
            Sum=sq_difference.sum()
            distance=np.sqrt(Sum)
            mean_distance=distance/n_samples

            return mean_distance



if __name__ == '__main__':
    app.run(debug=True)
