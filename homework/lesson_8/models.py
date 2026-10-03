from operator import truediv


class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int


    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity


    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity # «Не надо проверять условие и потом решать, какое слово вернуть.
        # Просто посчитай сравнение и сразу отдай то, что получилось»


    def check_invalid_quantity(self, quantity) -> bool:
        """
        Проверка но ввод значений <= 0
        """
        return quantity > 0


    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
            # return self.quantity
        else:
            raise ValueError("Запрошено больше, чем есть в наличии")


    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products: # Если товар уже есть — прибавляем к нему количество.
            self.products[product] += buy_count
        else:                        # Если нет — создаём новую запись с этим количеством.
            self.products[product] = buy_count
# У каждой отдельной корзины есть свой собственный пустой словарь. Этот словарь хранит товары, которые положил в неё конкретный покупатель.
# Ключи этого словаря — это сами объекты продуктов (apple, banana), а значения — количество этих продуктов.
# Запись вида self.products[product] — это обращение к конкретному элементу словаря по ключу


    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product not in self.products: # проверка удаления из корзины несуществующего товара
            raise ValueError(f"Товара '{product.name}' нет в корзине")
        elif remove_count is None or remove_count > self.products[product]:
            del self.products[product] # self.products[product] — это текущее количество этого товара у покупателя в корзине
        else:
            self.products[product] -= remove_count

# self.products - это и есть полностью наша корзина
# self.products[product] - это ровно то число, которое показывает, сколько именно этого конкретного товара лежит в корзине у данного покупателя
# self.products[product] - текущее состояние позиции в корзине
# Когда ты пишешь self.products[apple], ты говоришь Python'у: *«Возьми мой текущий объект корзины».
# «Найди внутри его атрибута .products тот самый товар-яблоко». «Покажи мне значение, привязанное к этому товару».

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product, quantity in self.products.items():
# .items(): Это специальный метод словарей Python. Он превращает весь словарь в список пар (ключ, значение) и выдаёт эти пары одну за другой.
# Множественное присвоение (for p,q in...)На каждой итерации цикла Python берёт очередную пару из словаря и распаковывает её в две разные переменные.
# Переменная product получает ссылку на текущий объект товара (экземпляр класса Product). Именно через неё мы можем обратиться к цене: product.price.
# Переменная quantity получает конкретное число штук именно в этой корзине. Она имеет тип int.
            total_price += float(product.price) * quantity
        return float(total_price)

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        try:
            for product, quantity in self.products.items():
                if ...
        except ValueError as e:
                    raise ValueError("Товаров не достаточно на складе")

# current_qty_in_cart = self.products[product]  # сколько штук этого товара лежит именно у покупателя в корзине.
# available_on_stock = product.quantity  # остаток этого же самого товара на общем складе магазина.