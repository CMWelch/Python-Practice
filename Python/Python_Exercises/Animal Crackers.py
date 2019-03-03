def animal_crackers(text):
	return text.split()[0][0].lower() == text.split()[1][0].lower()


x = input("Enter two words: ")
print(animal_crackers(x))
