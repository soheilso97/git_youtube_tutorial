# Smart Shop - corrected and polished

p_i = []
subtotal = 0.0

# Customer name
customer_name = input("Customer name: ").strip()

# Loyalty status (accept number or name)
loyalty_input = input("""Choose loyalty status (type number or name):
    1. Platinum
    2. Gold
    3. Silver
Your answer: """).strip().lower()

# Normalize loyalty input
if loyalty_input in ("1", "platinum", "p"):
    loyalty_status = "Platinum"
elif loyalty_input in ("2", "gold", "g"):
    loyalty_status = "Gold"
elif loyalty_input in ("3", "silver", "s"):
    loyalty_status = "Silver"
else:
    loyalty_status = "None"

if loyalty_status == "None":
    print("Invalid loyalty input — no loyalty discount will be applied.")
else:
    print(f"Loyalty status is {loyalty_status}")

# Number of purchased items
Purchased_items = int(input("Number of items: ").strip())

# Read items
for idx in range(Purchased_items):
    Name = input(f"Item No {idx + 1} name: ").strip()
    Unit_price = float(input("Unit price: ").strip())
    qty = int(input("Quantity: ").strip())
    p_i.append([Name, Unit_price, qty])

# Calculate subtotal
for items in p_i:
    item_total = items[1] * items[2]
    subtotal += item_total  # use of +=

print(f"\nsubtotal : {subtotal:,.2f} $")

# Loyalty discount
if loyalty_status == "Silver":
    loyal_discount = subtotal * 0.05
elif loyalty_status == "Gold":
    loyal_discount = subtotal * 0.10
elif loyalty_status == "Platinum":
    loyal_discount = subtotal * 0.15
else:
    loyal_discount = 0.0

# Price-based extra discount (check larger threshold first)
if subtotal >= 5000:
    price_discount = subtotal * 0.07
elif subtotal >= 3000:
    price_discount = subtotal * 0.03
else:
    price_discount = 0.0

# Bulk buyer bonus (1% if purchased_items >= 10)
if Purchased_items >= 10:
    print("Bulk buyer bonus applied!")
    bulk_buyer_bonus = subtotal * 0.01
else:
    bulk_buyer_bonus = 0.0

# Total discounts and totals
total_discount = loyal_discount + price_discount + bulk_buyer_bonus
total_no_vat = subtotal - total_discount

# VAT = 9% ON the amount AFTER discounts
vat = total_no_vat * 0.09
payable = total_no_vat + vat

# Receipt print with formatting
print("\n" + "=" * 50)
print("\t\tShopping Receipt")
print("=" * 50)
print(f"Customer name:       {customer_name}")
print(f"Loyalty Status:      {loyalty_status}")
print("-" * 50)
print(f"Purchased items:     {Purchased_items}")
print(f"Total purchase:      {subtotal:,.2f} $")
print("-" * 50)
print("\tDiscounts:")
print(f"Loyalty discount:    {loyal_discount:,.2f} $")
print(f"Price discount:      {price_discount:,.2f} $")
print(f"Bulk buyer bonus:    {bulk_buyer_bonus:,.2f} $")
print(f"Total discount:      {total_discount:,.2f} $")
print("-" * 50)
print("\tVAT and Final:")
print(f"Total before VAT:    {total_no_vat:,.2f} $")
print(f"VAT (9%):            {vat:,.2f} $")
print(f"Payable:             {payable:,.2f} $")
print("=" * 50)
print("\tThank you, see you soon")
print("=" * 50)

# Print type()s for notes (as requested)
print("\n# Types (for notes):")
print(f"type(customer_name) = {type(customer_name)}")
print(f"type(Purchased_items) = {type(Purchased_items)}")
print(f"type(subtotal) = {type(subtotal)}")
