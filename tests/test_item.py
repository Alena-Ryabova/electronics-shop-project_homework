import pytest

from src.item import Item, InstantiateCSVError


@pytest.fixture
def item_fortest():
    return Item("Планшет", 15000, 15)


def test_item_init(item_fortest):
    """Когда мы создаем экземпляр класса со значением Х, то get_value вернет нам Х."""
    assert item_fortest.name == "Планшет"
    assert item_fortest.price == 15000
    assert item_fortest.quantity == 15


def test_repr(item_fortest):
    """ Тест  repr"""
    assert repr(item_fortest) == "Item('Планшет', 15000, 15)"


def test_str(item_fortest):
    """ Тест  str"""
    assert str(item_fortest) == 'Планшет'


def test_calculate_total_price(item_fortest):
    """ Тест подсчета общей стоимости """
    assert item_fortest.calculate_total_price() == 225000


Item.pay_rate = 0.8


def test_apply_discount(item_fortest):
    """ Тест на применение скидки """
    assert item_fortest.apply_discount() == 12000


def test_name(item_fortest):
    """ Тест на подсчёт длинны наименования """
    assert len(item_fortest.name) <= 10
    item_fortest.name = 'Холодильник'
    assert len(item_fortest.name) == 10


def test_instantiate_from_csv():
    """ Тест на возврат верных значений из файла"""
    assert Item.instantiate_from_csv('../src/items.csv').name == "Клавиатура"
    assert Item.instantiate_from_csv('../src/items.csv').price == 75
    assert Item.instantiate_from_csv('../src/items.csv').quantity == 5


def test_file_not_found_error():
    """ Тест исключения отсутствия файла """
    with pytest.raises(FileNotFoundError, match='Отсутствует файл item.csv'):
        Item.instantiate_from_csv('../src/item.csv')


def test_instantiate_csv_error():
    """ Тест исключения на повреждение файла """
    with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
        Item.instantiate_from_csv('../src/items_for_error.csv')
