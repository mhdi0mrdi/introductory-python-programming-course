score = float(input('enter your score :'))


# if score >= 0 and score < 50:
if 0<=score<50:
    print("fail")

elif score >= 50 and score < 70:
    print("not bad")

elif score >= 70 and score <= 90:
    print("good")

elif score >= 90 and score <= 100:
    print("exellent")

# if score < 0 or score > 100:
else:
    print("error")


