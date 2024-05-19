from random import randint


user_score = 0
pc_score = 0


while user_score<3 and pc_score<3:
    
    user_input = int(input("1.Rock 2.Paper 3.Scissors : "))
    pc_input = randint(1, 3)

    if (user_input==1 and pc_input==3) \
            or (user_input==2 and pc_input==1) \
            or (user_input==3 and pc_input==2):
        user_score += 1

    elif ((user_input==3 and pc_input==1) 
            or (user_input==1 and pc_input==2) 
            or (user_input==2 and pc_input==3)):
        pc_score += 1


if user_score==3:
    print("user won")
else:
    print("pc won")


