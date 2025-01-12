import datetime
import re  

class Product:
    def __init__(self, code, name, price, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls):
        code = input("Enter product code (or 'done' to finish): ")
        if code.lower() == 'done':
            return None  
        
        while True:
            name = input("Enter product name: ")
            if re.match("^[A-Za-z]+$", name):  
                break
            else:
                print("Invalid name! Please enter only letters and spaces.")

        price_input = input("Enter product price: ")
        price = float(price_input)  
        quantity_input = input("Enter product quantity: ")
        quantity = int(quantity_input)  

        return cls(code, name, price, quantity)

    def get_product_data(self):
        return f"{self.code}: {self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"

def write_to_file(products, filename):
    with open(filename, 'w') as file:
        for product in products:
            file.write(product.get_product_data() + "\n")
    return filename  

def main():
    current_date = datetime.datetime.now().strftime("%d_%m_%Y")
    filename = f"Product_{current_date}.txt"

    products = []

    while True:
        product = Product.create_product()
        if product is None:  
            break
        products.append(product)

    written_file = write_to_file(products, filename)

    return products, written_file

products, file_written = main()

print("\nProducts entered:")
for product in products:
    print(product.get_product_data())

print(f"\nData has been written to {file_written}.")
