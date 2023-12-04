# Reference for background remove: https://www.python-engineer.com/posts/remove_background/
# Reference for dominant color: https://github.com/fengsp/color-thief-py

from rembg import remove
from colorthief import ColorThief
import modules.dominant_color as src

import matplotlib.pyplot as plt

# 'https://i.pinimg.com/originals/ee/d6/8c/eed68c61a18a23c9975a4400239cda72.jpg'
URL = 'https://th.bing.com/th/id/OIP.34MwIAdC_dQ4EmavNamaKAHaJQ?rs=1&pid=ImgDetMain'

src.load_image(url=URL)

input_path = 'original.jpg'
output_path = 'no_background.png'

with open(input_path, 'rb') as in_img:
    with open(output_path, 'wb') as out_img:
        input = in_img.read()
        output = remove(input)
        out_img.write(output)

dominant_color = ColorThief(output_path)

if __name__ == '__main__':
    print(f"Dominante: {dominant_color.get_color(quality=1)}")
    print(f"Paleta: {dominant_color.get_palette(color_count=6)}")
