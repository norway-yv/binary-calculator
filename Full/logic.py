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
