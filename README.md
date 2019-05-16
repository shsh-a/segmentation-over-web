
# segmentation-over-web
My attempt at making an interactive app that works from browser
and trains an ML model.
![alt text](https://raw.githubusercontent.com/shsh-a/segmentation-over-web/master/static/out2.png)

I could not find a good referneces to do training
on tensorflow.js. I found many sketching libraries
 that would work for annotation that could help to build datasets.
I choose segmentation because it
was easier, just sketch object and background. If
I had to choosen detection then I would have to generate
xml files of bounding boxes and cordinates.

Basically user takes snaps from webcam. Annotates it
on the webpage and sends it over to flask server
server stores  both images. The model gets
trained using [segmentation_keras](https://github.com/divamgupta/image-segmentation-keras) or [segmentation_models](https://github.com/qubvel/segmentation_models).
 I did not get enough time to experiment with either to
find which one would give decent results. I was thinking
of using anything with MobilenetV2.

Right now it  can take snaps
Draw using [wPaint.js](https://github.com/websanova/wPaint) and send to server
infer using default pretrained  model of segmentation_keras
which seems to be not working well.



To do
- training

## Running


```bash
pip3 install requirements.txt
python3 main.py
```
