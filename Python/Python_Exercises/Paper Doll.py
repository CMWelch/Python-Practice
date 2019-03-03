def paper_doll(string):
    new_string = ""

    for letter in string:
        if letter == " ":
            new_string = new_string + letter
        else:
            new_string = new_string + letter * 3
    return new_string


x = input("Input a string: ")
print(paper_doll(x))
