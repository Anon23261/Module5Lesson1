# BookHaven Database Schema Documentation

## Overview
This document outlines the database schema for the BookHaven bookstore management system. The schema is designed to efficiently manage books, authors, customers, and transactions while maintaining data integrity and eliminating redundancy.

## Tables Structure

### Authors
- `AuthorID` (PK): Unique identifier for authors
- `FirstName`: Author's first name
- `LastName`: Author's last name
- `Biography`: Author's biographical information
- `Email`: Author's contact email
- Timestamps for record management

### Publishers
- `PublisherID` (PK): Unique identifier for publishers
- `Name`: Publisher's name
- `Address`: Publisher's address
- `Phone`: Contact phone number
- `Email`: Contact email
- Timestamps for record management

### Books
- `BookID` (PK): Unique identifier for books
- `ISBN`: International Standard Book Number (unique)
- `Title`: Book title
- `PublisherID` (FK): Reference to Publishers table
- `PublicationDate`: Date of publication
- `Price`: Book price
- `StockQuantity`: Current stock level
- `Genre`: Book genre
- `Description`: Book description
- Timestamps for record management

### BookAuthors (Junction Table)
- `BookID` (PK, FK): Reference to Books table
- `AuthorID` (PK, FK): Reference to Authors table
- Implements many-to-many relationship between Books and Authors

### Customers
- `CustomerID` (PK): Unique identifier for customers
- `FirstName`: Customer's first name
- `LastName`: Customer's last name
- `Email`: Customer's email (unique)
- `Phone`: Contact phone number
- `Address`: Customer's address
- `JoinDate`: Date customer joined
- Timestamps for record management

### Orders
- `OrderID` (PK): Unique identifier for orders
- `CustomerID` (FK): Reference to Customers table
- `OrderDate`: Date of order
- `TotalAmount`: Total order amount
- `Status`: Order status
- `ShippingAddress`: Delivery address
- Timestamps for record management

### OrderDetails
- `OrderID` (PK, FK): Reference to Orders table
- `BookID` (PK, FK): Reference to Books table
- `Quantity`: Number of books ordered
- `UnitPrice`: Price per book
- `Subtotal`: Total for line item
- Timestamps for record management

### Reviews
- `ReviewID` (PK): Unique identifier for reviews
- `BookID` (FK): Reference to Books table
- `CustomerID` (FK): Reference to Customers table
- `Rating`: Book rating (1-5)
- `Comment`: Review text
- `ReviewDate`: Date of review
- Timestamps for record management

## Relationships

1. Books ↔ Authors (Many-to-Many)
   - Implemented through BookAuthors junction table
   - One book can have multiple authors
   - One author can write multiple books

2. Books → Publishers (Many-to-One)
   - Each book is published by one publisher
   - One publisher can publish many books

3. Orders → Customers (Many-to-One)
   - Each order belongs to one customer
   - One customer can have many orders

4. Orders ↔ Books (Many-to-Many)
   - Implemented through OrderDetails table
   - One order can contain multiple books
   - One book can be in multiple orders

5. Reviews → Books (Many-to-One)
   - Each review is for one book
   - One book can have multiple reviews

6. Reviews → Customers (Many-to-One)
   - Each review is written by one customer
   - One customer can write multiple reviews

## Data Integrity Features

1. Primary and Foreign Key constraints ensure referential integrity
2. UNIQUE constraints on ISBN and email fields prevent duplicates
3. CHECK constraint on Reviews.Rating ensures valid ratings (1-5)
4. DEFAULT constraints for timestamps and status fields
5. NOT NULL constraints on essential fields

## Timestamps
All tables include:
- `CreatedDate`: Record creation timestamp
- `UpdatedDate`: Last modification timestamp
