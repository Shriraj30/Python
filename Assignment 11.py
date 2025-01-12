class InvalidQuantityError(Exception):
    def __init__(self, message):
        self.message = message

class ExceedingMaximumOrderError(Exception):
    def __init__(self, message):
        self.message = message

class InvalidProductCodeError(Exception):
    def __init__(self, message):
        self.message = message

class Product:
    max_order_levels = {
        "P1": 100,
        "P2": 200,
        "P3": 150,
        "P4": 300
    }

    def __init__(self, product_code, qty):
        self.product_code = product_code
        self.qty = qty

    def validate(self):
        if self.product_code not in Product.max_order_levels:
            raise InvalidProductCodeError(f"Invalid Product Code: {self.product_code}")

        if self.qty < 0:
            raise InvalidQuantityError("Quantity must not be negative")

        max_qty = Product.max_order_levels[self.product_code]
        if self.qty > max_qty:
            raise ExceedingMaximumOrderError(f"Quantity exceeds maximum order level of {max_qty} for product {self.product_code}")

try:
    product_code = input("Enter product code: ")
    qty = int(input("Enter quantity: "))

    product = Product(product_code, qty)
    
    product.validate()

    print("Product details are valid!")

except InvalidProductCodeError as e:
    print(e.message)

except InvalidQuantityError as e:
    print(e.message)

except ExceedingMaximumOrderError as e:
    print(e.message)

except ValueError:
    print("Invalid input! Quantity must be an integer.")
