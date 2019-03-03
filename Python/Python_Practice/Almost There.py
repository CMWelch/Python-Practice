def almost_there(num):
    return 100-10 <= num <= 100+10 or 200-10 <= num <= 200+10



x = int(input("Input a number: "))
print(almost_there(x))
