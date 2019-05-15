from flask import Flask, render_template, request, flash, abort, send_file
from flask_cors import CORS
import base64
import random
import os
import glob
import cv2
import keras_segmentation as seg
from keras import backend as K
import time
import numpy as np


app = Flask(__name__)
app.secret_key = '208f2hdd029duq0isjc0jqwij0d2r0fj02'


CORS(app)

models_list = []
m = os.listdir('model')
models_list +=m
image_count = 0
t = 0
image1 = 0
image2 = 0


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

        img = cv2.imread("data/ann/"+file_name, 0)

        _,t_img = cv2.threshold(img, 100, 1, cv2.THRESH_BINARY)
        cv2.imwrite("data/ann/"+file_name, t_img)


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
    global image1, image2

    if request.method == "POST":
        image = request.form.get("image").split(",")[1]
        model_name = request.form['model']
        imgdata = base64.b64decode(image)
        with open("static/input.png", 'wb') as f:
            f.write(imgdata)

        if model_name in models_list:
            K.clear_session()

            model = seg.models.segnet.mobilenet_segnet(n_classes=2, input_height=224, input_width=224)
            model.load_weights("model/"+model_name)



            out = model.predict_segmentation(inp = "static/input.png", out_fname= "static/out.png")

            original = cv2.imread("static/input.png",0)
            #original = cv2.resize(original, (224,224))


            out = cv2.imread("static/out.png",0)
            _,out2 = cv2.threshold(out, 155, 255, cv2.THRESH_BINARY)

            edges = cv2.Canny(out2, 100, 200)
            edges = cv2.bitwise_not(edges)
            out3 = cv2.bitwise_and(original, original, mask=edges)
            out3 = np.hstack((original, out, out3))
            cv2.imwrite("static/out2.png", out3)




    return render_template("infer.html", models = models_list,im1= image1, im2 = image2)



@app.route("/result")
def result():
    try:
        return send_file("static/out2.png")
    except:
        abort(404)


@app.route("/train")
def training():
    K.clear_session()



    model = seg.models.segnet.mobilenet_segnet(n_classes=2, input_height=224, input_width=224)
    model.train( train_images =  "data/train", train_annotations = "data/ann", checkpoints_path = "model/" , epochs=1 )
    model.save_weights('model/mobilent_segnet'+str(time.time()).split('.')[0]+'.h5')

    return "training has finished, now you should be able to select new model"



if __name__ == '__main__':
    app.run(debug = True)
