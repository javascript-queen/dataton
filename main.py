# Перед началом загрузки выполнить данные действия! 
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

# Название сайта на streamlit
st.title('Селфи-стайлер Группы 10')

# Пути к style-images:
root_style = "./images/style-images"

# Создаём боковую панель для выбора стиля изображения
style_name = st.sidebar.selectbox(
    'Выберите стиль',
    ('Pop Art', 'Art Nouveau', 'Cubism', 'Abstract')
)
path_style = os.path.join(root_style, style_name+".jpg")

# Функциональность загрузки изображения
img = None
uploaded_file = st.file_uploader(
    "Выберите картинку...", type=["jpg", "jpeg", "png"])

show_file = st.empty()

# Проверка, загрузил ли пользователь какой-либо файл
if not uploaded_file:
    show_file.info("Please Upload an Image")
else:
    img = Image.open(uploaded_file)
    # Проверка: является ли файл файлом изображения
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.image(path_style, caption='Style Image', use_column_width=True)

# Создаём список разрешённых раширений
extensions = [".png", ".jpeg", ".jpg"]

# Проверка наличия загруженного файла и его расширения
if uploaded_file is not None and any(extension in uploaded_file.name for extension in extensions):
    
    # Получение имени файла и пути к модели стиля
    name_file = uploaded_file.name.split(".")
    root_model = "./models"
    model_path = os.path.join(root_model, style_name+".pth")
    
    # Подготовка изображения
    # Преобразование в RGB формат
    img = img.convert('RGB')
    # Исходное изображение для стилизации
    input_image = img

    # Пути для сохранения выходного изображения
    root_output = "./images/output-images"
    output_image = os.path.join(
        root_output, style_name+"-"+name_file[0]+".jpg")

    clicked = st.button("Stylize")

    # Если кнопка нажата, начинается процесс стилизации
    if clicked:
        st.snow()
        # Загрузка модели стиля и стилизация изображения
        model = style.load_model(model_path)
        with st.spinner('Wait for it...'):
            style.stylize(model, input_image, output_image)
            
            # Отображение выходного изображения
            st.write('### Output image:')
            image = Image.open(output_image)
            # Отображение изображения в интерфейсе
            st.image(image, width=400)
        # Сообщение об успешном завершении процесса
        st.success('Готово!')
