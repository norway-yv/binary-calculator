import adders

def bit(number, one, two):
    output = adders.start(one[number-1], two[number-1])["Output"]
    save = adders.start(one[number-1], two[number-1])["Carry"]
    output +=  adders.sum(one[number-2], two[number-2], save)
    save = adders.findCarry(one[number-2], two[number-2], save)
    for i in range(0, number-1, 1):
        output += adders.sum(one[i], two[i], save)
        save = adders.findCarry(one[i], two[i], save)
    return output[::-1]
