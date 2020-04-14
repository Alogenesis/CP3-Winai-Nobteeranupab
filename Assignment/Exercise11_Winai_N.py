numberInput = int(input("How many floor of your pyramid? .."))
x = 0
for y in range(numberInput):
    print(" "*(numberInput-(y+1))+"*"*(x+1))
    x= x+2