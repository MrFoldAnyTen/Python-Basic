#!/usr/bin/env python3
from PIL import Image
# import Image



def main(  ): #{

    filename = "image001.png";
    filename2 = "image002.png";

#    size = width, height =230, 234;

#    image = Image.new( "RGB", size, "hsl(0, 100%, 50%)")
#    image.show()

    image = Image.open(filename);
    image2 = Image.open(filename2);

    Image.blend(image, image2 ,0.5).show();

#    image2.show();

    del image2;
    del image;
#}

if ( __name__ =="__main__"): #{

    main();
#}
