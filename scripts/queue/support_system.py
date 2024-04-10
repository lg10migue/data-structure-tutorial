from queue import Queue


class SupportTicketQueue(Queue):  # Inherits from our Queue class.

    # Method to add a new ticket to the queue.
    def process_tickets(self):

        # Dequeue all tickets in the queue and process them.
        while not self.is_empty():
            ticket = self.dequeue()

            # Simulate ticket processing.
            self.handle_ticket(ticket)

    # Method to process a ticket.
    def handle_ticket(self, ticket):
        print(f"Processing ticket #{ticket}")
        print("Ticket resolved.\n")


# Example usage.
support_queue = SupportTicketQueue()
support_queue.enqueue(1)
support_queue.enqueue(2)
support_queue.enqueue(3)
support_queue.process_tickets()
