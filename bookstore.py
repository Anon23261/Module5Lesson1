from datetime import datetime

class Author:
    def __init__(self, first_name, last_name, email, biography=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.biography = biography
        self.books = []
        self.created_date = datetime.now()
        self.updated_date = datetime.now()

class Publisher:
    def __init__(self, name, address=None, phone=None, email=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.created_date = datetime.now()
        self.updated_date = datetime.now()

class Book:
    def __init__(self, isbn, title, publisher, price, stock_quantity=0, publication_date=None, genre=None, description=None):
        self.isbn = isbn
        self.title = title
        self.publisher = publisher
        self.price = price
        self.stock_quantity = stock_quantity
        self.publication_date = publication_date
        self.genre = genre
        self.description = description
        self.authors = []
        self.reviews = []
        self.created_date = datetime.now()
        self.updated_date = datetime.now()

    def add_author(self, author):
        if author not in self.authors:
            self.authors.append(author)
            author.books.append(self)

class Customer:
    def __init__(self, first_name, last_name, email, phone=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = datetime.now()
        self.orders = []
        self.reviews = []
        self.created_date = datetime.now()
        self.updated_date = datetime.now()

class Order:
    def __init__(self, customer, shipping_address=None):
        self.customer = customer
        self.order_date = datetime.now()
        self.total_amount = 0
        self.status = "Pending"
        self.shipping_address = shipping_address or customer.address
        self.order_details = []
        self.created_date = datetime.now()
        self.updated_date = datetime.now()
        customer.orders.append(self)

    def add_book(self, book, quantity, unit_price=None):
        if book.stock_quantity >= quantity:
            unit_price = unit_price or book.price
            subtotal = unit_price * quantity
            self.order_details.append(OrderDetail(self, book, quantity, unit_price, subtotal))
            self.total_amount += subtotal
            book.stock_quantity -= quantity
            return True
        return False

class OrderDetail:
    def __init__(self, order, book, quantity, unit_price, subtotal):
        self.order = order
        self.book = book
        self.quantity = quantity
        self.unit_price = unit_price
        self.subtotal = subtotal
        self.created_date = datetime.now()
        self.updated_date = datetime.now()

class Review:
    def __init__(self, book, customer, rating, comment=None):
        self.book = book
        self.customer = customer
        self.rating = min(max(rating, 1), 5)  # Rating between 1 and 5
        self.comment = comment
        self.review_date = datetime.now()
        self.created_date = datetime.now()
        self.updated_date = datetime.now()
        book.reviews.append(self)
        customer.reviews.append(self)

class BookStore:
    def __init__(self):
        self.books = []
        self.authors = []
        self.publishers = []
        self.customers = []
        self.orders = []
        
    def add_publisher(self, name, address=None, phone=None, email=None):
        publisher = Publisher(name, address, phone, email)
        self.publishers.append(publisher)
        return publisher
        
    def add_author(self, first_name, last_name, email, biography=None):
        author = Author(first_name, last_name, email, biography)
        self.authors.append(author)
        return author
    
    def add_book(self, isbn, title, publisher, price, authors=None, stock_quantity=0, 
                publication_date=None, genre=None, description=None):
        book = Book(isbn, title, publisher, price, stock_quantity, publication_date, genre, description)
        if authors:
            for author in authors:
                book.add_author(author)
        self.books.append(book)
        return book
    
    def add_customer(self, first_name, last_name, email, phone=None, address=None):
        customer = Customer(first_name, last_name, email, phone, address)
        self.customers.append(customer)
        return customer
    
    def create_order(self, customer, shipping_address=None):
        order = Order(customer, shipping_address)
        self.orders.append(order)
        return order
    
    def add_review(self, book, customer, rating, comment=None):
        return Review(book, customer, rating, comment)
    
    def find_book_by_isbn(self, isbn):
        return next((book for book in self.books if book.isbn == isbn), None)
    
    def find_books_by_author(self, author):
        return author.books
    
    def get_customer_orders(self, customer):
        return customer.orders
    
    def get_book_reviews(self, book):
        return book.reviews
    
    def get_top_rated_books(self, limit=10):
        rated_books = [(book, sum(review.rating for review in book.reviews)/len(book.reviews)) 
                      for book in self.books if book.reviews]
        return sorted(rated_books, key=lambda x: x[1], reverse=True)[:limit]
    
    def get_low_stock_books(self, threshold=5):
        return [book for book in self.books if book.stock_quantity <= threshold]

# Example usage
if __name__ == "__main__":
    # Create a new bookstore
    store = BookStore()
    
    # Add a publisher
    publisher = store.add_publisher("Penguin Books", "123 Publishing St", "555-0123", "contact@penguin.com")
    
    # Add authors
    author1 = store.add_author("F. Scott", "Fitzgerald", "fscott@email.com", "Famous American novelist")
    author2 = store.add_author("George", "Orwell", "gorwell@email.com", "English novelist and essayist")
    
    # Add books
    book1 = store.add_book("978-0743273565", "The Great Gatsby", publisher, 9.99, [author1], 5)
    book2 = store.add_book("978-0451524935", "1984", publisher, 12.99, [author2], 3)
    
    # Add a customer
    customer = store.add_customer("John", "Doe", "john@email.com", "555-0100", "456 Reader Lane")
    
    # Create an order
    order = store.create_order(customer)
    order.add_book(book1, 2)
    
    # Add a review
    store.add_review(book1, customer, 5, "A masterpiece!")
    
    # Print some information
    print(f"Book: {book1.title}")
    print(f"Author: {book1.authors[0].first_name} {book1.authors[0].last_name}")
    print(f"Stock: {book1.stock_quantity}")
    print(f"Reviews: {len(book1.reviews)}")
    print(f"Customer orders: {len(customer.orders)}")
    print(f"Order total: ${order.total_amount:.2f}")
