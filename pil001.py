#!/usr/bin/env python3
from PIL import Image
# import Image

def main():
#    size = width, height =230, 234;
#    image = Image.new( "RGB", size, "hsl(0, 100%, 50%)")
#    image.show()
#    image2.show();
    go()


def go():
    filename = "image003.png";
    filename2 = "image004.png";
    image = Image.open(filename);
    image2 = Image.open(filename2);
    Image.blend(image, image2 ,0.5).show();
    del image2;
    del image;


if ( __name__ =="__main__"):
    main();
