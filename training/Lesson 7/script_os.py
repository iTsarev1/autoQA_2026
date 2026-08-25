# Как найти файл. Работа с путями. Куда файл сохранился
import os


# скрипт где мы сейчас находимся:
# print(os.path.abspath(__file__))


CURRENT_FILE = os.path.abspath(__file__)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR) # папка, где находится объект
# куда бы мы не скопировали наш проект, сможем узнать куда нам внутри этого проекта распределить наши tmp,
# наши файлы скачать/зачитать, сохраненки делать

TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
print(TMP_DIR)