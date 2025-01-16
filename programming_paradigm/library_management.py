class Book:
    def __init__(self, title, author):
        """Initialize the book with a title, author, and a checked out status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Books are available by default

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned."""
        self._is_checked_out = False

    def is_checked_out(self):
        """Return the availability status of the book."""
        return self._is_checked_out

class Library:
    def __init__(self):
        """Initialize an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return True  # Successfully checked out
        return False  # Book not found or already checked out

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return True  # Successfully returned
        return False  # Book not found or not checked out

    def list_available_books(self):
        """Print all available books (not checked out)."""
        available_books = [book for book in self._books if not book.is_checked_out()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
