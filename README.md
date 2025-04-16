Library Management System API

#Overview
This project is a Library Management System built with Django and Django REST Framework (DRF). It allows users to manage library resources efficiently. The system enables functionalities such as user authentication, book management, and transaction tracking for borrowing and returning books. The application follows a role-based access control system, ensuring that only authorized users can perform specific actions like managing books and users.

#Features
User Management
- Users can register and log in to access the system.
- Role-based permissions

Book Management
- Add, edit, and delete books in the library.
- Manage available copies of books.
- View a list of all books or details of a specific book.

Transaction Management
- Borrow and return books with a streamlined transaction system.
- Automatically updates the availability of books.

API ENDPOINTS
User Endpoints
POST /register/ - Register a new user.
POST /login/- Log in an existing user.
POST /logout/- Log out the current user.

Book Endpoints
GET /api/books/ - Retrieve a list of all books.
POST /api/books/ - Add a new book (Admins and Superusers only).
PUT /api/books/<id>/ - Update book details (Admins and Superusers only).
DELETE /api/books/<id>/ - Delete a book (Admins and Superusers only).

Transaction Endpoints
GET /my_books/ - View books currently borrowed by the logged-in user.
POST /borrow/ - Borrow a book.
POST /return/ - Return a borrowed book.

Project Setup

Prerequisites
Python 3.10 or later
Django 4.x
Django REST Framework
pip (Python package installer)
A text editor/IDE like VS Code

