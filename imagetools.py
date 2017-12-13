from PIL import Image, ImageDraw

import numpy as np
from sklearn.cluster import KMeans


def path_to_img_array(path):
    img = Image.open(path)
    vec = np.array(img)    
    return vec


def pick_colors(vec, numColors):
    vec = vec.reshape(-1, 3)
    model = KMeans(n_clusters=numColors).fit(vec)
    return model.cluster_centers_


def show_key_colors(colorList):
    n = len(colorList)

    im = Image.new('RGBA', (100*n, 100))
    draw = ImageDraw.Draw(im)

    for idx, color in enumerate(colorList):
        color = tuple([int(x) for x in color])
        print(color)
        draw.rectangle([(100*idx, 0), (100*(idx+1), 100*(idx+1))]
                      , fill=tuple(color))

    return im
