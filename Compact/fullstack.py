def AND(one, two):
    if one == "1" and two == "1":
        return "1"
    else:
        return "0"

def OR(one, two):
    if one == "1" or two == "1":
        return "1"
    else:
        return "0"

def XOR(one, two):
    if (one == "1" or two == "1") and not (one == "1" and two == "1"):
        return "1"
    else:
        return "0"

def start(one, two):
    return {
        "Output": XOR(one, two),
        "Carry": AND(one, two)
    }

def sum(one, two, carried):
    return XOR(carried, XOR(one, two))

def findCarry(one, two, carried):
    return OR(AND(carried, XOR(one, two)), AND(one, two))

def bit(number, one, two):
    output = start(one[number-1], two[number-1])["Output"]
    save = start(one[number-1], two[number-1])["Carry"]
    output +=  sum(one[number-2], two[number-2], save)
    save = findCarry(one[number-2], two[number-2], save)
    for i in range(0, number-1, 1):
        output += sum(one[i], two[i], save)
        save = findCarry(one[i], two[i], save)
    return output[::-1]

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

inputOne = input("First number = ")
inputTwo = input("Second number = ")

if len(inputOne) > len(inputTwo):
    inputTwo = toBit(len(inputOne), inputTwo)
elif len(inputTwo) > len(inputOne):
    inputOne = toBit(len(inputTwo), inputOne)

print(f"Output: {shorten(bit(len(inputOne), inputOne, inputTwo))}")
