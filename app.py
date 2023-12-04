from rembg import remove
import modules.dominant_color as src

import matplotlib.pyplot as plt

URL = 'https://http2.mlstatic.com/bolsa-sacola-de-viagem-lona-kvn-transversal-mala-de-mo-50-l-D_NQ_NP_867901-MLB31174117376_062019-F.jpg'
#'https://i.pinimg.com/originals/ee/d6/8c/eed68c61a18a23c9975a4400239cda72.jpg'

src.load_image(url=URL)

input_path = 'temp.jpg'
output_path = 'temp_wb.jpg'

with open(input_path, 'rb') as in_img:
    with open(output_path, 'wb') as out_img:
        input = in_img.read()
        output = remove(input)
        out_img.write(output)

if __name__ == '__main__':
    print('Done')
