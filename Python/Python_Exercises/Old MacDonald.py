def old_macdonald(name="Name"):
    new_list = list(name)
    new_list[0] = new_list[0].upper()
    new_list[3] = new_list[3].upper()
    print(new_list)
    return "".join(new_list)

#first_half = name[:3]
#second_half = name[3:]
#return first_half.capitalize() + second_half.capitalize()


x = input("Input a name: ")
print(old_macdonald(x))


