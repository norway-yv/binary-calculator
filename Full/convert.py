def shorten(string):
    if string[0] != "1":
        string = string[string.index("1"):]
    return string

def toBit(number, string):
    if len(string) != number:
        string = string[::-1]
        for i in range(number - len(string)):
            string += "0"
        string = string[::-1]
    return string
