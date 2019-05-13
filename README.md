# segmentation-over-web
My attempt at making an interactive app that works from browser
and trains an ML model.

I could not find a good referneces to do training
on tensorflow.js. I found many sketching libraries
 that would work for annotation that could help to build datasets.
I choose segmentation because it
was easier, just sketch object and background. If
I had to choosen detection then I would generate
xml files of bounding boxes and cordinates.

Basically user takes snaps from webcam. Annotates it
on the webpage and sends it over to flask server
server stores  both images. The model gets
trained using segmentation_keras. I did not
get enough time to experiment with models to
find which one would give decent results. I was thinking
of using anything with Mobilenetv2.

Right now it  can take snaps
Draw using wPaint.js and send to server
infer using default model. 



To do
- training
