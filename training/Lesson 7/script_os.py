import os


# Как найти файл. Работа с путями. Куда файл сохранился


# скрипт где мы сейчас находимся
# print(os.path.abspath(__file__))


current_file = os.path.abspath(__file__)

current_dir = os.path.dirname(current_file)
print(current_dir) # папка, где находится объект
# куда бы мы не скопировали наш проект, сможем узнать куда нам внутри этого проекта распределить наши tmp,
# наши файлы скачать/зачитать, сохраненки делать

tmp_dir = os.path.join(current_dir, 'tmp')
print(tmp_dir)