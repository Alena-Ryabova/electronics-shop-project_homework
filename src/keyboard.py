from src.item import Item


class MixinLog:

    def __init__(self):
        """ Инициализация доступных языков"""
        self.languages = ['EN', 'RU']

    def get_lang(self):
        """ Функция возвращает список с доступными языками """
        return self.languages


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.mixin = MixinLog().get_lang()
        self.__language = self.mixin[0]

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"

    def __str__(self):
        return f"{self.name}"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Функция переключения языка"""
        if self.__language == self.mixin[0]:
            self.__language = self.mixin[1]
            return self.__language
        if self.__language == self.mixin[1]:
            self.__language = self.mixin[0]
            return self.__language
