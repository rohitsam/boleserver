from ShazamAPI import Shazam
from flask import Flask, request, render_template
import logging
import os
import json

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG) #for better debuging, we will log out every request with headers and body.
@app.before_request
def log_request_info():
    logging.info('Headers: %s', request.headers)
    logging.info('Body: %s', request.get_data())

@app.route("/upload", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST": #if we make a post request to the endpoint, look for the image in the request body
        image_raw_bytes = request.get_data()  #get the whole body

        save_location = (os.path.join(app.root_path, "resources/python.wav")) #save to the same folder as the flask app live in 

        f = open(save_location, 'wb') # wb for write byte data in the file instead of string
        f.write(image_raw_bytes) #write the bytes from the request body to the file
        f.close()
        
        print("audio saved")
        mp3_file_content_to_recognize = open("resources/python.wav", 'rb').read()
        shazam = Shazam(mp3_file_content_to_recognize)
        recognize_generator = shazam.recognizeSong()
        while 1:
            try:
                x = (next(recognize_generator))
                print("---------------------")
                y = x[1]
            except:
                return (y["track"]["title"])
                break
                
                
                

                
app.run()

   
#mp3_file_content_to_recognize = open("resources/python.wav", 'rb').read()
#shazam = Shazam(mp3_file_content_to_recognize)
#recognize_generator = shazam.recognizeSong()
#while 1:
#    try: 
#        x = (next(recognize_generator))
#        print("---------------------")
#        y = x[1]
#        print(y["track"]["title"],y["track"]["title"])
#    except:
#        break;
#

        
        
        
#        while 1:
#            try: 
#                x = (next(recognize_generator))
#                print("---------------------")
#                y = x[1]
#                print(y["track"]["title"],y["track"]["title"]