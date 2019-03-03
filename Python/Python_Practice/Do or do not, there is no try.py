
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("You can not perform math operations on strings")


try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("Divide by zero error")
finally:
    print("Done")

while True:
    try:
        int(input("Enter a number: "))
    except:
        print("That is not a number, try again.")
    else:
        break