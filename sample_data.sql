-- Sample Data for BookHaven Database

-- Insert Publishers
INSERT INTO Publishers (Name, Address, Phone, Email) VALUES
('Penguin Books', '123 Publishing Ave, New York, NY 10001', '212-555-0123', 'contact@penguin.com'),
('HarperCollins', '456 Book Street, Chicago, IL 60601', '312-555-0456', 'info@harpercollins.com'),
('Random House', '789 Literature Lane, Boston, MA 02108', '617-555-0789', 'support@randomhouse.com');

-- Insert Authors
INSERT INTO Authors (FirstName, LastName, Biography, Email) VALUES
('Jane', 'Austen', 'English novelist known for romantic fiction', 'jane.austen@literature.com'),
('George', 'Orwell', 'English novelist and essayist', 'george.orwell@literature.com'),
('J.K.', 'Rowling', 'British author best known for Harry Potter series', 'jk.rowling@literature.com'),
('Stephen', 'King', 'American author of horror and fantasy novels', 'stephen.king@literature.com');

-- Insert Books
INSERT INTO Books (ISBN, Title, PublisherID, PublicationDate, Price, StockQuantity, Genre, Description) VALUES
('9780141439518', 'Pride and Prejudice', 1, '1813-01-28', 14.99, 50, 'Classic Romance', 'A romantic novel of manners...'),
('9780451524935', '1984', 1, '1949-06-08', 12.99, 75, 'Dystopian Fiction', 'A dystopian social science fiction novel...'),
('9780439708180', 'Harry Potter and the Sorcerer''s Stone', 2, '1997-06-26', 24.99, 100, 'Fantasy', 'The first book in the Harry Potter series...'),
('9781501142970', 'The Shining', 3, '1977-01-28', 16.99, 30, 'Horror', 'A horror novel set in an isolated hotel...');

-- Insert BookAuthors relationships
INSERT INTO BookAuthors (BookID, AuthorID) VALUES
(1, 1), -- Pride and Prejudice - Jane Austen
(2, 2), -- 1984 - George Orwell
(3, 3), -- Harry Potter - J.K. Rowling
(4, 4); -- The Shining - Stephen King

-- Insert Customers
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES
('John', 'Smith', 'john.smith@email.com', '555-0101', '123 Main St, Springfield, IL 62701'),
('Mary', 'Johnson', 'mary.j@email.com', '555-0102', '456 Oak Ave, Chicago, IL 60601'),
('David', 'Brown', 'david.b@email.com', '555-0103', '789 Pine Rd, Boston, MA 02108'),
('Sarah', 'Wilson', 'sarah.w@email.com', '555-0104', '321 Elm St, New York, NY 10001');

-- Insert Orders
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount, Status, ShippingAddress) VALUES
(1, '2023-01-15', 27.98, 'Completed', '123 Main St, Springfield, IL 62701'),
(2, '2023-01-16', 24.99, 'Completed', '456 Oak Ave, Chicago, IL 60601'),
(3, '2023-01-17', 41.98, 'Processing', '789 Pine Rd, Boston, MA 02108'),
(4, '2023-01-18', 16.99, 'Shipped', '321 Elm St, New York, NY 10001');

-- Insert OrderDetails
INSERT INTO OrderDetails (OrderID, BookID, Quantity, UnitPrice, Subtotal) VALUES
(1, 1, 1, 14.99, 14.99),
(1, 2, 1, 12.99, 12.99),
(2, 3, 1, 24.99, 24.99),
(3, 3, 1, 24.99, 24.99),
(3, 4, 1, 16.99, 16.99),
(4, 4, 1, 16.99, 16.99);

-- Insert Reviews
INSERT INTO Reviews (BookID, CustomerID, Rating, Comment, ReviewDate) VALUES
(1, 1, 5, 'A timeless classic that never gets old!', '2023-01-20'),
(2, 2, 4, 'Thought-provoking and still relevant today.', '2023-01-21'),
(3, 3, 5, 'Magical and enchanting story for all ages.', '2023-01-22'),
(4, 4, 4, 'Absolutely terrifying! Couldn''t put it down.', '2023-01-23');
