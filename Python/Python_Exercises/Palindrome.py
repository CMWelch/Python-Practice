def palindrome(string):
    if len(string) % 2 == 0:
        return string[:int(len(string) / 2)] == string[int(len(string) / 2):][::-1]
    else:
        return string[:int(len(string) / 2)] == string[int(len(string) / 2)+1:][::-1]


print(palindrome("boggles"))
