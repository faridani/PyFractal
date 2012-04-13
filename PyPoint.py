# Mandelbrot set
# By Mark Alen
# linux_jvm@yahoo.com
# April 2012

import ImageDraw
from PIL import Image, ImageFilter
from math import log

white = (255, 255, 255)
width = 2000
height = width
image1 = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)


# http://en.wikipedia.org/wiki/Mandelbrot_set
for xpix in range(1,width+1):
    for ypix in range(1,height+1):
        x0 = (xpix*1.0/width*3.5) -2.5
        y0 = (ypix*1.0/height*2)-1
        x = 0
        y = 0
        iteration = 0
        max_iteration = 1000
        while ( (x*x + y*y) < 4)  & (iteration < max_iteration ):
            xtemp = x*x - y*y + x0
            y = 2*x*y + y0
            x = xtemp
            iteration = iteration + 1
        mycol =int(255.0*(1-log(iteration/1000.0*255+1)/log(256)))
        color = (255-mycol,255-mycol,255-mycol)
        if iteration == max_iteration:
            color = white
        draw.point((xpix,ypix), color)
            

filename = "mandel.png"
image1.save(filename)
print "Done!"

