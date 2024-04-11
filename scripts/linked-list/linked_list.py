class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_head(self, value):

        # Create a new node.
        new_node = LinkedList.Node(value)

        # Check if the head is empty.
        if self.head is None:

            # Set the head to the new node.
            self.head = new_node

            # Set the tail to the new node.
            self.tail = new_node
        else:

            # Set the new node's pointer to the current head.
            new_node.next = self.head

            # Set the current head's previous pointer to the new node.
            self.head.prev = new_node

            # Set the head to the new node.
            self.head = new_node

        # Increment the length.
        self.length += 1

    def insert_tail(self, value):

        # Create a new node.
        new_node = LinkedList.Node(value)

        # Check if the head is empty.
        if self.head is None:

            # Set the head to the new node.
            self.head = new_node

            # Set the tail to the new node.
            self.tail = new_node
        else:

            # Set the current tail's next pointer to the new node.
            self.tail.next = new_node

            # Set the new node's previous pointer to the current tail.
            new_node.prev = self.tail

            # Set the tail to the new node.
            self.tail = new_node

        # Increment the length.
        self.length += 1

    def insert_after(self, value, new_value):

        # Get the current head node.
        curr = self.head

        # Iterate through the linked list.
        while curr is not None:

            # Check if the current node's data is equal to the value.
            if curr.data == value:

                # Check if the current node is the tail.
                if curr == self.tail:

                    # Insert the new value at the tail.
                    self.insert_tail(new_value)
                else:

                    # Create a new node.
                    new_node = LinkedList.Node(new_value)

                    # Set the new node's previous pointer to the current node.
                    new_node.prev = curr

                    # Set the new node's next pointer to the current node's next node.
                    new_node.next = curr.next

                    # Set the current node's next node's previous pointer to the new node.
                    curr.next.prev = new_node

                    # Set the current node's next pointer to the new node.
                    curr.next = new_node

                return

            # Move to the next node.
            curr = curr.next

        # Increment the length.
        self.length += 1

    def remove(self, value):

        # Get the current head node.
        current = self.head

        # Iterate through the linked list.
        while current is not None:

            # Check if the current node's data is equal to the value.
            if current.data == value:

                # Check if the current node is the head.
                if current == self.head:

                    # Remove the head.
                    self.remove_head()

                # Check if the current node is the tail.
                elif current == self.tail:

                    # Remove the tail.
                    self.remove_tail()
                else:

                    # Set the current node's previous node's next pointer to the current node's next node.
                    current.prev.next = current.next

                    # Set the current node's next node's previous pointer to the current node's previous node.
                    current.next.prev = current.prev
                return

            # Move to the next node.
            current = current.next

        # Decrement the length.
        self.length -= 1

    def remove_head(self):

        # Check if the head is the tail.
        if self.head == self.tail:

            # Set the head to None.
            self.head = None

            # Set the tail to None.
            self.tail = None

        # Check if the head is not None.
        elif self.head is not None:

            # Set the head's next node's previous pointer to None.
            self.head.next.prev = None

            # Set the head to the head's next node.
            self.head = self.head.next

        # Decrement the length.
        self.length -= 1

    def remove_tail(self):

        # Check if the head is the tail.
        if self.head == self.tail:

            # Set the head to None.
            self.head = None

            # Set the tail to None.
            self.tail = None

        # Check if the head is not None.
        elif self.head is not None:

            # Set the tail's previous node's next pointer to None.
            self.tail.prev.next = None

            # Set the tail to the tail's previous node.
            self.tail = self.tail.prev

        # Decrement the length.
        self.length -= 1

    def size(self):
        return self.length

    def is_empty(self):
        return self.size() == 0

    def __str__(self):

        # Create a list to store the linked list's data.
        data = []

        # Get the current head node.
        current = self.head

        # Iterate through the linked list.
        while current is not None:

            # Append the current node's data to the list.
            data.append(current.data)

            # Move to the next node.
            current = current.next

        # Return the linked list's data.
        return f"LinkedList: {data}"
