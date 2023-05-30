"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


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
