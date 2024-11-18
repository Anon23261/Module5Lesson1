from datetime import datetime

class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = []

class Book:
    def __init__(self, title, isbn, price, stock):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.stock = stock
        self.authors = []
        self.reviews = []

    def add_author(self, author):
        self.authors.append(author)
        author.books.append(self)

    def add_review(self, review):
        self.reviews.append(review)

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.books = []  # List of (book, quantity) tuples
        self.date = datetime.now()
        self.total = 0
        customer.orders.append(self)

    def add_book(self, book, quantity):
        if book.stock >= quantity:
            self.books.append((book, quantity))
            book.stock -= quantity
            self.total += book.price * quantity
        else:
            print(f"Not enough stock for {book.title}")

class Review:
    def __init__(self, customer, rating, comment):
        self.customer = customer
        self.rating = rating  # 1-5
        self.comment = comment
        self.date = datetime.now()

class BookStore:
    def __init__(self):
        self.books = []
        self.customers = []
        self.authors = []

    def add_book(self, title, isbn, price, stock):
        book = Book(title, isbn, price, stock)
        self.books.append(book)
        return book

    def add_customer(self, name, email):
        customer = Customer(name, email)
        self.customers.append(customer)
        return customer

    def add_author(self, name, email):
        author = Author(name, email)
        self.authors.append(author)
        return author

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

# Example usage
if __name__ == "__main__":
    # Create store
    store = BookStore()

    # Add authors
    author1 = store.add_author("J.K. Rowling", "jk@email.com")
    author2 = store.add_author("George Orwell", "go@email.com")

    # Add books
    book1 = store.add_book("Harry Potter", "123456", 29.99, 100)
    book2 = store.add_book("1984", "789012", 19.99, 50)

    # Link authors to books
    book1.add_author(author1)
    book2.add_author(author2)

    # Add customers
    customer1 = store.add_customer("John Doe", "john@email.com")
    customer2 = store.add_customer("Jane Smith", "jane@email.com")

    # Create orders
    order1 = Order(customer1)
    order1.add_book(book1, 2)  # Order 2 copies of Harry Potter

    # Add reviews
    review1 = Review(customer1, 5, "Great book!")
    book1.add_review(review1)

    # Print some information
    print(f"Book: {book1.title}")
    print(f"Author: {book1.authors[0].name}")
    print(f"Stock: {book1.stock}")
    print(f"Reviews: {len(book1.reviews)}")
    print(f"Customer orders: {len(customer1.orders)}")
    print(f"Order total: ${order1.total:.2f}")
