import pytest

from src.phone import Phone


@pytest.fixture
def phone_fortest():
    return Phone("Sony", 15000, 15, 2)


def test_phone_init(phone_fortest):
    """Когда мы создаем экземпляр класса со значением Х, то get_value вернет нам Х."""
    assert phone_fortest.name == "Sony"
    assert phone_fortest.price == 15000
    assert phone_fortest.quantity == 15
    assert phone_fortest.number_of_sim == 2


def test_phone_repr(phone_fortest):
    assert repr(phone_fortest) == "Phone('Sony', 15000, 15, 2)"


