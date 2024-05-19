from os import system


score_list = [None] * 100

# set
for index in range(len(score_list)):

    # region get score
    while True:
        score = float(input("score : "))
        system("cls")

        if 0<=score<=100:
            break

        print("Error")
    # endregion

    score_list[index] = score



min_ = max_ = score_list[0]
sum_ = 0

#get
for score in score_list:
    sum_ += score

    if score <min_:
        min_ = score
    elif score>max_:
        max_ = score


print("Min : ", min_)
print("Max : ", max_)
print("Avg : ", sum_/len(score_list))
