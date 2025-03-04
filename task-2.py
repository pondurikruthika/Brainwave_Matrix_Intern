import json

inventory_file = "inventory.json"

def load_inventory():
    try:
        with open(inventory_file, "r") as file:
            inventory = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        inventory = {}
    return inventory


def save_inventory(inventory):
    with open(inventory_file, "w") as file:
        json.dump(inventory, file, indent=4)


def add_product(inventory):
    product_id = input("Enter Product ID: ")
    if product_id in inventory:
        print(f"Product with ID {product_id} already exists.")
        return
    
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    
    inventory[product_id] = {"name": name, "quantity": quantity, "price": price}
    save_inventory(inventory)
    print(f"Product {name} added successfully.")


def edit_product(inventory):
    product_id = input("Enter Product ID to edit: ")
    
    if product_id not in inventory:
        print(f"Product with ID {product_id} not found.")
        return
    
    name = input(f"Enter new Name (current: {inventory[product_id]['name']}): ")
    quantity = int(input(f"Enter new Quantity (current: {inventory[product_id]['quantity']}): "))
    price = float(input(f"Enter new Price (current: {inventory[product_id]['price']}): "))
    
    inventory[product_id] = {"name": name, "quantity": quantity, "price": price}
    save_inventory(inventory)
    print(f"Product with ID {product_id} updated successfully.")


def delete_product(inventory):
    product_id = input("Enter Product ID to delete: ")
    
    if product_id not in inventory:
        print(f"Product with ID {product_id} not found.")
        return
    
    del inventory[product_id]
    save_inventory(inventory)
    print(f"Product with ID {product_id} deleted successfully.")


def display_inventory(inventory):
    if not inventory:
        print("No products in inventory.")
        return
    
    print("\nInventory:")
    for product_id, details in inventory.items():
        print(f"ID: {product_id} | Name: {details['name']} | Quantity: {details['quantity']} | Price: ${details['price']:.2f}")


def low_stock_alert(inventory, threshold=5):
    low_stock = {id: details for id, details in inventory.items() if details["quantity"] <= threshold}
    
    if not low_stock:
        print("No low-stock products.")
    else:
        print("\nLow-Stock Products:")
        for product_id, details in low_stock.items():
            print(f"ID: {product_id} | Name: {details['name']} | Quantity: {details['quantity']}")


def sales_summary(inventory):
    total_sales = 0
    print("\nEnter sales details (enter 'done' to finish):")
    
    while True:
        product_id = input("Enter Product ID: ")
        if product_id.lower() == "done":
            break
        if product_id not in inventory:
            print(f"Product with ID {product_id} not found.")
            continue
        
        quantity_sold = int(input(f"Enter quantity sold for {inventory[product_id]['name']}: "))
        if quantity_sold > inventory[product_id]["quantity"]:
            print("Not enough stock to complete this sale.")
            continue
        
        inventory[product_id]["quantity"] -= quantity_sold
        sale_value = quantity_sold * inventory[product_id]["price"]
        total_sales += sale_value
        print(f"Sale of {quantity_sold} {inventory[product_id]['name']} completed.")
    
    save_inventory(inventory)
    print(f"\nTotal Sales: ${total_sales:.2f}")


def menu():
    inventory = load_inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Edit Product")
        print("3. Delete Product")
        print("4. Display Inventory")
        print("5. Low-Stock Alert")
        print("6. Sales Summary")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            edit_product(inventory)
        elif choice == "3":
            delete_product(inventory)
        elif choice == "4":
            display_inventory(inventory)
        elif choice == "5":
            low_stock_alert(inventory)
        elif choice == "6":
            sales_summary(inventory)
        elif choice == "7":
            print("Exiting the Inventory Management System.")
            break
        else:
            print("Invalid option. Please choose between 1 and 7.")

if __name__ == "__main__":
    menu()
