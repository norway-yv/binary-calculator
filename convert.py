def toByte(string):
    if len(string) != 8:
        temporaryString = string[::-1]
        for i in range(8 - len(string)):
            temporaryString += "0"
        string = temporaryString[::-1]
    return string
