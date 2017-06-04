from PIL import Image
from pylab import *

def clickIm():
    im = array(Image.open('image001.png'))
    imshow(im)
    print('please click three points')
    x = ginput(3)
    print('you clicked: ', x)
    show()

def arrayIm():
    im = array(Image.open('image001.png'))
    print(im.shape, im.dtype)

    im = array(Image.open('image001.png'))
    print(im.shape, im.dtype)
    imshow(im)
    show()

def invertGrey():
    im = array(Image.open('image001.png').convert('L'),'f')
    im2 = 255 - im #invert image
    imshow(im2)
    show()

def clampInter():
    im = array(Image.open('image001.png').convert('L'),'f')
    im3 = (100.0/255) * im + 100 # clamp to interval 100...200
    imshow(im3)
    show()

def squared():
    im = array(Image.open('image001.png').convert('L'),'f')
    im4 = 255.0 * (im/255.0)**2 # squared
    imshow(im4)
    show()
