
from os import system

# region input
while True:
    num = int(input("Number : (1,4) :"))
    system('cls')

    if num in range(1,5):
        break
    
    print("Invalid number")
# endregion

# region input numbers
num1 = int(input("Number1 :"))
num2 = int(input("Number2 :"))
system("cls")
# endregion

# region math operations
match num:
    case 1:
        print("num1+num2 :" ,num1 + num2)
    case 2:
        print("num1-num2 :" ,num1 - num2)
    case 3:
        print("num1*num2 :" ,num1 * num2)
    case 4:
        print("num1/num2 :" , num1 / num2)
# endregion

              
    