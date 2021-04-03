from abc import ABC


class Pizza:
    def __init__(self):
        self.size = None
        self.has_bacon = False
        self.has_bacon = False
        self.has_egg = False
        self.cheese = None

    def __str__(self):
        return (
            f"Tamanho: {self.size}, tem bacon: {self.has_bacon}, "
            f"tem ovo: {self.has_egg}, queijo: {self.cheese}"
        )


class Director:
    _builder = None

    def set_builder(self, builder):
        self._builder = builder

    def get_pizza(self):
        self._builder.create_pizza()
        self._builder.set_size()
        self._builder.add_bacon()
        self._builder.add_egg()
        self._builder.set_cheese()
        return self._builder.get_pizza()


class PizzaBuilder(ABC):
    def create_pizza(self):
        self._pizza = Pizza()

    def set_size(self):
        pass

    def add_bacon(self):
        pass

    def add_egg(self):
        pass

    def set_cheese(self):
        pass

    def get_pizza(self):
        return self._pizza


class PortuguesaBigBuilder(PizzaBuilder):
    def set_size(self):
        self._pizza.size = "big"

    def add_bacon(self):
        self._pizza.has_bacon = True

    def add_egg(self):
        self._pizza.has_egg = True

    def set_cheese(self):
        self._pizza.cheese = "mozzarella"


class MargueritaSmallBuilder(PizzaBuilder):
    def set_size(self):
        self._pizza.size = "small"

    def add_bacon(self):
        self._pizza.has_bacon = False

    def add_egg(self):
        self._pizza.has_egg = False

    def set_cheese(self):
        self._pizza.cheese = "mozzarella"


class CalabresaBigBuilder(PizzaBuilder):
    def set_size(self):
        self._pizza.size = "big"

    def add_bacon(self):
        self._pizza.has_bacon = False

    def add_egg(self):
        self._pizza.has_egg = False

    def set_cheese(self):
        self._pizza.cheese = "sem queijo"


portuguesa_builder = PortuguesaBigBuilder()
marguerita_builder = MargueritaSmallBuilder()
calabresa_builder = CalabresaBigBuilder()

director = Director()

director.set_builder(portuguesa_builder)
print("-- Portuguesa: ", director.get_pizza())

director.set_builder(marguerita_builder)
print("-- Marguerita: ", director.get_pizza())

director.set_builder(calabresa_builder)
print("-- Calabresa: ", director.get_pizza())
