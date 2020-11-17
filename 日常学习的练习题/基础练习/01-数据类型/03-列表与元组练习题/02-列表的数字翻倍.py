def double_list(lst):
    for index, item in enumerate(lst):
        if isinstance(item, bool):
            continue
        if isinstance(item, (int, float)):
            lst[index] *= 2
        if isinstance(item, list):
            double_list(item)


if __name__ == "__main__":
    lst = [1, [4, 6], True]
    double_list(lst)
    print(lst)
