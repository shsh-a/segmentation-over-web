from flask import Flask, render_template, request, flash
from flask_cors import CORS
import base64
import random
import os
import glob
import cv2
import keras_segmentation
from keras import backend as K


app = Flask(__name__)
app.secret_key = '208f2hdd029duq0isjc0jqwij0d2r0fj02'

CORS(app)

models_list = ['default']
m = os.listdir('model')
models_list +=m
image_count = 0


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/getimages", methods=["GET", "POST"])
def getData():
    if request.method == "POST":
        image1 = request.form.get("image1").split(",")[1]
        image2 = request.form.get("image2").split(",")[1]

        img1data = base64.b64decode(image1)
        img2data = base64.b64decode(image2)

        file_name = str(image_count)+".png"
        with open("data/train/"+file_name, 'wb') as f:
            f.write(img1data)

        with open("data/ann/"+file_name, 'wb') as f:
            f.write(img2data)


        flash(format("Got the image"),'success')
        global image_count
        image_count += 1

    return render_template("index.html", models = models_list)


@app.route("/getcount")
def test():
    real_count = len(os.listdir("data/train"))
    return render_template("test.html", count = image_count, real = real_count)

def delt(path):
    files = glob.glob(path)
    for f in files:
        os.remove(f)

@app.route("/delete")
def delete():
    delt('data/train/*')
    delt('data/ann/*')

    return render_template("delete.html")

@app.route("/infer", methods=["GET", "POST"])
def infer():
    if request.method == "POST":
        image = request.form.get("image").split(",")[1]
        model_name = request.form['model']
        imgdata = base64.b64decode(image)
        with open("static/input.png", 'wb') as f:
            f.write(imgdata)

        if model_name == 'default':
            K.clear_session()

            model = keras_segmentation.pretrained.resnet_pspnet_VOC12_v0_1()
            out = model.predict_segmentation(inp = "static/input.png", out_fname= "static/out.png")



    return render_template("infer.html", models = models_list)



@app.route("/result")
def result():

    return render_template("result.html")

if __name__ == '__main__':
    app.run(debug = True)
