import pytest

from src.item import Item


@pytest.fixture
def item_fortest():
    return Item("Планшет", 15000, 15)


def test_item_init(item_fortest):
    """Когда мы создаем экземпляр класса со значением Х, то get_value вернет нам Х."""
    assert item_fortest.name == "Планшет"
    assert item_fortest.price == 15000
    assert item_fortest.quantity == 15


def test_calculate_total_price(item_fortest):
    assert item_fortest.calculate_total_price() == 225000


Item.pay_rate = 0.8


def test_apply_discount(item_fortest):
    assert item_fortest.apply_discount() == 12000
