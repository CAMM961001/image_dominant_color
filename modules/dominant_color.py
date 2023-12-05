import webcolors
import numpy as np
from PIL import Image
from  urllib.request import urlopen


def load_image(url:str):
    with urlopen(url=url) as url:
        with open('original.jpg', 'wb') as file:
            file.write(url.read())


def closest_color(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


if __name__ == '__main__':
    print('Hola mundo')
