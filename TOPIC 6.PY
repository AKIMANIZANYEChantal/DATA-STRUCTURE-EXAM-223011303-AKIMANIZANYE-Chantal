

### Implementation


# Tree structure for hierarchical data in inventory tracking

# Function to create a tree node
def create_node(name, data=None):
    return {"name": name, "data": data, "children": []}

# Function to add a child node
def add_child(parent, child_name, child_data=None):
    child_node = create_node(child_name, child_data)
    parent["children"].append(child_node)
    return child_node

# Function to display the tree
def display_tree(node, level=0):
    indent = "  " * level
    if node["data"]:
        print(f"{indent}- {node['name']} (Data: {node['data']})")
    else:
        print(f"{indent}- {node['name']}")
    for child in node["children"]:
        display_tree(child, level + 1)

# Function to find a node by name
def find_node(root, name):
    if root["name"] == name:
        return root
    for child in root["children"]:
        result = find_node(child, name)
        if result:
            return result
    return None

# Example: Pharmacy inventory management using a tree
if __name__ == "__main__":
    # Create the root node
    inventory = create_node("Pharmacy Inventory")

    # Add categories
    tablets = add_child(inventory, "Tablets")
    syrups = add_child(inventory, "Syrups")
    injections = add_child(inventory, "Injections")

    # Add subcategories and medicines
    painkillers = add_child(tablets, "Painkillers")
    antibiotics = add_child(tablets, "Antibiotics")

    add_child(painkillers, "Paracetamol", {"quantity": 100, "price": 10.5})
    add_child(painkillers, "Ibuprofen", {"quantity": 50, "price": 15.0})
    add_child(antibiotics, "Amoxicillin", {"quantity": 200, "price": 12.0})

    add_child(syrups, "Cough Syrup", {"quantity": 75, "price": 20.0})
    add_child(syrups, "Antacid Syrup", {"quantity": 30, "price": 25.0})

    add_child(injections, "Insulin", {"quantity": 150, "price": 100.0})

    # Display the inventory tree
    print("Inventory Hierarchy:")
    display_tree(inventory)

    # Find a specific node
    search_name = "Painkillers"
    node = find_node(inventory, search_name)
    if node:
        print(f"\nDetails of '{search_name}':")
        display_tree(node)
    else:
        print(f"'{search_name}' not found in inventory.")
