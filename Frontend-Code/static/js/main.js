$(document).ready(function () {
    // Init

    // Upload Preview

    // Predict
    $('#btn-test').click(function () {
        var form_data = new FormData($('#upload-file')[0]);


        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/test',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
        });
    });

});
