def has_33(args):
    for num in range(0,len(args)-1):
        if num == 3 and args[num+1] == 3:
                return True
    return False


x = input("Input multiple numbers with no spaces: ")
input_list = list(x)
input_list = [int(num) for num in input_list]
print(has_33(input_list))
