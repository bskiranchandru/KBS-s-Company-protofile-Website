# upload - store - predict using models
#to upload use form tag tag
# can use any cloud like aws ,eduku,jps
import os
import torch
from flask import request
from flask import Flask
from flask import render_template


app = Flask(__name__)
UPLOAD_FOLDER = "D:\My_work\Cancer_cell_Detection_website\static" #global variable to solve new images

@app.route("/cancer.html")
def indec():
    return render_template("cancer.html")

@app.route("/web.html", methods = ["GET", "POST"])

def upolad_predict():
    if request.method == "POST":
        image_file = request.files["image"] #only exit if request method is post
        if image_file: # to get and save image in image location
            image_location = os.path.join(
                UPLOAD_FOLDER, 
                image_file.filename
            )
            image_file.save(image_location)
            #pred = predict(image_location, MODEL)
            return render_template("web.html", predictions = 1, image_loc = image_file.filename)
    return render_template("web.html", predictions = 0,image_loc=None )#none bez if you are run without image

if __name__ == "__main__":
    app.run(port = 1200, debug = True)