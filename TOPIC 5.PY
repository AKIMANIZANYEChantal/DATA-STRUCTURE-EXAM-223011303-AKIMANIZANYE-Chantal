# Pharmacy inventory management using arrays

# Initialize the inventory
inventory = []

# Function to add a medicine to the inventory
def add_medicine(inventory, name, quantity, price):
    # Check if the medicine already exists
    for item in inventory:
        if item["name"] == name:
            item["quantity"] += quantity  # Update the quantity if found
            print(f"Updated {name}'s quantity to {item['quantity']}.")
            return inventory
    
    # Add a new medicine if not found
    inventory.append({"name": name, "quantity": quantity, "price": price})
    print(f"Added new medicine: {name}.")
    return inventory

# Function to update the quantity of a medicine
def update_quantity(inventory, name, quantity):
    for item in inventory:
        if item["name"] == name:
            item["quantity"] += quantity
            print(f"Updated {name}'s quantity to {item['quantity']}.")
            return inventory
    
    print(f"Medicine '{name}' not found in inventory.")
    return inventory

# Function to remove a medicine from the inventory
def remove_medicine(inventory, name):
    for i, item in enumerate(inventory):
        if item["name"] == name:
            del inventory[i]
            print(f"Removed {name} from inventory.")
            return inventory
    
    print(f"Medicine '{name}' not found in inventory.")
    return inventory

# Function to display the inventory
def display_inventory(inventory):
    print("\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item in inventory:
            print(
                f"Medicine: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']:.2f}"
            )

# Main functionality
if __name__ == "__main__":
    # Add medicines
    inventory = add_medicine(inventory, "Paracetamol", 50, 10.5)
    inventory = add_medicine(inventory, "Ibuprofen", 30, 15.0)
    inventory = add_medicine(inventory, "Amoxicillin", 20, 12.0)
    
    # Display inventory
    display_inventory(inventory)
    
    # Update quantities
    inventory = update_quantity(inventory, "Paracetamol", 20)
    inventory = update_quantity(inventory, "Cetrizine", 10)  # Not found
    
    # Remove a medicine
    inventory = remove_medicine(inventory, "Ibuprofen")
    
    # Display updated inventory
    display_inventory(inventory)



