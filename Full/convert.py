def toByte(string):
    if len(string) != 8:
        string = string[::-1]
        for i in range(8 - len(string)):
            string += "0"
        string = string[::-1]
    return string

def to32bit(string):
    if len(string) != 32:
        string = string[::-1]
        for i in range(32 - len(string)):
            string += "0"
        string = string[::-1]
    return string

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
