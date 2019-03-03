def num_uppers(string):
    uppers = 0
    lowers = 0
    for letter in string:
        if letter.isupper():
            uppers += 1
        elif letter.islower():
            lowers += 1
        else:
            continue
    print(lowers, uppers)


num_uppers("I am")


def count_uppers(string):
    def upper(letter):
        return letter.isupper()

    def lower(letter):
        return letter.islower()

    uppers = len(list(filter(upper, string)))
    lowers = len(list(filter(lower, string)))
    return lowers, uppers


print(count_uppers("I am"))
