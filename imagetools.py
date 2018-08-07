from PIL import Image, ImageDraw

import numpy as np
from sklearn.cluster import KMeans


def path_to_img_array(path):
    '''
    Load image into numpy array
    '''
    img = Image.open(path)
    vec = np.array(img)    
    return vec


def pick_colors(vec, numColors):
    '''
    Do k-means clustering over ``vec`` to return ``numColors``
    '''
    vec = vec.reshape(-1, 3)
    model = KMeans(n_clusters=numColors).fit(vec)
    return model.cluster_centers_


def show_key_colors(colorList):
    '''
    Make a long rectangle, composed of the colors
    detailed in colorList, a list of (R, G, B) tuples
    '''
    n = len(colorList)

    im = Image.new('RGBA', (100*n, 100))
    draw = ImageDraw.Draw(im)

    for idx, color in enumerate(colorList):
        color = tuple([int(x) for x in color])
        print(color)
        draw.rectangle([(100*idx, 0), (100*(idx+1), 100*(idx+1))],
                       fill=tuple(color))

    return im


def avg_rgb(picVec):
    fn = lambda arr, i: int(np.average(arr[:, :, i]))
    return fn(picVec, 0), fn(picVec, 1), fn(picVec, 2)
