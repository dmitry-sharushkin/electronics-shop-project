"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


class TesteItem:

    def test_calculate_total_price(self):
        item = Item("Смартфон", 10000, 20)
        assert item.calculate_total_price() == 200000

    def test_apply_discount(self):
        Item.pay_rate = 0.8
        item = Item("Смартфон", 10000, 20)
        item.apply_discount()
        assert item.price == 8000.0

    def test_instances(self):
        item1 = Item("Смартфон", 10000, 20)
        item2 = Item("Ноутбук", 20000, 5)
        assert item1 in Item.all
        assert item2 in Item.all


def test_name():
    item = Item('Телефон', 10000, 5)

    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'Смартфон2'
    assert item.name == 'Смартфон2'
    with pytest.raises(Exception):
        item.name = 'Длина наименования товара превышает 10 символов'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Компьютер", 20000, 5)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Компьютер', 20000, 5)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Компьютер", 20000, 5)
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Компьютер'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item1 + 1000 is None


def test_instantiate_from_csv_str():
    csv_error = InstantiateCSVError()
    assert str(csv_error) == 'Файл item.csv поврежден'


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()
        raise FileNotFoundError("Отсутствует файл items.csv")


def test_instantiate_from_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
        raise InstantiateCSVError
