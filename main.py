# python3 -m venv venv
# . venv/bin/activate
# pip install streamlit
# pip install torch torchvision
# streamlit run main.py

import time
import streamlit as st
from PIL import Image
import style

st.title('Group 10 Style Transfer App')

img = st.sidebar.selectbox(
    'Выберите Фото',
    ('selfie.jpg', 'selfietwo.jpg')
)

style_name = st.sidebar.selectbox(
    'Выберите Стиль',
    ('Pop art', 'Art Nouveau', 'Cubism', 'Abstract')
)


model = "models/" + style_name + ".pth"
input_image = "images/content-images/" + img
output_image = "images/output-images/" + style_name + "-" + img

st.write('### Source image:')
image = Image.open(input_image)
st.image(image, width=400)

clicked = st.button('Stylize')
        
if clicked:
    st.snow()
    model = style.load_model(model)
    with st.spinner('Wait for it...'):
        style.stylize(model, input_image, output_image)
      
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    st.success('Done!')
