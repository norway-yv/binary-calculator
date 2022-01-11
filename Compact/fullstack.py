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


def toByte(string):
    if len(string) != 8:
        temporaryString = string[::-1]
        for i in range(8 - len(string)):
            temporaryString += "0"
        string = temporaryString[::-1]
    return string


def start(one, two):
    return {
        "Output": XOR(one, two),
        "Carry": AND(one, two)
    }


def sum(one, two, carried):
    return XOR(carried, XOR(one, two))


def findCarry(one, two, carried):
    return OR(AND(carried, XOR(one, two)), AND(one, two))


def byte(one, two):
    output = ""
    output += start(one[7], two[7])["Output"]
    output += sum(one[6], two[6], start(one[7], two[7])["Carry"])
    output += sum(one[5], two[5], findCarry(one[6], two[6], start(one[7], two[7])["Carry"]))
    output += sum(one[4], two[4], findCarry(one[5], two[5], findCarry(one[6], two[6], start(one[7], two[7])["Carry"])))
    output += sum(one[3], two[3], findCarry(one[4], two[4], findCarry(one[5], two[5], findCarry(one[6], two[6], start(one[7], two[7])["Carry"]))))
    output += sum(one[2], two[2], findCarry(one[3], two[3], findCarry(one[4], two[4], findCarry(one[5], two[5], findCarry(one[6], two[6], start(one[7], two[7])["Carry"])))))
    output += sum(one[1], two[1], findCarry(one[2], two[2], findCarry(one[3], two[3], findCarry(one[4], two[4], findCarry(one[5], two[5], findCarry(one[6], two[6], start(one[7], two[7])["Carry"]))))))
    output += sum(one[0], two[0], findCarry(one[1], two[1], findCarry(one[2], two[2], findCarry(one[3], two[3], findCarry(one[4], two[4], findCarry(one[5], two[5], findCarry(one[6], two[6], start(one[7], two[7])["Carry"])))))))
    return output[::-1]


inputOne = toByte(input("First number = "))
inputTwo = toByte(input("Second number = "))

print(f"Output: {byte(inputOne, inputTwo)}")
