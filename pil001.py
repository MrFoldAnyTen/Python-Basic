#!/usr/bin/env python3
from PIL import Image
# import Image

def main(  ): #{
    size = width, height =230, 234;

    image = Image.new( "RGB", size, "hsl(0, 100%, 50%)")
    image.show()

    del image;
#}

if ( __name__ =="__main__"): #{

    main();
#}
