class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

class Bookstore:
    def __init__(self):
        self.books = []
        
    def add_book(self, title, author, price, quantity):
        book = Book(title, author, price, quantity)
        self.books.append(book)
        return f"Added {title} by {author}"
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def sell_book(self, title):
        book = self.find_book(title)
        if book:
            if book.quantity > 0:
                book.quantity -= 1
                return f"Sold {book.title} for ${book.price}"
            return "Book out of stock"
        return "Book not found"
    
    def list_books(self):
        if not self.books:
            return "No books in store"
        book_list = []
        for book in self.books:
            book_list.append(f"{book.title} by {book.author} - ${book.price} ({book.quantity} in stock)")
        return "\n".join(book_list)

# Example usage
if __name__ == "__main__":
    # Create a new bookstore
    store = Bookstore()
    
    # Add some books
    print(store.add_book("The Great Gatsby", "F. Scott Fitzgerald", 9.99, 5))
    print(store.add_book("1984", "George Orwell", 12.99, 3))
    
    # List all books
    print("\nCurrent inventory:")
    print(store.list_books())
    
    # Sell some books
    print("\nSelling books:")
    print(store.sell_book("1984"))
    print(store.sell_book("The Great Gatsby"))
    
    # List updated inventory
    print("\nUpdated inventory:")
    print(store.list_books())
