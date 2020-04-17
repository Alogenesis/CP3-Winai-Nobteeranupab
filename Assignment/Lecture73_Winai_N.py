systemMenu = {"ข้าว":10, "ไข่":20, "ข้าวหมกไข่":45,"ข้าวไข่เจียว":50}
menuList = []
def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(number+1,menuList[number])

def sumBill():
    print("--------------------")
    totalPrice = 0
    for number in range(len(menuList)):
        totalPrice = totalPrice+menuList[number][1]
    print("Total Price are ..", totalPrice, "THB")

while True:
    menuName = input("Please enter your menu >> ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
showBill()
sumBill()
