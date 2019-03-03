import string


def is_pangram(str1, alphabet=string.ascii_lowercase):
    lower = str1.lower()
    for letter in alphabet:
        if not (letter in lower):
            return False
    return True


print(is_pangram("I went to the store"))
