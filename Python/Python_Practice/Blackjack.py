def black_jack(a, b ,c):
    total = a + b + c
    
    if total > 21:
        if a == 11:
            total -= 10
        if total > 21 and b == 11:
            total -= 10
        if total > 21 and c == 11:
            total -= 10
    if total > 21:
        return "BUST"
    else:
        return total


x = int(input("Input a number between 1 and 11: "))
y = int(input("Input another number between 1 and 11: "))
z = int(input("Input another number between 1 and 11: "))
print(black_jack(x, y, z))


