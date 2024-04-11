from linked_list import LinkedList


class ReadingTracker(LinkedList):
    def __init__(self):
        super().__init__()

    def add_book(self, title):
        self.insert_tail(title)

    def complete_book(self):
        if self.head is not None:
            print(f"Reading {self.head.data}")
            self.remove_head()
        else:
            print("No books in the reading list.")

    def show_next_book(self):
        if self.head is not None:
            print(f"Next book to read: {self.head.data}")
        else:
            print("No books in the reading list.")

    def show_reading_list(self):
        books = []
        curr = self.head
        while curr is not None:
            books.append(curr.data)
            curr = curr.next
        return " -> ".join(books)


# Simulation of reading books.
reading_tracker = ReadingTracker()

# Add books to the reading list.
reading_tracker.add_book("Pride and Prejudice")
reading_tracker.add_book("The Great Gatsby")
reading_tracker.add_book("1984")

# Iterate through the reading list.
while reading_tracker.size() > 0:
    # Show the reading list.
    print(f"\nReading List: {reading_tracker.show_reading_list()}")

    # Show the next book to read.
    reading_tracker.show_next_book()

    # Mark the current book as read.
    reading_tracker.complete_book()

# Reading list is empty.
reading_tracker.show_next_book()
