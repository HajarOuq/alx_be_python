class Book:
    """Represents a book with a title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self._books = []  # Private list of Book instances

    def add_book(self, book):
        """Add a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        # (Optional) You could print a message if book not found

    def return_book(self, title):
        """Return a book by title to make it available again."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        # (Optional) You could print a message if book not found

    def list_available_books(self):
        """Print all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
