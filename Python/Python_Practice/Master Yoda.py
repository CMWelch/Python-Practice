def master_yoda(string):
    return " ".join(string.split()[::-1])


x = input("Input a phrase Yoda would say: ")
print(master_yoda(x))
