import numpy as np
from PIL import Image
from  urllib.request import urlopen


def load_image(url:str):
    with urlopen(url=url) as url:
        with open('original.jpg', 'wb') as file:
            file.write(url.read())

def color_count(img_path:str):
    img = Image.open(img_path)
    reduced = img.convert(mode='P', palette=Image.WEB)
    palette = reduced.getpalette()
    palette = [palette[3*n: 3*n + 3] for n in range(int(len(palette) / 3))]
    color_count = np.array([(n, palette[m]) for n, m in reduced.getcolors()], dtype=object)

    return color_count


if __name__ == '__main__':
    print('Hola mundo')
