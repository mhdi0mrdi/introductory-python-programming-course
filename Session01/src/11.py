# indent

# if condition:
#     block if
#     statement
#     statement
#     statement
#     statement

season = int(input("season :"))  # 3


if season == 1:
    print("Spring")

if season == 2:
    print("summer")

if season == 3:
    print("fall")

if season == 4:
    print("winter")

# if season!=1 and season!=2 and season!=3 and season!=4:
# if season<1 or season>4:
# if season not in (1,2,3,4):
if season not in range(1, 5):
    print("Error!")
