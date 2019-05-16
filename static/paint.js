$(document).ready(function(){




            paintContext = document.getElementById('paintCanvas').getContext("2d");




            $('#clearCanvasSimpleColors').mousedown(function(e)
            	{
            		clickX_simpleColors = new Array();
            		clickY_simpleColors = new Array();
            		clickDrag_simpleColors = new Array();
            		//clickColor_simpleColors = new Array();

            	});



            var curColor = "#000000";
            var clickColor = new Array();
            var sizeList = new Array();
            var curSize = "50";

            $('#wBtn').click(function(){ curColor = "#ffffff"; });

            $('#bBtn').click(function(){ curColor = "#000000"; });


            $('#sizeList').on('change', function(){ curSize = $(this).val();   });

            $('#paintCanvas').mousedown(function(e){
                console.log("mouse down");
                var mouseX = e.pageX - this.offsetLeft;
                var mouseY = e.pageY - this.offsetTop;

                paint = true;
                addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
                redraw();
            });

            $('#paintCanvas').mousemove(function(e){
                if(paint){
                    addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
                    redraw();
                }
            });

            $('#paintCanvas').mouseup(function(e){
                paint = false;
            });

            $('#paintCanvas').mouseleave(function(e){
                paint = false;
            });

            var clickX = new Array();
            var clickY = new Array();
            var clickDrag = new Array();
            var paint;

            function addClick(x, y, dragging)
            {
                clickX.push(x);
                clickY.push(y);
                clickDrag.push(dragging);
                clickColor.push(curColor);
                sizeList.push(curSize);

            }



            function redraw(){
                //paintContext.clearRect(0, 0, paintContext.#paintCanvas.width, paintContext.#paintCanvas.height); // Clears the #paintCanvas

                paintContext.lineJoin = "round";

                for(var i=0; i < clickX.length; i++) {
                    paintContext.beginPath();
                    if(clickDrag[i] && i){
                        paintContext.moveTo(clickX[i-1], clickY[i-1]);
                    }else{
                        paintContext.moveTo(clickX[i]-1, clickY[i]);
                    }
                    paintContext.lineTo(clickX[i], clickY[i]);
                    paintContext.closePath();
                    paintContext.stroke();
                    paintContext.strokeStyle = clickColor[i];
                    paintContext.lineWidth = sizeList[i];

                }
            }







        });
