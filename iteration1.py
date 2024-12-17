NJ_SALES_TAX = 0.06625

subtotal = float(input("Enter purchase: "))
tax = subtotal * NJ_SALES_TAX
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
