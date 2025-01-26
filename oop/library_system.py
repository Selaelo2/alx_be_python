# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Calling the constructor of the base class
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()}, File Size: {self.file_size}MB"

# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Calling the constructor of the base class
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()}, Page Count: {self.page_count}"

# Composition - Library
class Library:
    def __init__(self):
        self.books = []  # A list to store instances of Book, EBook, or PrintBook

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)  # Adds a book of any type (Book, EBook, PrintBook)
        else:
            print("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            print(book)
