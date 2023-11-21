def calculate_gst_amount(unit_price, gst_percentage, quantity):
    return (unit_price * gst_percentage / 100) * quantity

def calculate_discounted_price(unit_price, quantity):
    if unit_price >= 500:
        return unit_price * 0.95 * quantity
    else:
        return unit_price * quantity

def display_basket(basket):
    for item in basket:
        print(f"Product: {item['product_name']}, Quantity: {item['quantity']}")

# Define the basket
basket = [
    {"product_name": "Leather wallet", "unit_price": 1100, "gst_percentage": 18, "quantity": 1},
    {"product_name": "Umbrella", "unit_price": 900, "gst_percentage": 12, "quantity": 4},
    {"product_name": "Cigarette", "unit_price": 200, "gst_percentage": 28, "quantity": 3},
    {"product_name": "Honey", "unit_price": 100, "gst_percentage": 0, "quantity": 2}
]

# Display the initial basket
print("Initial Basket:")
display_basket(basket)

# 1. Identify the product for which we paid the maximum GST amount
max_gst_product = max(basket, key=lambda x: calculate_gst_amount(x["unit_price"], x["gst_percentage"], x["quantity"]))
print("\nProduct with maximum GST amount:", max_gst_product["product_name"])

# 2. Calculate the total amount to be paid to the shopkeeper
total_amount = sum(calculate_discounted_price(item["unit_price"], item["quantity"]) for item in basket)
print("Total amount to be paid to the shopkeeper:", total_amount)

# 3. Add a new product to the basket
new_product = {"product_name": "New Item", "unit_price": 300, "gst_percentage": 15, "quantity": 2}
basket.append(new_product)

# Display the updated basket
print("\nBasket after adding a new product:")
display_basket(basket)

# 4. Update the quantity of an existing product
updated_product_name = "Umbrella"
updated_quantity = 6
for item in basket:
    if item["product_name"] == updated_product_name:
        item["quantity"] = updated_quantity

# Display the basket after updating the quantity
print("\nBasket after updating the quantity of an existing product:")
display_basket(basket)

# 5. Remove a product from the basket
product_to_remove = "Cigarette"
basket = [item for item in basket if item["product_name"] != product_to_remove]

# Display the basket after removing a product
print("\nBasket after removing a product:")
display_basket(basket)

# 6. Calculate the total amount after all activities
total_amount = sum(calculate_discounted_price(item["unit_price"], item["quantity"]) for item in basket)
print("\nTotal amount to be paid to the shopkeeper after all activities:", total_amount)
