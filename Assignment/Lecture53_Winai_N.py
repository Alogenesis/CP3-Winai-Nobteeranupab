def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
priceInput = float(input("Enter your price .."))
print("Vat included price is",vatCalculate(priceInput),"THB")
