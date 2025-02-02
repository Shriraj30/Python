import re
numPattern = r'^[0-9]+$'
namePattern = r"^[A-Za-z0-9\s]+$"
inventory = {}
categories = ("electronics", "clothing", "groceries", "furniture", "toys")
def isValidName(name):
    return re.fullmatch(namePattern, name) is not None
    
def isValidNum(n):
    return re.fullmatch(numPattern, n) is not None

def acceptProductName():
    name = input("Enter Product Name: ")
    if isValidName(name):   
        return name
    else:
        print("Invalid Product Name.")
        return None
        
def acceptProductID():
    prod_id = input("Enter Product ID: ")
    if isValidNum(prod_id):
        if prod_id in inventory:
            print("Product ID already exists. Please enter a different Product ID.")
            return None
        else:
            return prod_id
    else:
        print("Invalid Product ID.") 
        return None

def acceptPrice():
    price = input("Enter Product Price: ")
    price_pattern = r'^\d+(\.\d{1,2})?$'
    if re.match(price_pattern, price):
        return price
    else:
        print("Invalid Price. Please enter a valid number with up to two decimal places.")
        return None

def acceptQuantity():
    quantity = input("Enter Product Quantity: ")
    if quantity.isnumeric() and int(quantity) >= 0:
        return quantity
    else:
        print("Invalid Quantity.")
        return None    
        
def acceptCategory():
    category = input("Enter Product Category ('electronics', 'clothing', 'groceries', 'furniture', 'toys'): ")
    category = category.lower()
    if category in categories:
        return category
    else:
        print("Invalid Category.")
        return None
        
def insertProduct():
    prod_id = acceptProductID()
    if prod_id is None:
        return 0
    name = acceptProductName()
    if name is None:
        return 0
    price = acceptPrice()
    if price is None:
        return 0    
    quantity = acceptQuantity()
    if quantity is None:
        return 0
    category = acceptCategory()
    if category is None:
        return 0
    inventory[prod_id] = {"Name": name, "Price": price, "Quantity": quantity, "Category": category}
    return 1
    
def updateProductDetails():
    prod_id = input("Enter the product ID you want to update: ")
    if prod_id in inventory:
        print("1. Name\n2. Price\n3. Quantity\n4. Category\n5. Product ID")
        ch = input("Enter what you want to update from the above: ")
        if ch == "1":
            name = acceptProductName()
            if name:
                inventory[prod_id]["Name"] = name
                print("Name updated successfully")
        elif ch == "2":
            price = acceptPrice()
            if price:
                inventory[prod_id]["Price"] = price
                print("Price updated successfully")
        elif ch == "3":
            quantity = acceptQuantity()
            if quantity:
                inventory[prod_id]["Quantity"] = quantity
                print("Quantity updated successfully")
        elif ch == "4":
            category = acceptCategory()
            if category:
                inventory[prod_id]["Category"] = category
                print("Category updated successfully")
        elif ch == "5":
            new_prod_id = acceptProductID()
            if new_prod_id:
                inventory[new_prod_id] = inventory.pop(prod_id)
                print("Product ID updated successfully")
        else:
            print("Invalid choice, please try again")
    else:
        print("Product not found")

def retrieveProduct():
    prod_id = input("Enter the Product ID: ")
    if prod_id in inventory:
        product = inventory[prod_id]
        print("\nProduct ID: ", prod_id)
        print("Name: ", product["Name"])
        print("Price: ", product["Price"])
        print("Quantity: ", product["Quantity"])
        print("Category: ", product["Category"])
    else:
        print("Product not found")

def deleteProduct():
    prod_id = input("Enter the Product ID: ")
    if prod_id in inventory:
        del inventory[prod_id]
        print("Product deleted successfully")
    else:
        print("Product not found")

def showAllProducts():
    if len(inventory) == 0:
        print("No products in the inventory")
    else:
        print("Product ID | Name | Price | Quantity | Category")
        print("-" * 50)
        for prod_id, details in inventory.items():
            print(f"{prod_id:<10} | {details['Name']:<20} | {details['Price']:<6} | {details['Quantity']:<8} | {details['Category']:<12}")

while True:
    print("\n1. Add Product")
    print("2. Update Product")
    print("3. Retrieve Product")
    print("4. Delete Product")
    print("5. Show All Products")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        if insertProduct() == 1:
            print("Product details inserted successfully")
    elif choice == "2":
        updateProductDetails()
    elif choice == "3":
        retrieveProduct()
    elif choice == "4":
        deleteProduct()
    elif choice == "5":
        showAllProducts()
    elif choice == "6":
        break
    else:
        print("Invalid choice, please try again")
