class Book:
    TYPES = ("hardcover", "paperback")
  
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
  
    # to return the details.
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight)

book = Book.hardcover("Harry Potter", 1500)
lightbook = Book.hardcover("Python 101", 600)

print(book)
print(lightbook)

print(f"Lighter book weighs {lightbook.weight}g")


return f"{store.name}, total stock price: {sum([item['price'] item in store.items])}"


return cls(store.name + 'flkgjlkfgjh')

return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))