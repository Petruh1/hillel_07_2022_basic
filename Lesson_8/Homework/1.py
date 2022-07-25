class Product:
    def __init__(self, name, color, price, amount, discount):
        self.name = name
        self.color = color
        self.price = price
        self.amount = amount
        self.discount = discount

    def get_product_description(self):
        return f"{self.name}/{self.color}: {self.price} | {self.amount}"

    def show_description(self):
        print(f"Description: {self.get_product_description()}")

    def get_price(self):
        price = self.price * self.discount
        print(f"New price for {self.name} - {price}")


class Phone(Product):
    def __init__(self, name, color, price, amount, discount, lte=False):
        # Product.__init__(self, name, color, price, amount)
        super().__init__(name, color, price, amount, discount)
        self.lte = lte

    def get_product_description(self):
        additional = ", LTE" if self.lte else ""
        message = super().get_product_description()
        message += additional

        return message

    # def show_description(self):
    #     # if self.lte is True:
    #     #     additional = "LTE"
    #     # else:
    #     #     additional = ""
    #     additional = "LTE" if self.lte else ""
    #     print(f"Description: {self.name}/{self.color}: {self.price} | {self.amount}, {additional}")


class Laptop(Product):
    def __init__(self, motherboard_type, material, name, color, price, amount, discount):
        super().__init__(name, color, price, amount, discount)
        self.motherboard_type = motherboard_type
        self.material = material

    def get_product_description(self):
        price = self.price * self.discount if self.discount else self.price
        self.price = price
        return f"{self.name}/{self.color}: {self.price} | {self.amount}, {self.motherboard_type}," \
               f" material - {self.material}"


iphone7 = Phone(name="iPhone 7", color="red", price=700.0, amount=1, discount=0.50)
iphone13 = Phone(name="iPhone 13", color="black", price=2000.0, amount=2, lte=True, discount=0.70)
lenovo = Laptop(name="Lenovo", color="grey", price=3000.0, amount=1, discount=2, motherboard_type="ATX",
                material="steel")

iphone13.show_description()
iphone7.show_description()

lenovo.show_description()

iphone13.get_price()
iphone7.get_price()
