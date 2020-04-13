userNameInput = input("Username : ")
passwordInput = input("Password : ")
sMask = 5
gelA = 90
fMask = 10
eGlove = 35
dSoap = 10
noBuy = 0

if userNameInput == "aaaa" and passwordInput == "aaaa":
    print("Log in complete")
    print("---Welcome to Tool Dealer shop---")
    print("-------Please select menu--------")
    print("1. Surgical mask          [5 THB/pcs]")
    print("2. Gel alcohol ethanol    [90 THB/pcs]")
    print("3. Fabric mask re-useable [10 THB/pcs]")
    print("4. Elastic glove          [35 THB/pack]")
    print("5. Dettol Soap            [10 THB/pcs]")
    print("---------------------------------")
    menuSelected = int(input("Menu Number... "))
    if menuSelected == 1:
        print("Surgical mask [5 THB/pcs]")
        piece = int(input("How Many pieces do you prefer ? "))
        result = sMask*piece
    elif menuSelected == 2:
        print("Gel alcohol ethanol [90 THB/pcs]")
        piece = int(input("How Many pieces do you prefer ? "))
        result = gelA*piece
    elif menuSelected == 3:
        print("Fabric mask re-useable [10 THB/pcs]")
        piece = int(input("How Many pieces do you prefer ? "))
        result = fMask*piece
    elif menuSelected == 4:
        print("Elastic glove [35 THB/pack]")
        piece = int(input("How Many pieces do you prefer ? "))
        result = eGlove*piece
    elif menuSelected == 5:
        print("Dettol Soap [10 THB/pcs]")
        piece = int(input("How Many pieces do you prefer ? "))
        result = dSoap*piece
    else:
        piece = 0
        result = noBuy * piece
        print("--------Unavailable Menu--------")
        print("----------We are sorry----------")
        print("--------------------------------")
    print("----------Vat invoice-----------")
    print("Total cost are.. ", result, "THB")


else:
    print("**Invalid Username or Password**")
print("------Thank you for coming-------")
print("-----------End Program-----------")

