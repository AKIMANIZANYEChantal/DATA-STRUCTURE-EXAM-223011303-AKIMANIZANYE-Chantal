# AVL Tree for managing orders

# Function to create a new node
def create_node(order_id, medicine_name, quantity, price):
    return {
        "order_id": order_id,
        "medicine_name": medicine_name,
        "quantity": quantity,
        "price": price,
        "left": None,
        "right": None,
        "height": 1,
    }

# Function to get the height of a node
def get_height(node):
    if node is None:
        return 0
    return node["height"]

# Function to calculate the balance factor of a node
def get_balance(node):
    if node is None:
        return 0
    return get_height(node["left"]) - get_height(node["right"])

# Right rotation
def rotate_right(y):
    x = y["left"]
    T = x["right"]

    # Perform rotation
    x["right"] = y
    y["left"] = T

    # Update heights
    y["height"] = 1 + max(get_height(y["left"]), get_height(y["right"]))
    x["height"] = 1 + max(get_height(x["left"]), get_height(x["right"]))

    return x

# Left rotation
def rotate_left(x):
    y = x["right"]
    T = y["left"]

    # Perform rotation
    y["left"] = x
    x["right"] = T

    # Update heights
    x["height"] = 1 + max(get_height(x["left"]), get_height(x["right"]))
    y["height"] = 1 + max(get_height(y["left"]), get_height(y["right"]))

    return y

# Function to insert a node into the AVL Tree
def insert(root, order_id, medicine_name, quantity, price):
    # Perform standard BST insert
    if root is None:
        return create_node(order_id, medicine_name, quantity, price)
    
    if order_id < root["order_id"]:
        root["left"] = insert(root["left"], order_id, medicine_name, quantity, price)
    elif order_id > root["order_id"]:
        root["right"] = insert(root["right"], order_id, medicine_name, quantity, price)
    else:
        return root  # Duplicate order IDs are not allowed

    # Update height
    root["height"] = 1 + max(get_height(root["left"]), get_height(root["right"]))

    # Get balance factor
    balance = get_balance(root)

    # Perform rotations if unbalanced
    if balance > 1 and order_id < root["left"]["order_id"]:
        return rotate_right(root)  # Left-left case
    if balance < -1 and order_id > root["right"]["order_id"]:
        return rotate_left(root)  # Right-right case
    if balance > 1 and order_id > root["left"]["order_id"]:
        root["left"] = rotate_left(root["left"])  # Left-right case
        return rotate_right(root)
    if balance < -1 and order_id < root["right"]["order_id"]:
        root["right"] = rotate_right(root["right"])  # Right-left case
        return rotate_left(root)

    return root

# Function to display orders in-order (sorted by order ID)
def display_orders(root):
    if root is not None:
        display_orders(root["left"])
        print(
            f"Order ID: {root['order_id']}, Medicine: {root['medicine_name']}, "
            f"Quantity: {root['quantity']}, Price: {root['price']}"
        )
        display_orders(root["right"])

# Function to count nodes in the AVL Tree
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root["left"]) + count_nodes(root["right"])

# Function to ensure a fixed number of orders are maintained
def maintain_fixed_orders(root, max_orders):
    while count_nodes(root) > max_orders:
        root = delete_minimum(root)
    return root

# Function to find the node with the minimum order ID
def find_minimum(root):
    while root["left"] is not None:
        root = root["left"]
    return root

# Function to delete the minimum node
def delete_minimum(root):
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_minimum(root["left"])
    root["height"] = 1 + max(get_height(root["left"]), get_height(root["right"]))
    return root

# Main functionality
if __name__ == "__main__":
    root = None
    max_orders = 5  # Maximum number of orders to manage

    # Insert orders
    orders = [
        (1, "Paracetamol", 10, 100),
        (2, "Ibuprofen", 5, 50),
        (3, "Amoxicillin", 8, 80),
        (4, "Cetrizine", 12, 60),
        (5, "Metformin", 20, 200),
        (6, "Aspirin", 15, 150),  # This will trigger deletion of the oldest order
    ]

    for order in orders:
        root = insert(root, *order)
        root = maintain_fixed_orders(root, max_orders)

    print("Current Orders:")
    display_orders(root)
