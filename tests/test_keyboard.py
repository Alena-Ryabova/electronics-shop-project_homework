import pytest

from src.keyboard import Keyboard, MixinLog


@pytest.fixture
def keyboard_fortest():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_phone_init(keyboard_fortest):
    assert keyboard_fortest.name == "Dark Project KD87A"
    assert keyboard_fortest.price == 9600
    assert keyboard_fortest.quantity == 5
    assert keyboard_fortest.language == "EN"


def test_change_lang(keyboard_fortest):
    keyboard_fortest.change_lang()
    assert str(keyboard_fortest.language) == "RU"
    keyboard_fortest.change_lang()
    assert str(keyboard_fortest.language) == "EN"


def test_mixin_log():
    mixin = MixinLog()
    assert type(mixin.get_lang()) == list
