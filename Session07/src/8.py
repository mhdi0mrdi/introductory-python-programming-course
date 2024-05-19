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


print("Min : ", min(score_list))
print("Max : ", max(score_list))
print("Avg : ", sum(score_list)/len(score_list))
