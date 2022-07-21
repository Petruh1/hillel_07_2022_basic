class Book:
    def __init__(self, name, graduation, publish, genre, author, price):
        self.name = name
        self.graduation = graduation
        self.publish = publish
        self.genre = genre
        self.author = author
        self.price = price
    def show_details(self):
        print(f"Name book: - {self.name}\n"
              f"Graduation in: {self.graduation}\n"
              f"Published in: {self.publish}\n"
              f"Genre is {self.genre}\n"
              f"Author is {self.author}\n"
              f"Price: {self.price}\n")
    def show_genre(self):
        print(f"{self.name}: genre is {self.genre}")

harry_potter = Book(name="Harry Potter and the Philosopher's Stone", graduation=1997, publish=2016, genre="fantasy",
                    author="Joanne Rowling", price=700)

Book.show_details(harry_potter)

harry_potter.show_genre()


