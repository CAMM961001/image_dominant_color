import cv2
import numpy as np
import easygui

from  urllib.request import urlopen


def load_image(url:str):
    with urlopen(url=url) as url:
        with open('original.jpg', 'wb') as file:
            file.write(url.read())


if __name__ == '__main__':
    print('Hola mundo')
