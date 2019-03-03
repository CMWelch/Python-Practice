def spy_game(nums):
    first0 = False
    second0 = False

    for num in nums:
        if num == 0 and first0 is False:
            first0 = True
        elif num == 0 and first0 is True:
            second0 = True
        elif num == 7 and (first0 is True and second0 is True):
            return True
        else:
            continue
    return False

#code = [0, 0, 7, 'x']
# for num in nums:
#    if num == code[0]:
#        code.pop()
# return len(code) == 1


num_list = [1, 7, 4, 0, 0, 8, 5]
print(spy_game(num_list))
