from queue import Queue


class CafeteriaOrderQueue(Queue):
    # Method to place an order in the queue.
    def place_order(self, order_id):
        self.enqueue(order_id)

    # Method to serve an order from the queue.
    def serve_order(self):
        if not self.is_empty():
            order = self.dequeue()
            print(f"Order #{order} served.")
        else:
            print("\nNo more orders to serve.")

    # Method to check the next order to serve.
    def next_order(self):
        if not self.is_empty():
            print(f"\nNext order to serve: {self.peek()}.")
        else:
            print("\nNo more orders to serve.")


# Simulation of order placement and serving.
cafeteria_queue = CafeteriaOrderQueue()

# Place orders.
cafeteria_queue.place_order(1)
cafeteria_queue.place_order(2)

# Serve orders and check the next order.
cafeteria_queue.next_order()
cafeteria_queue.serve_order()
cafeteria_queue.next_order()
cafeteria_queue.serve_order()
cafeteria_queue.serve_order()
