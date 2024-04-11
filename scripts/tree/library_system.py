from tree import BinarySearchTree


class LibrarySystem(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def add_book(self, book_id):
        self.insert(book_id)
        print(f"Book {book_id} added to the system.")

    def search_book(self, book_id):
        if self.search(book_id):
            print(f"Book {book_id} is available in the library.")
        else:
            print(f"Book {book_id} is not found in the library.")

    def remove_book(self, book_id):
        self.delete(book_id)
        print(f"Book {book_id} has been removed from the system.")


# Example usage.
library = LibrarySystem()
library.add_book(100)
library.add_book(50)
library.add_book(150)
library.search_book(50)
library.remove_book(50)
library.search_book(50)
