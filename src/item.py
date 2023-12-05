import os.path


class InstantiateCSVError(Exception):
    def __init__(self):
        self.error = 'Файл item.csv поврежден'

    def __str__(self):
        return self.error


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> int:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.pay_rate * self.price)
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        """Проверяет, что длина наименования товара не больше 10 символов."""
        if len(self.__name) <= 10:
            self.__name = name
        elif len(self.__name) > 10:
            self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Класс-метод, который принимает путь к документу с значениями.
        Открывает документ и преобразовывает его в словарь.
        Инициализирует значения под атрибуты класса
        """
        if not os.path.exists(path):
            raise FileNotFoundError('Отсутствует файл item.csv')
        import csv
        cls.all.clear()
        string_count = 0
        with open(path, 'r', newline='', encoding='cp1251') as attributes:
            attribute = csv.DictReader(attributes)
            for attr in attribute:
                name = attr['name']
                price = cls.string_to_number(attr['price'])
                quantity = cls.string_to_number(attr['quantity'])
                items_csv = Item(name, price, quantity)
                string_count += 1
            if string_count < 5:
                raise InstantiateCSVError
            return items_csv

    @staticmethod
    def string_to_number(string: str):
        if string.isdigit:
            if '.' in string:
                string = int(float(string))
            else:
                string = int(string)
            return string

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
