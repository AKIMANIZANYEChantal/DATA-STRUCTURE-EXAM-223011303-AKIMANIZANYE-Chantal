# Insertion Sort for sorting inventory based on priority

# Function to sort inventory using insertion sort
def insertion_sort(inventory, key):
    """
    Sort the inventory list in ascending order based on the given key.

    Parameters:
    - inventory: List of dictionaries representing inventory items.
    - key: The key in the dictionary to sort by (e.g., 'quantity', 'price').

    Returns:
    - Sorted list of inventory items.
    """
    for i in range(1, len(inventory)):
        current_item = inventory[i]
        j = i - 1

        # Move elements that are greater than current_item[key] one position ahead
        while j >= 0 and inventory[j][key] > current_item[key]:
            inventory[j + 1] = inventory[j]
            j -= 1
        
        inventory[j + 1] = current_item

    return inventory

# Function to display the inventory
def display_inventory(inventory):
    print("\nSorted Inventory:")
    for item in inventory:
        print(
            f"Medicine: {item['name']}, Quantity: {item['quantity']}, "
            f"Price: {item['price']:.2f}, Priority: {item['priority']}"
        )

# Main functionality
if __name__ == "__main__":
    # Example inventory data
    inventory = [
        {"name": "Paracetamol", "quantity": 50, "price": 10.5, "priority": 3},
        {"name": "Ibuprofen", "quantity": 30, "price": 15.0, "priority": 1},
        {"name": "Amoxicillin", "quantity": 20, "price": 12.0, "priority": 2},
        {"name": "Cetrizine", "quantity": 40, "price": 8.0, "priority": 4},
    ]

    print("Original Inventory:")
    for item in inventory:
        print(
            f"Medicine: {item['name']}, Quantity: {item['quantity']}, "
            f"Price: {item['price']:.2f}, Priority: {item['priority']}"
        )

    # Sort inventory based on 'priority'
    sorted_inventory = insertion_sort(inventory, key="priority")

    # Display sorted inventory
    display_inventory(sorted_inventory)
