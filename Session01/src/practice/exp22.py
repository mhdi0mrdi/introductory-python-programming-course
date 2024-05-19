number1 = int(input('enter your 1st num:'))
number2 = int(input('enter your 2nd num:'))
number3 = int(input('enter your 3rd num:'))

# if number1 > number2 and number2 > number3:
#     print(number1)

# elif number2 > number2 > number3:
#     print(number1)

if number1>=number2 and number1>=number3:
    print(number1)

elif number2>=number1 and number2>=number3:
    print(number2)

# elif number3>=number1 and number3>=number2:
else:
    print(number3)


