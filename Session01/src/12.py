score = float(input('enter your score :'))


if score >= 0 and score < 50:
    print("fail")

if score >= 50 and score < 80:
    print("not bad")

if score >= 80 and score <= 100:
    print("good")

if score < 0 or score > 100:
    print("error")
