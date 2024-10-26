from os import system


gf_list = []

while True:
    print("add gf (1) :")
    print("show list (2) :")
    print("remove (3) :")
    print("exit (4) :")
    menu = int(input("enter menu :"))
    system('cls')

    match menu:
        case 1:
            # region name

            while True:
                name = input("name :")

                if name != "":
                    break
                print("error!")
            # endregion

            # region family
            while True:
                family = input("family :")

                if family != "":
                    break
                print("error!")
            # endregion

             # region name
            while True:
                number = input("number :")

                if number == "":
                    print("error!")
                    continue

                for gf in gf_list:
                    if gf[2] == number:
                        print("number already exist!")
                        break
                else:
                    break
            # endregion

            girl = [name, family, number]
            gf_list.append(girl)

        case 2:
            print("_________________________")

            for girl in gf_list:
                print(*gf, sep="\t")
            print("_________________________")

        case 3:
            # region show
            print("_________________________")

            for girl in gf_list:
                print(*gf, sep="\t")
            print("_________________________")
            # endregion

            # region remove key
            while True:
                remove_key = input("remove key (name(1),family(2),number(3) :")

                if remove_key == (1, 2, 3):
                    break
                print("error")
            # endregion

            # region remove value
            match remove_key:
                case 1 :
                    remove_value = input("name :")
                    remove_index = 0
                    
                case 2 :
                    remove_value = input("family :")
                    remove_index = 1

    
                case 3 :
                    remove_value = input("number :")
                    remove_index = 2

            # endregion

            for gf in gf_list.copy() :
                if gf[remove_index] == remove_value:
                    print("full name :" , gf[0] , gf[1] , "number :" , gf[2])
                    if input("are you sure ? :") == "yes":
                        gf_list.remove(gf)

        case 4:
            break

        case _:
            print("error")
