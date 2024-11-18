from sqlalchemy import func
from database import get_session
from models import Author, Publisher, Book, Customer, Order, OrderDetail, Review

def get_book_by_isbn(isbn):
    """Get book details by ISBN."""
    session = get_session()
    try:
        book = session.query(Book).filter(Book.isbn == isbn).first()
        return book
    finally:
        session.close()

def get_books_by_author(author_last_name):
    """Get all books by author's last name."""
    session = get_session()
    try:
        books = session.query(Book)\
            .join(Book.authors)\
            .filter(Author.last_name == author_last_name)\
            .all()
        return books
    finally:
        session.close()

def get_customer_orders(customer_email):
    """Get all orders for a customer."""
    session = get_session()
    try:
        orders = session.query(Order)\
            .join(Customer)\
            .filter(Customer.email == customer_email)\
            .all()
        return orders
    finally:
        session.close()

def get_book_reviews(isbn):
    """Get all reviews for a book."""
    session = get_session()
    try:
        reviews = session.query(Review)\
            .join(Book)\
            .filter(Book.isbn == isbn)\
            .all()
        return reviews
    finally:
        session.close()

def get_top_rated_books(limit=5):
    """Get top rated books based on average review rating."""
    session = get_session()
    try:
        top_books = session.query(
            Book,
            func.avg(Review.rating).label('avg_rating'),
            func.count(Review.review_id).label('review_count')
        )\
            .join(Review)\
            .group_by(Book)\
            .order_by(func.avg(Review.rating).desc())\
            .limit(limit)\
            .all()
        return top_books
    finally:
        session.close()

def get_bestselling_books(limit=5):
    """Get bestselling books based on order quantity."""
    session = get_session()
    try:
        bestsellers = session.query(
            Book,
            func.sum(OrderDetail.quantity).label('total_sold')
        )\
            .join(OrderDetail)\
            .group_by(Book)\
            .order_by(func.sum(OrderDetail.quantity).desc())\
            .limit(limit)\
            .all()
        return bestsellers
    finally:
        session.close()

def get_customer_spending(customer_email):
    """Get total spending for a customer."""
    session = get_session()
    try:
        total = session.query(func.sum(Order.total_amount))\
            .join(Customer)\
            .filter(Customer.email == customer_email)\
            .scalar()
        return total or 0
    finally:
        session.close()

def get_low_stock_books(threshold=10):
    """Get books with stock quantity below threshold."""
    session = get_session()
    try:
        books = session.query(Book)\
            .filter(Book.stock_quantity <= threshold)\
            .all()
        return books
    finally:
        session.close()

# Example usage
if __name__ == '__main__':
    # Get book by ISBN
    book = get_book_by_isbn('9780141439518')
    if book:
        print(f"Book: {book.title} by {', '.join([author.first_name + ' ' + author.last_name for author in book.authors])}")
    
    # Get books by author
    books = get_books_by_author('Rowling')
    for book in books:
        print(f"Book by J.K. Rowling: {book.title}")
    
    # Get customer orders
    orders = get_customer_orders('john.smith@email.com')
    for order in orders:
        print(f"Order {order.order_id}: ${order.total_amount} - {order.status}")
    
    # Get top rated books
    top_books = get_top_rated_books(3)
    for book, avg_rating, review_count in top_books:
        print(f"{book.title}: {avg_rating:.1f} stars ({review_count} reviews)")
    
    # Get bestselling books
    bestsellers = get_bestselling_books(3)
    for book, total_sold in bestsellers:
        print(f"{book.title}: {total_sold} copies sold")
