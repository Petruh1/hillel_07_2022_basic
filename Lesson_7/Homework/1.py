class Car:
    def __init__(self, name_producent, model, graduation, engine_capacity, color, price):
        self.name_producent = name_producent
        self.model = model
        self.age = graduation
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def show_details(self):
        print(f"Car is {self.name_producent} {self.model}, year of production {self.age},"
              f"engine is {self.engine_capacity}, color {self.color}, price {self.price}")

    def show_price(self):
        print(f"{self.name_producent} {self.model} price is {self.price}")


ford_focus = Car(name_producent="Ford", model="Focus cabrio", graduation=2007, engine_capacity=2.0, color="blue", price=20000)
opel_vectra = Car(name_producent="Opel", model="Vectra", graduation=2004, engine_capacity=1.8, color="white", price=10000)

ford_focus.show_details()

Car.show_price(opel_vectra)