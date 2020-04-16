def login():
    userNameInput = input("Username : ")
    passwordInput = input("Password : ")
    if userNameInput == "aaaa" and passwordInput == "aaaa":
        return True
    else:
        return False

def showMenu():
        print("---Log in complete---")
        print("-----iShop Menu------")
        print("1. Vat Calculator")
        print("2. Total Price included Vat")

def menuSelect():
    menuselected = int(input("Menu number : "))
    return menuselected
def vatCalMenu():
    totalPrice = int(input("Enter your price to calculate Vat included price .."))
    vat = 7                                       
    result = totalPrice + (totalPrice * vat / 100)
    print("Vat included price is",result,"THB")
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("Price of menu 1 = ? "))
    price2 = int(input("Price of menu 2 = ? "))
    print("Included Vat price are ..",vatCalculate(price1+price2),"THB")

#WorkFlow
if login():
    showMenu()
    getMenuSelected = menuSelect()
    if int(getMenuSelected) == 1:
        vatCalMenu()
    elif int(getMenuSelected) == 2:
        priceCalculate()
    else:
        print("Unavailable menu")
else:
    print("Invalid ID or Password")
print("End Program")
