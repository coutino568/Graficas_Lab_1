
import random
from gl import Renderer
from obj import Object

windoWidth = 1920*1
windowHeight = 1080*1
scale= 1
viewportWidth= windoWidth*scale
viewportHeight= windowHeight *scale
viewportX=0
viewportY=0



myRenderer = Renderer(windoWidth, windowHeight)
myRenderer.glViewPort(viewportX,viewportY,viewportWidth,viewportHeight)


myRenderer.glFillTriangle(50,50,600,950,800,500)
myRenderer.glFillTriangle(50,50,1900,100,1900,0)


myRenderer.glFillTriangle(1600,50,1200,350,1700,500)

myRenderer.glFillTriangle(700,50,1000,200,950,50)
myRenderer.glFinish("output.bmp")