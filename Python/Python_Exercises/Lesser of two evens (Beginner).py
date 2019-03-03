x = 2
y = 4


def lesser_of_two_evens(a,b):
	if a > b:
		greater_num = a
		lesser_num = b
	else:
		greater_num = b
		lesser_num = a

	if a % 2 == 0 and b % 2 == 0:
		print(lesser_num)
		return lesser_num
	else: 
		print(greater_num)
		return greater_num


lesser_of_two_evens(x,y)
