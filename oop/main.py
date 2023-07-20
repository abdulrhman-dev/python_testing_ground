# practice a decorator that has some method like argument functionality
from functools import wraps
from csv import DictReader


def item_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        item = {'name': 'Car', 'price': 2500, 'amount': 2}
        result = func(item, *args, **kwargs)
        return result
    return wrapper


@item_decorator
def calculate_price(item, x, y):
    return item['price'] + x + y


total = calculate_price(5, 10)
# print(total)

# test 2 for default values


def name_change(name, names=["abood"]):
    names.append(name)


# name_change("abdallah")
# name_change("asha")

# actual classes now YAY!


class Car:
    discount = 0.2
    all_cars = []

    def __init__(self, model: str, price: float, quantity=0) -> None:
        assert price >= 0, "Price should be positive "
        assert quantity >= 0, "Quantity should be positive "

        self.model = model
        self.__price = price
        self.quantity = quantity
        self.all_cars.append(self)

    def calculate_total_price(self) -> float:
        return self.__price * self.quantity

    def apply_discount(self) -> float:
        self.__price = self.__price - (self.__price * self.discount)
        return self.__price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        print(value)
        assert isinstance(value, float) or isinstance(
            value, int), "Price has to be a number"
        assert value >= 0, "The price needs to be positve"

        self.__price = value

    @classmethod
    def add_cars_from_csv(cls, filename: str):
        with open(filename) as file:
            cars = DictReader(file)
            for car in cars:
                cls(car["model"], float(car["price"]), float(car["quantity"]))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.model}, {self.__price }, {self.quantity})"


class SUV(Car):
    def __init__(self, model: str, price: float, quantity) -> None:
        super().__init__(model, price, quantity)


Car.add_cars_from_csv("./oop/cars.csv")
print(Car.all_cars)

my_awesome_car = Car("BMW", 150000, 1)
my_awesome_car.price = -150000.0  # WHAT?

print(my_awesome_car)

# my_personal_suv = SUV("BMW", 500000, True, 20)
# print(my_personal_suv)

# __name is for making private attr
