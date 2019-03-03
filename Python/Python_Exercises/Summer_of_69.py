def summer_69(input):
    bool6 = False
    total = 0
    for num in input:
        if num == 6:
            bool6 = True
        if num == 9 and bool6:
            bool6 = False
        elif not bool6:
            total += num
    return total


print(summer_69([1, 2, 3, 6, 9, 1, 3, 5, 6, 7, 9]))
