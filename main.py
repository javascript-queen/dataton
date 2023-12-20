# python3 -m venv venv
# . venv/bin/activate
# pip install streamlit
# pip install torch torchvision
# streamlit run main.py

import time
import streamlit as st
from PIL import Image
import style
import os

st.title('Group 10 Style Transfer App')

# style image paths:
root_style = "./images/style-images"

# creating a side bar for picking the style of image
style_name = st.sidebar.selectbox(
    'Select Style',
    ('Pop Art', 'Art Nouveau', 'Cubism', 'Abstract')
)
path_style = os.path.join(root_style, style_name+".jpg")

# Upload image functionality
img = None
uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png"])

show_file = st.empty()

# checking if user has uploaded any file
if not uploaded_file:
    show_file.info("Please Upload an Image")
else:
    img = Image.open(uploaded_file)
    # check required here if file is an image file
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.image(path_style, caption='Style Image', use_column_width=True)

extensions = [".png", ".jpeg", ".jpg"]

if uploaded_file is not None and any(extension in uploaded_file.name for extension in extensions):

    name_file = uploaded_file.name.split(".")
    root_model = "./models"
    model_path = os.path.join(root_model, style_name+".pth")

    img = img.convert('RGB')
    input_image = img

    root_output = "./images/output-images"
    output_image = os.path.join(
        root_output, style_name+"-"+name_file[0]+".jpg")

    clicked = st.button("Stylize")
        
    if clicked:
        st.snow()
        model = style.load_model(model_path)
        with st.spinner('Wait for it...'):
            style.stylize(model, input_image, output_image)
          
            st.write('### Output image:')
            image = Image.open(output_image)
            st.image(image, width=400)
        st.success('Done!')
