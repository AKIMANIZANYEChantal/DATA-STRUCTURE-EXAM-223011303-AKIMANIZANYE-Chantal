# Binary tree for pharmacy management system

# Function to create a new node
def create_node(name, quantity, price):
    return {"name": name, "quantity": quantity, "price": price, "left": None, "right": None}

# Function to insert a node in the binary tree
def insert(root, name, quantity, price):
    if root is None:
        return create_node(name, quantity, price)
    
    if name < root["name"]:
        root["left"] = insert(root["left"], name, quantity, price)
    elif name > root["name"]:
        root["right"] = insert(root["right"], name, quantity, price)
    else:
        # If the medicine already exists, update the quantity
        root["quantity"] += quantity
    
    return root

# Function to search for a medicine in the binary tree
def search(root, name):
    if root is None or root["name"] == name:
        return root
    
    if name < root["name"]:
        return search(root["left"], name)
    
    return search(root["right"], name)

# Function to update the quantity of a medicine
def update_quantity(root, name, quantity):
    node = search(root, name)
    if node:
        node["quantity"] += quantity
    else:
        print(f"Medicine '{name}' not found.")

# Function to delete a node
def delete(root, name):
    if root is None:
        return root
    
    if name < root["name"]:
        root["left"] = delete(root["left"], name)
    elif name > root["name"]:
        root["right"] = delete(root["right"], name)
    else:
        if root["left"] is None:
            return root["right"]
        elif root["right"] is None:
            return root["left"]
        
        # Find the inorder successor (smallest in the right subtree)
        successor = root["right"]
        while successor["left"] is not None:
            successor = successor["left"]
        
        root["name"], root["quantity"], root["price"] = (
            successor["name"],
            successor["quantity"],
            successor["price"],
        )
        root["right"] = delete(root["right"], successor["name"])
    
    return root

# Function to display the inventory in-order (sorted by name)
def display_inventory(root):
    if root is not None:
        display_inventory(root["left"])
        print(
            f"Medicine: {root['name']}, Quantity: {root['quantity']}, Price: {root['price']}"
        )
        display_inventory(root["right"])

# Main functionality
if __name__ == "__main__":
    root = None
    root = insert(root, "Paracetamol", 50, 10.5)
    root = insert(root, "Ibuprofen", 30, 15.0)
    root = insert(root, "Amoxicillin", 20, 12.0)
    root = insert(root, "Cetrizine", 40, 8.0)

    print("Initial Inventory:")
    display_inventory(root)
    
    print("\nUpdating quantity of Paracetamol:")
    update_quantity(root, "Paracetamol", 20)
    display_inventory(root)
    
    print("\nDeleting Ibuprofen:")
    root = delete(root, "Ibuprofen")
    display_inventory(root)
