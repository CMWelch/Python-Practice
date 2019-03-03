def makes_twenty(a, b):
	return a == 20 or b == 20 or a + b == 20


x = int(input("Input a number: "))
y = int(input("Input another number: "))
#print(f"{x}{y}")
print(makes_twenty(x, y))