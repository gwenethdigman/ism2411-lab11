
# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Gweneth Digman


# Question 1:
# I would use .get() when I am not sure if a piece of
# information is available, for example, a customer's email or phone number.
# I would use bracket notation instead, when I know the information should be
# there. My rule of thumb is to use .get() when information might be
# missing so my code does not crash.

# Question 2:
# Exercise 8 reminds me of using a PivotTable in Excel because both
# allow you to organize data into categories and calculate totals.
# Python might be more useful for larger datasets because it can
# automatically process a lot of information without having to
# manually update a spreadsheet.


# EXERCISE 1: One Customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1500
}
#let's print one by one 
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)


# EXERCISE 2: Update and Add
# Add a phone number
customer["phone"] = "555-123-4567"
print(customer)

# Update the customer's tier
customer["tier"] = "platinum"
print(customer)

# Delete the email
del customer["email"]
print(customer)


# EXERCISE 3: Safe Lookup

print("\nEXERCISE 3")

# .get() returns a default if the key is missing
print(customer.get("email", "no email on file"))

# Bracket notation raises a KeyError if the key is missing
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# EXERCISE 4: Iterate
# .items() gives both the key and its value
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives the keys
for key in customer:
    print(key)


# EXERCISE 5: Lookup Table

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

# Find the customer's discount
tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

# Calculate the price after the discount
original_price = 200
final_price = original_price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount * 100}%")
print(f"Final price: ${final_price:.2f}")


# EXERCISE 6: List of Dictionaries

customers = [
    customer,
    {
        "name": "Bob",
        "tier": "silver",
        "ytd_spend": 800
    },
    {
        "name": "Charlie",
        "tier": "bronze",
        "ytd_spend": 300
    }
]

# Calculate the discount on a $300 purchase
for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(f"{name}: {tier} - ${discount_amount:.2f} discount")


# EXERCISE 7: Nested Catalog

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

# Check which products have low stock
for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")


# EXERCISE 8: Sales by Region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

region_sales = {}

# Add up the sales for each region
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    region_sales[region] = region_sales.get(region, 0) + amount

# Print the regions in alphabetical order
for region in sorted(region_sales):
    print(f"{region}: ${region_sales[region]}")
