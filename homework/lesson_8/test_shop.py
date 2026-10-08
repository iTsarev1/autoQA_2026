"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from homework.lesson_8.models import Product, Cart


@pytest.fixture
def cart()->Cart:
    """
    Возвращает чистую пустую корзину
    """
    return Cart()
# Ты определяешь новую фикстуру по имени cart. Она ничего не принимает на вход (() пустые), а возвращает объект класса Cart.
# Стрелочка -> Cart — это аннотация типа возвращаемого значения. Ты сообщаешь PyCharm и другим инструментам статического анализа, что эта функция вернёт именно корзину.


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """


    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(10) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False, "На складе нет такого кол-ва товара"


    def test_product_check_invalid_quantity(self, product):
        assert product.check_invalid_quantity(0) is False, "Значение должно быть больше нуля"
        assert product.check_invalid_quantity(-1) is False, f"Значение должно быть больше нуля"
        assert product.check_invalid_quantity(0.1) is True


    def test_product_buy_positive(self, product):
        # TODO напишите проверки на метод buy
        product.buy(5)
        assert product.quantity == 995


    def test_product_buy_zero(self, product):
        product.buy(1000)
        assert product.quantity == 0

    def test_product_buy_negative(self, product):
        try:
            product.buy(1001)
        except ValueError as e:
            assert str(e) == "Запрошено больше, чем есть в наличии"


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, cart, product):
        cart.add_product(product, 5)
        assert product in cart.products
        assert cart.products[product] == 5

    def test_cart_remove_product(self, cart, product):
        # добавить товар в корзину
        cart.add_product(product, 5)
        # проверка наличия товара в корзине перед удалением
        assert product in cart.products