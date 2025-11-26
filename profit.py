actual_price=float(input("Enter the price of the original product:   "))
sale_price=float(input("Enter the price you resold it:   "))
if sale_price>actual_price:
    profit=sale_price-actual_price
    print("Profit =", profit)
else:
    loss = actual_price - sale_price
    print("Loss =", loss)
