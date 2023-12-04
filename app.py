# Reference for background remove:
# https://www.python-engineer.com/posts/remove_background/

from rembg import remove
import modules.dominant_color as src

import matplotlib.pyplot as plt

URL = 'https://i.pinimg.com/originals/ee/d6/8c/eed68c61a18a23c9975a4400239cda72.jpg'
#'https://pngimg.com/uploads/women_bag/women_bag_PNG6428.png'

src.load_image(url=URL)

input_path = 'original.jpg'
output_path = 'no_background.png'

with open(input_path, 'rb') as in_img:
    with open(output_path, 'wb') as out_img:
        input = in_img.read()
        output = remove(input)
        out_img.write(output)

if __name__ == '__main__':
    print('Done')
