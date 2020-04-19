class Customer:
    name = ""
    lastName = ""
    age = 0
    def addCart(self):
        print("Added to ",self.name,self.lastName, "'s cart")

customer1 = Customer()
customer1.name = "Winai"
customer1.lastName = "Nobteeranupab"
customer1.age = 28
customer1.addCart()

customer2 = Customer()
customer2.name = "Pang"
customer2.lastName = "Pond"
customer2.age = 21
customer2.addCart()

customer3 = Customer()
customer3.name = "Ton"
customer3.lastName = "Chef"
customer3.age = 37
customer3.addCart()

customer4 = Customer()
customer4.name = "Sittibodi"
customer4.lastName = "Knight"
customer4.age = 15
customer4.addCart()