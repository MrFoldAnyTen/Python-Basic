import os

def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im, sz):
    """Resize an image array using PIL"""
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))

def histeq(im,nbr_bins=256):
    """ Histogram equalization of a greyscale image"""

    # get image Histogram
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() #cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalize

    # use linear interpolation
    im2 = interp(im.flattern(),bins[:-1],cdf)

    return im2.reshape(im.shape), cdf
