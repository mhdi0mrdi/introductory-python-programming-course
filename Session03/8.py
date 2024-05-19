odd_number = 0
even_number = 0
i = 1


while i <= 100:
    num = int(input('num :'))

    if num % 2 == 0:
        even_number += 1
    else:
        odd_number += 1

    i += 1


print("odd numbers:", odd_number, "even numbers:", even_number)
