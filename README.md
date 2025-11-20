# Library-management-system
* A console-based Library Management System built with Python. This application allows administrators to manage the book inventory and students to   borrow or return books, with all data permanently stored in a JSON file.

# Project Structure
* *Main(lms).py*: The main entry point of the application. Handles user authentication and navigation.
* *Admin.py*: Contains all administrative functions (adding, viewing, and removing books).
* *Student.py*: Contains student functions (borrowing, returning, and viewing books).
* *file_handler.py*: A utility module that handles reading from and writing to the books.json file.
* *books.json*: The database file where all book information (code, name, status) is stored.

# Features
**Admin Features**
* *Add Book*: Add new books to the library inventory with a unique code and name.
* *View Books*: See a complete list of all books in the system.
* *Remove Book*: Delete a book from the inventory permanently.

# Student Features
* *Borrow Book*: Borrow a book if it is currently available.
* *Return Book*: Return a borrowed book to update its status to "available".
* *View All Books*: See the entire collection.
* *View Available Books*: Filter and view only the books that can be borrowed.
