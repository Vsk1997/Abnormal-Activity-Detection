# Abnormal Activity Detection

Surveillance systems, mainly composed of cameras, are today widespread in both indoor and outdoor environments.

Video surveillance involves the act of observing a scene or scenes and looking for specific behaviors that are improper or that may indicate the emergence or existence of improper behavior.

Common uses of video surveillance include observing the public at the entry to sports events, public transportation (train platforms, airports, etc.), and around the perimeter of secure facilities, especially those that are directly bounded by community spaces.

In this project, convolutional neural networks using image recognition and their combination with recurrent neural networks temporal information is extracted using which an intelligent surveillance system is made.The LSTM Encoder-Decoder framework is used to learn representation of video sequences and applied for detect abnormal event in complex environment.The abnormal events are identified by computing the reconstruction loss using Euclidean distance between original and reconstructed batch.

The training videos capture normal situations. Testing videos include both normal and abnormal events. Some of the abnormal activities are as follows:

- Fighting
- Stealing
- Doing some abnormal activites

---

In this project we have two datasets one which is available on internet i.e. CUHK campus avenue 
dataset.

The videos are captured in CUHK campus avenue with 15328 training frames.This dataset accompanies paper "Abnormal Event Detection at 150 FPS in Matlab, Cewu Lu, Jianping Shi, JiayaJia, International Conference on Computer Vision, (ICCV), 2013".

The training videos capture normal situations. Testing videos include both normal and abnormal events. Two samples are shown as follows:
AvenueDataset : http://www.cse.cuhk.edu.hk/leojia/projects/detectabnormal/dataset.html

![image](https://user-images.githubusercontent.com/37743343/179402667-ef8c2f2f-7d72-4294-8c0c-f2094e4aa629.png)

---

For this project we have collected a variety of video footages from our college (M.B.M. Engineering College) cctv cameras which is over more than 15 GB (12-14 hours) of data. For this we have taken the data or videos from 3 cameras which are:
- Camera near the computer center.
- Camera near the physics department.
- Camera in mechanical department.

<p align="center">
  <img width="650" height="550" src="https://user-images.githubusercontent.com/37743343/179403055-7f6ea75d-d06a-463c-9361-0d7d494cfa55.png">
</p>

---

For testing we needed some abnormal activities too since in campus it is not normal to find out those especially during covid times. So, we shooted some abnormal activities in front of those cameras.

Some of the abnormal events detected are as follows:

<p align="center">
  <img width="500" height="350" src="https://user-images.githubusercontent.com/37743343/179403348-cf3bc8d7-5264-45bb-a51c-2d0b2b747c0b.png">
</p>

<p align="center">
  <img width="500" height="350" src="https://user-images.githubusercontent.com/37743343/179403604-f1dceeeb-448b-4477-8105-17715df99ece.png">
</p>

<p align="center">
  <img width="500" height="350" src="https://user-images.githubusercontent.com/37743343/179403608-b6467b41-e975-4130-8db7-02e619bfa1e2.png">
</p>



