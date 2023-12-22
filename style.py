# Импорт модуля для обработки аргументов командной строки.
import argparse
# Импорт модуля для взаимодействия с операционной системой.
import os
# Импорт системного модуля для доступа к различным переменным и функциям Python.
import sys
# Импорт модуля для работы со временем.
import time
# Импорт модуля для работы с регулярными выражениями.
import re

import numpy as np
# Импорт пакетов Torch
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
import torch.onnx

# Импорт пользовательских утилит
import utils
#  Импорт класса TransformerNet из файла transformer_net.py
from transformer_net import TransformerNet
# Импорт класса Vgg16 из файла vgg.py
from vgg import Vgg16
import streamlit as st

# Здесь мы будем использовать концепцию кэширования, чтобы после того, как пользователь
# использовал определенную модель, вместо загрузки ее снова и снова при каждом использовании,
# мы будем кэшировать модель.

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Загрузка модели

@st.cache_data
def load_model(model_path):
    # Создание экземпляра модели стиля
    with torch.no_grad():
        # Файл transformer_net.py содержит модель стиля
        style_model = TransformerNet()  
        state_dict = torch.load(model_path)
        # Удаление сохраненных устаревших ключей running_* в InstanceNorm из контрольной точки
        for k in list(state_dict.keys()):
            if re.search(r'in\d+\.running_(mean|var)$', k):
                del state_dict[k]
        # Загрузка весов модели стиля
        style_model.load_state_dict(state_dict)
        style_model.to(device)
        style_model.eval()
        return style_model

# Нам нужно изображение контента и загруженная модель стиля,
# загруженная с помощью функции load_model

@st.cache_data
def stylize(_style_model, content_image, output_image):

    # Eсли изображение контента представлено в виде пути к файлу
    if type(content_image) == "str":
        content_image = utils.load_image(
            content_image)
    # Преобразование изображения контента
    content_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])
    content_image = content_transform(content_image)

    # Преобразование одного изображения как пакета
    content_image = content_image.unsqueeze(0).to(device)

    with torch.no_grad():
        # Получение стилизованного изображения
        output = _style_model(content_image).cpu()

    # Сохранение стилизованного изображения по указанному пути
    img = utils.save_image(output_image, output[0])
    return img


if __name__ == "__main__":
    main()
