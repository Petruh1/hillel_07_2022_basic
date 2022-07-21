
class Stadium:
    def __init__(self, name, open_date, country, city, amount):
        self.name = name
        self.open = open_date
        self.country = country
        self.city = city
        self.amount = amount
    def show_details(self):
        print(f"Stadium {self.name}\n"
              f"was opened in {self.open}\n"
              f"Country: {self.country}\n"
              f"City: {self.city}\n"
              f"Amount of people {self.amount}")
    def location(self):
        print(f"{self.name} located in {self.city} {self.country}")

santiago_bernabeu = Stadium(name="Santiago Bernabeu", open_date="14.12.1947",
                            country="Spain", city="Madrid", amount=81044)

arena_lviv = Stadium(name="Arena Lviv", open_date="29.10.2011", country="Ukraine",
                     city="Lviv", amount=34915)

santiago_bernabeu.show_details()
arena_lviv.location()