from src.item import Item


class Phone(Item):

    # Переопределяем метод базового класса
    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Дополнительный код
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count_sim):
        if not isinstance(count_sim, int) or count_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = count_sim
