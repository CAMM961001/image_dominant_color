# Reference for background remove: https://www.python-engineer.com/posts/remove_background/
# Reference for dominant color: https://github.com/fengsp/color-thief-py

from rembg import remove
from colorthief import ColorThief

import webcolors
import pandas as pd
import modules.dominant_color as src

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

dominant_rgb = dominant_color.get_color(quality=1)
palette_rgb = dominant_color.get_palette(color_count=6)

colors = {
    'type': ['rgb', 'hex', 'label']
    ,'color': [
        dominant_rgb
        ,webcolors.rgb_to_hex(dominant_rgb)
        ,src.closest_color(requested_colour=dominant_rgb)]
    ,'palette': [
        palette_rgb
        ,[webcolors.rgb_to_hex(col) for col in palette_rgb]
        ,[src.closest_color(col)for col in palette_rgb]]}

colors = pd.DataFrame(data=colors).set_index('type')

if __name__ == '__main__':
    print(colors)
