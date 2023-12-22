import torch
from PIL import Image

# Функция load_image(filename, size=None, scale=None) загружает изображение из файла с учетом заданного размера или масштабирования.
def load_image(filename, size=None, scale=None):
    img = Image.open(filename)
    if size is not None:
        img = img.resize((size, size), Image.ANTIALIAS)
    elif scale is not None:
        img = img.resize((int(img.size[0] / scale), int(img.size[1] / scale)), Image.ANTIALIAS)
    return img

# Функция save_image(filename, data) сохраняет данные изображения в файле.
def save_image(filename, data):
    # Клонирует данные, ограничивает значения пикселей и преобразует их в массив NumPy
    img = data.clone().clamp(0, 255).numpy()
    # Транспонирование массива и преобразование типа данных в формат uint8
    img = img.transpose(1, 2, 0).astype("uint8")
    # Создание объекта изображения из массива NumPy
    img = Image.fromarray(img)
    # Сохранение изображения в файл
    img.save(filename)

# Функция gram_matrix(y) вычисляет матрицу Грама для заданного тензора y.
def gram_matrix(y):
    # Получение размеров тензора
    (b, ch, h, w) = y.size()
    # Преобразование тензора для подсчета матрицы Грама
    features = y.view(b, ch, w * h)
    # Транспонирование для подсчета произведения матрицы на транспонированную матрицу
    features_t = features.transpose(1, 2)
    # Вычисление матрицы Грама
    gram = features.bmm(features_t) / (ch * h * w)
    return gram

# Функция normalize_batch(batch) нормализует пакет изображений.
def normalize_batch(batch):
    # Нормализация с использованием средних и стандартных отклонений ImageNet
    mean = batch.new_tensor([0.485, 0.456, 0.406]).view(-1, 1, 1)
    std = batch.new_tensor([0.229, 0.224, 0.225]).view(-1, 1, 1)
    # Деление на 255 для приведения значений пикселей к диапазону от 0 до 1
    batch = batch.div_(255.0)
    # Нормализация с использованием средних и стандартных отклонений
    return (batch - mean) / std
