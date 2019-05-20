
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

Basically user takes snaps from webcam.Lets you annotate it
on the webpage and send it over to flask server.
Server stores  both images. The model gets
trained using [segmentation_keras](https://github.com/divamgupta/image-segmentation-keras).


Right now it  can take snaps. Can build simple datasets.
infer using default pretrained  model of segmentation_keras
which seems working. 

[image segmentation keras](https://github.com/divamgupta/image-segmentation-keras)

[canvas drawing tutorial](http://www.williammalone.com/articles/create-html5-canvas-javascript-drawing-app/#demo-simple)


To do
- May be add tensorflow serving

## Running
	





```bash
sudo apt install python3-pip
pip3 install  -r requirements.txt
python3 main.py
```
