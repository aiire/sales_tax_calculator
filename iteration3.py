import os

sales_tax_per_state = {
        'AK': 0.00 / 100,
        'AL': 4.00 / 100,
        'AR': 6.50 / 100,
        'AS': 15.00 / 100,
        'AZ': 5.60 / 100,
        'CA': 7.25 / 100,
        'CO': 2.90 / 100,
        'CT': 6.35 / 100,
        'DC': 6.00 / 100,
        'DE': 0.00 / 100,
        'FL': 6.00 / 100,
        'GA': 4.00 / 100,
        'GU': 2.00 / 100,
        'HI': 4.00 / 100,
        'IA': 6.00 / 100,
        'ID': 6.00 / 100,
        'IL': 6.25 / 100,
        'IN': 7.00 / 100,
        'KS': 6.50 / 100,
        'KY': 6.00 / 100,
        'LA': 4.45 / 100,
        'MA': 6.25 / 100,
        'MD': 6.00 / 100,
        'ME': 5.50 / 100,
        'MI': 6.00 / 100,
        'MN': 6.875 / 100,
        'MO': 4.225 / 100,
        'MP': 0.00 / 100,
        'MS': 7.00 / 100,
        'MT': 0.00 / 100,
        'NC': 4.75 / 100,
        'ND': 5.00 / 100,
        'NE': 5.50 / 100,
        'NH': 0.00 / 100,
        'NJ': 6.625 / 100,
        'NM': 4.875 / 100,
        'NV': 6.85 / 100,
        'NY': 4.00 / 100,
        'OH': 5.75 / 100,
        'OK': 4.50 / 100,
        'OR': 0.00 / 100,
        'PA': 6.00 / 100,
        'PR': 11.50 / 100,
        'RI': 7.00 / 100,
        'SC': 6.00 / 100,
        'SD': 4.20 / 100,
        'TN': 7.00 / 100,
        'TX': 6.25 / 100,
        'UT': 6.10 / 100,
        'VA': 5.30 / 100,
        'VI': 0.00 / 100,
        'VT': 6.00 / 100,
        'WA': 6.50 / 100,
        'WI': 5.00 / 100,
        'WV': 6.00 / 100,
        'WY': 4.00 / 100
}

LINE_SEP_HALF = '=' * 5
LINE_SEP = LINE_SEP_HALF * 6 # 30 '='

def get_shopping_cart():
    count = int(input('Enter the amount of items you want to buy: '))
    print()
    cart = {}
    for i in range(count):
        item = input(f'Enter the name of item {i + 1}: ')
        print()
        price = float(input(f'Enter the price of item {i + 1}: $'))
        print()
        cart[item] = price
    return cart

def get_state_sales_tax(sales_tax):
    state = input('Enter the state you live in (as abbreviation): ').upper().strip()
    print()
    return sales_tax[state]

def calculate_sales_tax(price, tax_rate):
    return price * tax_rate

def calculate_total(subtotal, tax_rate):
    total = 0.0
    tax = calculate_sales_tax(subtotal, tax_rate)
    total += subtotal + tax
    return total

def clear():
    if os.name == 'posix':
        os.system('clear') # For Linux users
    elif os.name == 'nt':
        os.system('cls') # For Windows users

def title():
    print()
    print()
    print(LINE_SEP)
    print('         𝕊𝔸𝕃𝔼𝕊 𝕋𝔸𝕏')
    print('             &')
    print('          ℝ𝔼ℂ𝔼𝕀ℙ𝕋')
    print(LINE_SEP)
    print()
    input("Press Enter to Begin . . . ")
    clear()

def display_receipt(cart, tax_rate):    
    subtotal = 0.0
    total = 0.0

    print()

    for item, price in cart.items():
        subtotal += price # Add price before tax to subtotal
        tax = calculate_sales_tax(price, tax_rate) # Calculate tax
        total_price = calculate_total(price, tax_rate) # Calculate total cost of item (price + tax)
        total += total_price # Add total price of item to total cost
        print(f'Item: {item}')
        print(f'Price: ${price:.2f}')
        print(f'Tax: ${tax:.2f}')
        print(f'Total Cost: ${total_price:.2f}')
        print()

    print(LINE_SEP_HALF + ' SUMMARY ' + LINE_SEP_HALF)
    print(f'Tax Rate: {tax_rate * 100}%')
    print(f'Subtotal: ${subtotal:.2f}')
    print(f'Total: ${total:.2f}')
    print(LINE_SEP)
    print()

title()

state_sales_tax = get_state_sales_tax(sales_tax_per_state) 
cart = get_shopping_cart()
display_receipt(cart, state_sales_tax)
