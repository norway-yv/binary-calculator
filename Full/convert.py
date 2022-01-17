def toByte(string):
    if len(string) != 8:
        temporaryString = string[::-1]
        for i in range(8 - len(string)):
            temporaryString += "0"
        string = temporaryString[::-1]
    return string

def to32bit(string):
    if len(string) != 32:
        temporaryString = string[::-1]
        for i in range(32 - len(string)):
            temporaryString += "0"
        string = temporaryString[::-1]
