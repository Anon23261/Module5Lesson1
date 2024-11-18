from datetime import datetime
from decimal import Decimal
from database import get_session
from models import Author, Publisher, Book, BookAuthor, Customer, Order, OrderDetail, Review

def seed_database():
    session = get_session()
    
    try:
        # Add Publishers
        publishers = [
            Publisher(
                name='Penguin Books',
                address='123 Publishing Ave, New York, NY 10001',
                phone='212-555-0123',
                email='contact@penguin.com'
            ),
            Publisher(
                name='HarperCollins',
                address='456 Book Street, Chicago, IL 60601',
                phone='312-555-0456',
                email='info@harpercollins.com'
            ),
            Publisher(
                name='Random House',
                address='789 Literature Lane, Boston, MA 02108',
                phone='617-555-0789',
                email='support@randomhouse.com'
            )
        ]
        session.add_all(publishers)
        session.flush()  # Flush to get publisher IDs
        
        # Add Authors
        authors = [
            Author(
                first_name='Jane',
                last_name='Austen',
                biography='English novelist known for romantic fiction',
                email='jane.austen@literature.com'
            ),
            Author(
                first_name='George',
                last_name='Orwell',
                biography='English novelist and essayist',
                email='george.orwell@literature.com'
            ),
            Author(
                first_name='J.K.',
                last_name='Rowling',
                biography='British author best known for Harry Potter series',
                email='jk.rowling@literature.com'
            ),
            Author(
                first_name='Stephen',
                last_name='King',
                biography='American author of horror and fantasy novels',
                email='stephen.king@literature.com'
            )
        ]
        session.add_all(authors)
        session.flush()  # Flush to get author IDs
        
        # Add Books
        books = [
            Book(
                isbn='9780141439518',
                title='Pride and Prejudice',
                publisher_id=publishers[0].publisher_id,
                publication_date=datetime(1813, 1, 28).date(),
                price=Decimal('14.99'),
                stock_quantity=50,
                genre='Classic Romance',
                description='A romantic novel of manners...'
            ),
            Book(
                isbn='9780451524935',
                title='1984',
                publisher_id=publishers[0].publisher_id,
                publication_date=datetime(1949, 6, 8).date(),
                price=Decimal('12.99'),
                stock_quantity=75,
                genre='Dystopian Fiction',
                description='A dystopian social science fiction novel...'
            ),
            Book(
                isbn='9780439708180',
                title='Harry Potter and the Sorcerer''s Stone',
                publisher_id=publishers[1].publisher_id,
                publication_date=datetime(1997, 6, 26).date(),
                price=Decimal('24.99'),
                stock_quantity=100,
                genre='Fantasy',
                description='The first book in the Harry Potter series...'
            ),
            Book(
                isbn='9781501142970',
                title='The Shining',
                publisher_id=publishers[2].publisher_id,
                publication_date=datetime(1977, 1, 28).date(),
                price=Decimal('16.99'),
                stock_quantity=30,
                genre='Horror',
                description='A horror novel set in an isolated hotel...'
            )
        ]
        session.add_all(books)
        session.flush()  # Flush to get book IDs
        
        # Add BookAuthor relationships
        book_authors = [
            BookAuthor(book_id=books[0].book_id, author_id=authors[0].author_id),  # Pride and Prejudice - Jane Austen
            BookAuthor(book_id=books[1].book_id, author_id=authors[1].author_id),  # 1984 - George Orwell
            BookAuthor(book_id=books[2].book_id, author_id=authors[2].author_id),  # Harry Potter - J.K. Rowling
            BookAuthor(book_id=books[3].book_id, author_id=authors[3].author_id)   # The Shining - Stephen King
        ]
        session.add_all(book_authors)
        
        # Add Customers
        customers = [
            Customer(
                first_name='John',
                last_name='Smith',
                email='john.smith@email.com',
                phone='555-0101',
                address='123 Main St, Springfield, IL 62701'
            ),
            Customer(
                first_name='Mary',
                last_name='Johnson',
                email='mary.j@email.com',
                phone='555-0102',
                address='456 Oak Ave, Chicago, IL 60601'
            ),
            Customer(
                first_name='David',
                last_name='Brown',
                email='david.b@email.com',
                phone='555-0103',
                address='789 Pine Rd, Boston, MA 02108'
            ),
            Customer(
                first_name='Sarah',
                last_name='Wilson',
                email='sarah.w@email.com',
                phone='555-0104',
                address='321 Elm St, New York, NY 10001'
            )
        ]
        session.add_all(customers)
        session.flush()  # Flush to get customer IDs
        
        # Add Orders
        orders = [
            Order(
                customer_id=customers[0].customer_id,
                order_date=datetime(2023, 1, 15),
                total_amount=Decimal('27.98'),
                status='Completed',
                shipping_address='123 Main St, Springfield, IL 62701'
            ),
            Order(
                customer_id=customers[1].customer_id,
                order_date=datetime(2023, 1, 16),
                total_amount=Decimal('24.99'),
                status='Completed',
                shipping_address='456 Oak Ave, Chicago, IL 60601'
            ),
            Order(
                customer_id=customers[2].customer_id,
                order_date=datetime(2023, 1, 17),
                total_amount=Decimal('41.98'),
                status='Processing',
                shipping_address='789 Pine Rd, Boston, MA 02108'
            ),
            Order(
                customer_id=customers[3].customer_id,
                order_date=datetime(2023, 1, 18),
                total_amount=Decimal('16.99'),
                status='Shipped',
                shipping_address='321 Elm St, New York, NY 10001'
            )
        ]
        session.add_all(orders)
        session.flush()  # Flush to get order IDs
        
        # Add OrderDetails
        order_details = [
            OrderDetail(
                order_id=orders[0].order_id,
                book_id=books[0].book_id,
                quantity=1,
                unit_price=Decimal('14.99'),
                subtotal=Decimal('14.99')
            ),
            OrderDetail(
                order_id=orders[0].order_id,
                book_id=books[1].book_id,
                quantity=1,
                unit_price=Decimal('12.99'),
                subtotal=Decimal('12.99')
            ),
            OrderDetail(
                order_id=orders[1].order_id,
                book_id=books[2].book_id,
                quantity=1,
                unit_price=Decimal('24.99'),
                subtotal=Decimal('24.99')
            ),
            OrderDetail(
                order_id=orders[2].order_id,
                book_id=books[2].book_id,
                quantity=1,
                unit_price=Decimal('24.99'),
                subtotal=Decimal('24.99')
            ),
            OrderDetail(
                order_id=orders[2].order_id,
                book_id=books[3].book_id,
                quantity=1,
                unit_price=Decimal('16.99'),
                subtotal=Decimal('16.99')
            ),
            OrderDetail(
                order_id=orders[3].order_id,
                book_id=books[3].book_id,
                quantity=1,
                unit_price=Decimal('16.99'),
                subtotal=Decimal('16.99')
            )
        ]
        session.add_all(order_details)
        
        # Add Reviews
        reviews = [
            Review(
                book_id=books[0].book_id,
                customer_id=customers[0].customer_id,
                rating=5,
                comment='A timeless classic that never gets old!',
                review_date=datetime(2023, 1, 20)
            ),
            Review(
                book_id=books[1].book_id,
                customer_id=customers[1].customer_id,
                rating=4,
                comment='Thought-provoking and still relevant today.',
                review_date=datetime(2023, 1, 21)
            ),
            Review(
                book_id=books[2].book_id,
                customer_id=customers[2].customer_id,
                rating=5,
                comment='Magical and enchanting story for all ages.',
                review_date=datetime(2023, 1, 22)
            ),
            Review(
                book_id=books[3].book_id,
                customer_id=customers[3].customer_id,
                rating=4,
                comment='Absolutely terrifying! Couldn''t put it down.',
                review_date=datetime(2023, 1, 23)
            )
        ]
        session.add_all(reviews)
        
        # Commit all changes
        session.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        session.rollback()
        print(f"Error seeding database: {str(e)}")
        raise
    finally:
        session.close()

if __name__ == '__main__':
    seed_database()
