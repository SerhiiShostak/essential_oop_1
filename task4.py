class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f'{self.model}, {self.color} ({self.year})'


class CarShop:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def sell_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Автомобіль {car} продано")
        else:
            print("Такий автомобіль не знайдено")

    def __str__(self):
        if self.cars:
            cars_list = '\n '.join([str(car) for car in self.cars])
        else:
            cars_list = 'Автомобілів немає'
        return f'Автомобілі в магазині:\n {cars_list}'


new_shop = CarShop()

car1 = Car("Toyota", 2020, "red")
car2 = Car("Honda", 2019, "blue")
car3 = Car("BMW", 2022, "white")

new_shop.add_car(car1)
new_shop.add_car(car2)
new_shop.add_car(car3)
print(new_shop)

new_shop.sell_car(car2)
print()
print(new_shop)
print()
new_shop.sell_car(car1)
print()
print(new_shop)
print()
new_shop.sell_car(car1)