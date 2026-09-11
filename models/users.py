from enum import Enum


class UserStatus(Enum): # «Создай мне набор постоянных констант». мы UserStatus наследуем у Enum
    student = "student"
    worker = "worker"
# Enum создаёт список разрешённых значений, которые нельзя изменить


class User:
    name = str
    age = int
    status = UserStatus
    items = list[str]

    # Чтобы этим шаблоном воспользоваться, необходимо описать конструктор класса, то есть то, как мы можем создать из вот этой абстракции,
    # абстракции user, какого-то конкретного пользователя, у которого эти поля уже будут заполнены.

    # Для этого используется функция __init__ - это функция-конструктор, в которой мы можем описать все те данные, которые
    # нужны для того, чтобы создать пользователя.
    def __init__(self, name, age, status, items):
        self.name = name
        self.age = age
        self.status = status
        self.items = items


# self - обозначает сам себя. В каждом экземпляре класса, то есть в каждом конкретном пользователе, с которым мы будем дальше работать,
# этот self будет обозначать самого этого пользователя.


if __name__ == '__main__':
    # в виде словаря наш пользователь будет выглядеть:
    d = {"name": "Oleg",
         "age": 20,
         "status": "student",
         "items": ["book"]}

    # в виде объекта наш пользователь будет выглядеть:
    oleg = User(name="Oleg", age=16, status=UserStatus.student, items=["book"])
    anna = User(name="Anna", age=17, status=UserStatus.student, items=["pen", "eraser", "notebook"])
    elena = User(name="Elena", age=15, status=UserStatus.student, items=["book", "pen"])
    ivan = User(name="Ivan", age=18, status=UserStatus.worker, items=["pen", "notebook"])
    Maria = User(name="Maria", age=23, status=UserStatus.worker, items=["book", "pen", "notebook"])
    # получается, у нас есть 4 экземпляра одного и того же класса, и эти экземпляры между собой никак не связаны.
    # они представляют собой один и тот же класс, с одним и тем же набором полей, но с разнымными значениями.

    # как мы можем это использовать в коде? мы можем обращаться к каждому экземпляру класса и брать из него какие-то атрибуты
    assert oleg.age == 16
    # Этот класс мы можем использовать в нашем тесте и можем улучшить наш код