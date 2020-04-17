menuList = []
priceList = []

def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(number,menuList[number],priceList[number])

def sumBill():
    print("--------------------")
    totalPrice = 0
    for number in range(len(menuList)):
        totalPrice = totalPrice+menuPrice
    print("Total Price are ..", totalPrice, "THB")

while True:
    menuName = input("Please enter your menu >> ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Please enter your price >> "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
sumBill()
