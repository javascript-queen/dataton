# Импорт namedtuple для создания именованных кортежей
from collections import namedtuple
# Импорт моделей из библиотеки torchvision
import torch
from torchvision import models

# Определение класса Vgg16, представляющего модель VGG-16.
class Vgg16(torch.nn.Module):
    def __init__(self, requires_grad=False):
        super(Vgg16, self).__init__()
        # Получение предварительно обученных функций (features) модели VGG16 из torchvision
        vgg_pretrained_features = models.vgg16(pretrained=True).features
        # Разделение предварительно обученных функций на четыре "среза" для извлечения различных уровней признаков
        self.slice1 = torch.nn.Sequential()
        self.slice2 = torch.nn.Sequential()
        self.slice3 = torch.nn.Sequential()
        self.slice4 = torch.nn.Sequential()

        # Добавление слоев из предварительно обученных функций в соответствующие срезы
        # Каждый срез содержит определенный набор слоев из VGG-16 для извлечения признаков
        for x in range(4):
            self.slice1.add_module(str(x), vgg_pretrained_features[x])
        for x in range(4, 9):
            self.slice2.add_module(str(x), vgg_pretrained_features[x])
        for x in range(9, 16):
            self.slice3.add_module(str(x), vgg_pretrained_features[x])
        for x in range(16, 23):
            self.slice4.add_module(str(x), vgg_pretrained_features[x])
        # Если requires_grad равно False, то устанавливаем параметры модели как не требующие градиентов
        if not requires_grad:
            for param in self.parameters():
                param.requires_grad = False

    def forward(self, X):
        # Прямой проход (forward pass) через каждый срез для извлечения признаков на разных уровнях
        h = self.slice1(X)
        h_relu1_2 = h
        h = self.slice2(h)
        h_relu2_2 = h
        h = self.slice3(h)
        h_relu3_3 = h
        h = self.slice4(h)
        h_relu4_3 = h
        
        # Используем namedtuple для возврата именованных выходов с различных слоев модели VGG-16
        vgg_outputs = namedtuple("VggOutputs", ['relu1_2', 'relu2_2', 'relu3_3', 'relu4_3'])
        out = vgg_outputs(h_relu1_2, h_relu2_2, h_relu3_3, h_relu4_3)
        return out
