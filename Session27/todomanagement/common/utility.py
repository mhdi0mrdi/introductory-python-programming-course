from os import system
from typing import Any, Hashable, Iterable


def get_input(field: str = "input", err_msg: str = "input", required: bool = True, valid_items: Iterable = ()):

    err_msg = []

    while True:
        data = input(f"{field} : ")
        system("cls")

        if required and data == "":
            err_msg.append(f"{err_msg} is empty")

        if valid_items and data not in valid_items:
            err_msg.append(f"{err_msg} not in valid range")

        if not err_msg:
            return data

        print(*err_msg, sep="\n")
        err_msg.clear()


def print_list_of_dict(data: list[dict], keys: Iterable[Hashable]):
    print("Sort", *keys, sep="\t")
    print("______________________________________________")

    for id_, item in enumerate(data, 1):
        print(id_, *[item[key] for key in keys], sep="\t")

    print("_______________________________________________")


def search_list_dict(data: list[dict], search_value: Any, search_key: Hashable) -> list[dict]:
    res = []

    for item in data:
        if item[search_key] == search_value:
            res.append(item)

    return res
