def calculate_gst_amount(unit_price, gst_percentage, quantity):
    return (unit_price * gst_percentage / 100) * quantity

def calculate_discounted_price(unit_price, quantity):
    if unit_price >= 500:
        return unit_price * 0.95 * quantity
    else:
        return unit_price * quantity

# Define the basket
basket = [
    {"product_name": "Leather wallet", "unit_price": 1100, "gst_percentage": 18, "quantity": 1},
    {"product_name": "Umbrella", "unit_price": 900, "gst_percentage": 12, "quantity": 4},
    {"product_name": "Cigarette", "unit_price": 200, "gst_percentage": 28, "quantity": 3},
    {"product_name": "Honey", "unit_price": 100, "gst_percentage": 0, "quantity": 2}
]

# Display details of each product
for product in basket:
    gst_amount = calculate_gst_amount(product["unit_price"], product["gst_percentage"], product["quantity"])
    discounted_price = calculate_discounted_price(product["unit_price"], product["quantity"])
    print(f"Product: {product['product_name']}, GST Amount: {gst_amount}, Discounted Price: {discounted_price}")

# Identify the product with the maximum discounted price
max_discounted_product = max(basket, key=lambda x: calculate_discounted_price(x["unit_price"], x["quantity"]))
print("Product with maximum discounted price:", max_discounted_product["product_name"])

# Calculate and display the average GST percentage for all products
average_gst_percentage = sum(product["gst_percentage"] for product in basket) / len(basket)
print("Average GST Percentage for all products:", average_gst_percentage)

# Identify the product for which we paid the maximum GST amount
max_gst_product = max(basket, key=lambda x: calculate_gst_amount(x["unit_price"], x["gst_percentage"], x["quantity"]))
print("Product with maximum GST amount:", max_gst_product["product_name"])

# Calculate the total amount to be paid to the shopkeeper
total_amount = sum(calculate_discounted_price(item["unit_price"], item["quantity"]) for item in basket)
print("Total amount to be paid to the shopkeeper:", total_amount)
