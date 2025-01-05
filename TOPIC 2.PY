class Node:
    """
    Node for the Doubly Linked List.
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """
    Doubly Linked List for inventory tracking.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add_item(self, item):
        """Add an item to the inventory."""
        new_node = Node(item)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_item(self, item):
        """Remove an item from the inventory."""
        current = self.head
        while current:
            if current.data == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return f"Item '{item}' removed from inventory."
            current = current.next
        return f"Item '{item}' not found in inventory."

    def display_inventory(self):
        """Display all items in the inventory."""
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items

class CircularQueue:
    """
    Circular Queue for managing orders.
    """
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, order):
        """Add an order to the queue."""
        if (self.rear + 1) % self.size == self.front:
            return "Queue is full. Cannot add new order."
        elif self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = order
        return f"Order '{order}' added to the queue."

    def dequeue(self):
        """Remove an order from the queue."""
        if self.front == -1:
            return "Queue is empty. Cannot remove order."
        order = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return f"Order '{order}' removed from the queue."

    def display_orders(self):
        """Display all orders in the queue."""
        if self.front == -1:
            return []
        elif self.rear >= self.front:
            return self.queue[self.front : self.rear + 1]
        else:
            return self.queue[self.front :] + self.queue[: self.rear + 1]

# Example usage:
if __name__ == "__main__":
    # Inventory management using Doubly Linked List
    inventory = DoublyLinkedList()
    inventory.add_item("Paracetamol")
    inventory.add_item("Ibuprofen")
    inventory.add_item("Aspirin")
    print("Inventory:", inventory.display_inventory())
    print(inventory.remove_item("Ibuprofen"))
    print("Inventory after removal:", inventory.display_inventory())

    # Order management using Circular Queue
    order_queue = CircularQueue(3)
    print(order_queue.enqueue("Order1"))
    print(order_queue.enqueue("Order2"))
    print(order_queue.enqueue("Order3"))
    print(order_queue.enqueue("Order4"))  # Queue is full
    print("Orders in queue:", order_queue.display_orders())
    print(order_queue.dequeue())
    print("Orders after dequeuing:", order_queue.display_orders())
