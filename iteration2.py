NJ_SALES_TAX = 0.06625
LINE_SEP = "=" * 30

def get_shopping_cart() -> dict[str, float]:
    count = int(input("Enter the amount of items you want to buy: "))
    cart = {}
    for i in range(count):
        item = input(f"Enter the name of item {i + 1}: ")
        price = float(input(f"Enter the price of item {i + 1}: "))
        cart[item] = price
    return cart

def calculate_sales_tax(price, tax_rate):
    return price * tax_rate

def calculate_total(subtotal, tax_rate):
    total = 0.0
    sales_tax = calculate_sales_tax(subtotal, tax_rate)
    total += subtotal + sales_tax
    return total

def display_receipt(cart: dict[str, float], tax_rate):
    subtotal = 0.0
    total = 0.0

    print()
    print()
    print(LINE_SEP)
    print("         𝕊𝔸𝕃𝔼𝕊 𝕋𝔸𝕏")
    print("             &")
    print("          ℝ𝔼ℂ𝔼𝕀ℙ𝕋")
    print(LINE_SEP)
    print()

    for item, price in cart.items():
        subtotal += price # Add price before tax to subtotal
        sales_tax = calculate_sales_tax(price, tax_rate) # Calculate tax
        total_price = calculate_total(price, tax_rate) # Calculate total cost of item (price + tax)
        total += total_price # Add total price of item to total cost
        print(f"[ITEM] {item}:")
        print(f"\tPrice: ${price:.2f}")
        print(f"\tTax: ${sales_tax:.2f}")
        print(f"\tTotal Cost: ${total_price:.2f}")
        print()
    
    print(LINE_SEP)
    print()
    print(f"Tax Rate: {tax_rate * 100}%")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total: ${total:.2f}")
    print()

cart = get_shopping_cart()
display_receipt(cart, NJ_SALES_TAX)
