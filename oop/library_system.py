class Book:
    def __init__(self, title, author):
        """Initialize the base Book class."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook, calling the parent constructor."""
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        """Return a string representation specific to EBooks."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook, calling the parent constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation specific to PrintBooks."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)


from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
