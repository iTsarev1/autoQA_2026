import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    current_address: str
    permanent_address: str

customer = User(full_name='Заказчик Заказчиков', email='tsarev@mailforspam.com',
                current_address='683024, край Камчатский, Петропавловск-Камчатский, 50 лет Октября, 13Б',
                permanent_address='край Камчатский')
supplier = User(full_name='Поставщик Поставщиков', email='test.post666@mailforspam.net',
                current_address='127055, город Москва, город Москва, Сущёвский Вал, дом 2, помещение 23, район Тверской',
                permanent_address='Moscow region')
admin = User(full_name='Tsarev Ilya Vladimirovich', email='itsarev.111@gmail.com', current_address='Saratov, Shevyrevskaya, 2a-23',
             permanent_address='Saratov region')