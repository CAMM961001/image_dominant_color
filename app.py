# Reference for background remove: https://www.python-engineer.com/posts/remove_background/
# Reference for dominant color: https://github.com/fengsp/color-thief-py

from rembg import remove
from PIL import Image
from colorthief import ColorThief

import webcolors

import streamlit as st
import pandas as pd
import modules.dominant_color as src

# ---------------------------------------------------------------- App settings
st.set_page_config(
    page_title = 'Dominant Color'
    ,layout = 'wide'
    ,initial_sidebar_state='collapsed')

st.title(body='Dominant colors')

st.write('To start provide an image URL:')

URL = st.text_input(label='URL', value=None)


if URL != None:

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
        ,'dominant': [
            str(dominant_rgb)
            ,webcolors.rgb_to_hex(dominant_rgb)
            ,src.closest_color(requested_colour=dominant_rgb)]
        ,'palette': [
            ' | '.join(str(rgb) for rgb in palette_rgb)
            ,' | '.join([webcolors.rgb_to_hex(col) for col in palette_rgb])
            ,' | '.join([src.closest_color(col)for col in palette_rgb])]}

    colors = pd.DataFrame(data=colors).set_index('type')

    col1, col2 = st.columns(spec=(1, 2.5), gap='small')

    with col1:
        img = Image.open(input_path)
        st.image(
            image=img
            ,use_column_width=True)
    
    with col2:
        st.write('Dominant:')
        st.write(
            f'''
            <svg xmlns="http://www.w3.org/2000/svg">
                <circle cx="20" cy="20" r="20" fill={colors.dominant.loc['hex']} />
            </svg>'''
            ,unsafe_allow_html=True)
        
        st.dataframe(
            data=colors
            ,width=800
            ,hide_index=False)
