# Группа 10 - Проект для Dataton от Skillfactory Науки о Данных

## Описание файлов приложения:

### Ветки (branches) в данном репозитории:

- ```main``` (файлы для **продакшн**), есть готовый [домен](https://dataton.streamlit.app), который будет работать на GPU
- ```bot-branch``` - папка с файлами для **бота** (бот работает по [ссылке](@barbarartbot) или в поиске телеграм: @barbarartbot)
- ```web``` - папка с файлами для **приложения**

### Папки: 
- ```images```
   - output images -- картинки, которые получили после применения фильтра
   - style-images -- картинки, использованные для обучения моделей (сами фильтры)
- ```models``` -- обученные модели
- ```presentation``` -- презентация проекта в формате pdf

### Файлы главного репозитория: 

- ```__init__.py``` -- инициализация приложения

- ```main.py``` -- код для запуска приложения на streamlit

- ```neural_style.py``` -- код для обучения модели

- ```requirements.txt``` -- зависимости для работы приложения

- ```style.py``` -- основной код для использования обученных моделей в main.py

- ```transformer_net.py``` -- это архитектура, целью которой является решение последовательных задач при обработке долгосрочных зависимостей. Файл содержит модель стиля

- ```utils.py``` -- утилиты для обучения модели

- ```vgg.py``` -- файл под лицензией Pytorch. VGG означает группу визуальной геометрии; это стандартная архитектура глубокой сверточной нейронной сети (CNN) с несколькими уровнями. Это класс Vgg16.

  ![web](https://github.com/javascript-queen/dataton/assets/90614620/433491e9-1da4-40ff-8995-1cee6e47995a)

### Состав группы 10:
- Анна Трэйлор
- Леонид Бахтияров
- Алёна Драгунская
- Марина Яськова
- Елена Петушкова

## Задание

### 1. Описание задания:
#### «Умный городской гид»

**Задача проекта** — улучшить опыт от посещения музеев, городов или новых мест.
**Цель проекта** — сделать посещение людьми музеев, городов или новых мест интересным, информативным и комфортным.

### 2. Бизнес-идея: *стилизуй свои фото/селфи в стиле картины*
Мы решили создать бота и приложение для наложения фильтра на свои селфи. Программы позволяют выбрать понравившийся стиль искусства, представленный в коллекции музея и наложить на себя фильтр, созданный обученной моделью Neural Style Transfer.

### 3. Использованные стилей из картин Русского Музея:
На [сайте](https://ticket.rusmuseum.ru) Русского Музея большой простор для поиска вдохновения. Мы решили взять несколько основных стилей искусства, представленный в музее и создать из них фильтры для наложения на свои собственные селфи.

## Приложение 

### 1. Пример работы приложения (гиф):

![ezgif com-optimize](https://github.com/javascript-queen/dataton/assets/90614620/9bf3e723-b01c-4219-b747-21ee28938e86)

### 2. Пример работы приложения (картинки):

1. Input image:
   
   ![selfie-kid](https://github.com/javascript-queen/dataton/assets/90614620/ff1cbe9f-e425-4e81-98fb-11861f926bf4)

3. Output images:
   - Абстракционизм:
     
   ![Abstract](https://github.com/javascript-queen/dataton/assets/90614620/cdde5cd6-2b9d-4888-934d-1a287ab827c7)

   ![Abstract-selfie-kid](https://github.com/javascript-queen/dataton/assets/90614620/e7b9dad7-1a92-4c65-85ec-d9127b24e61e)

   - Арт нуво:
  
     ![Art Nouveau](https://github.com/javascript-queen/dataton/assets/90614620/7df733a9-a607-4606-a506-3e36edb98b8a)
  
     ![Art Nouveau-selfie-kid](https://github.com/javascript-queen/dataton/assets/90614620/da3181f6-0c67-4ba9-b7da-5d004bfa4711)

   - Поп Арт:
  
     ![Pop Art](https://github.com/javascript-queen/dataton/assets/90614620/f23a1340-31fc-4a3d-b19e-f7aabe69a7fc)
     
     ![Pop Art-selfie-kid](https://github.com/javascript-queen/dataton/assets/90614620/9f07507a-951c-43d5-9b94-6b48c37f85e5)

   - Кубизм:
     
   ![Cubism](https://github.com/javascript-queen/dataton/assets/90614620/c61c61d1-6b65-4045-a4c7-cfb51a2ff2f1)

   ![Cubism-selfie-kid](https://github.com/javascript-queen/dataton/assets/90614620/f93a03dd-c495-4948-9ee3-c2e82fe1ec77)
   
### 3. Как запускать приложение локально:
1. Склонировать репозиторий локально
   - загрузка [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
   ```
   # git clone https://github.com/javascript-queen/dataton.git
   ```
2. Запустить venv в общей папке:
    ```
   # python3 -m venv venv
   # . venv/bin/activate
   ```

3. Загрузить dependencies:
   ```
   # pip install streamlit
   # pip install torch torchvision
   ```
   
4. Запустить streamlit приложение:
   ```
   # streamlit run main.py
   ```

## Описание файлов приложения:

### Папки: 
- ```images```
   - output images -- картинки, которые получили после применения фильтра
   - style-images -- картинки, использованные для обучения моделей (сами фильтры)

- ```models``` -- обученные модели

### Файлы главного репозитория: 

- ```__init__.py``` -- инициализация приложения

- ```main.py``` -- код для запуска приложения на streamlit

- ```neural_style.py``` -- код для обучения модели

- ```requirements.txt``` -- зависимости для работы приложения

- ```style.py``` -- основной код для использования обученных моделей в main.py

- ```transformer_net.py``` -- это архитектура, целью которой является решение последовательных задач при обработке долгосрочных зависимостей. Файл содержит модель стиля

- ```utils.py``` -- утилиты для обучения модели

- ```vgg.py``` -- файл под лицензией Pytorch. VGG означает группу визуальной геометрии; это стандартная архитектура глубокой сверточной нейронной сети (CNN) с несколькими уровнями. Это класс Vgg16.

## Модель

### 1. Neural Style Transfer:

Алгоритм NST, разработанный Леоном Гатисом, Александром Экером и Матиасом Бетге, преобразует изображение в соответствии с выбранным стилем путем объединения содержания изображения контента с художественным стилем изображения стиля. Он оперирует двумя ключевыми изображениями: изображением контента, содержащим основной интерес, и изображением стиля, которое представляет художественные элементы, такие как цвета и текстуры. Алгоритм модифицирует входные данные таким образом, чтобы сохранить содержание изображения контента и в то же время передать художественный стиль изображения стиля. Для этой цели авторы используют сверточную нейронную сеть VGG16 в качестве модели.

### 2. Описание модели:

Модель лучше рассмотреть при помощи визуализации:

![Image1](https://github.com/javascript-queen/dataton/assets/90614620/5372baaa-15d7-4e9c-8e83-0c0b31268270)


Источник: [Ссылка на статью Medium](https://towardsdatascience.com/neural-style-transfer-tutorial-part-1-f5cd3315fa7f) (! может, пригодится VPN)

### 3. Как обучить свою модель, используя данный репозиторий:

#### Стилизация изображений:

Команда в терминале:
```
python neural_style/neural_style.py eval --content-image </path/to/content/image> --model </path/to/saved/model> --output-image </path/to/output/image> --cuda 0
```

Объяснение содержания кода для командной строки:

```--content-image:``` путь к изображению контента, которое вы хотите стилизовать.

```--model:``` сохраненная модель, которая будет использоваться для стилизации изображения (например: mosaic.pth)

```--output-image:``` путь для сохранения выходного изображения.

```--content-scale:``` коэффициент масштабирования изображения контента для уменьшения размера, если есть проблемы с памятью (например, значение 2 уменьшит высоту и ширину изображения контента в два раза).

```--cuda:``` установите значение 1 для выполнения на GPU, 0 для выполнения на CPU.

#### Тренировка модели

Команда в терминале:
```
python neural_style/neural_style.py train --dataset </path/to/train-dataset> --style-image </path/to/style/image> --save-model-dir </path/to/save-model/folder> --epochs 2 --cuda 1
```
Объяснение содержания кода для командной строки:


```--dataset:``` путь к обучающему набору данных, должен указывать на папку, содержащую еще одну папку со всеми обучающими изображениями. Например, можно воспользоваться данными датасетами:
 - [датасет-1](https://cocodataset.org/#download)

```--style-image:``` путь к изображению стиля.

```--save-model-dir:``` путь к папке, где будет сохранена обученная модель.

```--cuda:``` установите значение 1 для выполнения на GPU, 0 для выполнения на CPU.

Обратитесь к neural_style/neural_style.py для других параметров командной строки. Для обучения новых моделей вам может потребоваться настроить значения --content-weight и --style-weight. 

#### Лицензия

- Модель была предоставлена официальным (репозиторием PyTorch)[https://github.com/pytorch/examples/tree/main] для обучения моделей машинного обучения на локальных компьютерах.
  
- Все изображения взяты с официальных иточников свободных для использования:
   - [freepik](https://www.freepik.com)
   - [Русский музей (виртуальная коллекция)](https://rusmuseumvrm.ru/collections/index.php)
 
## Планы развития

У нас в дальнейших планах намечаются следующие проекты:
- доработка бота
- деплой веб-приложения на React
- деплой мобильного приложения на React Native

Ниже представлены дизайны будущих проектов:

![web](https://github.com/javascript-queen/dataton/assets/90614620/433491e9-1da4-40ff-8995-1cee6e47995a)

![app](https://github.com/javascript-queen/dataton/assets/90614620/ec9a4a43-7d7f-42fc-9f66-5ae1d13106c4)

## Бот
### 1. Скрипт:
- Скрипт бота находится в ветви bot-branch(готовые скрипты) и bot (прошлые наработки бота и описание проекта)
### 2. Телеграм-бот:
- Ботом можно будет пользоваться в телеграме: [ссылка](t.me/barbarartbot)
### 3. Работа телеграм-бота:
  ![bot_Artboard 1](https://github.com/javascript-queen/dataton/assets/90614620/c9367226-f67c-4ab0-aa4c-8daaec28fa4a)


