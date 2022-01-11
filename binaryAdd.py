import adders


def byte(one, two):
    output = ""
    output += adders.start(one[7], two[7])["Output"]
    output += adders.sum(one[6], two[6], adders.start(one[7], two[7])["Carry"])
    output += adders.sum(one[5], two[5], adders.findCarry(one[6], two[6], adders.start(one[7], two[7])["Carry"]))
    output += adders.sum(one[4], two[4], adders.findCarry(one[5], two[5], adders.findCarry(one[6], two[6], adders.start(one[7], two[7])["Carry"])))
    output += adders.sum(one[3], two[3], adders.findCarry(one[4], two[4], adders.findCarry(one[5], two[5], adders.findCarry(one[6], two[6], adders.start(one[7], two[7])["Carry"]))))
    output += adders.sum(one[2], two[2], adders.findCarry(one[3], two[3], adders.findCarry(one[4], two[4], adders.findCarry(one[5], two[5], adders.findCarry(one[6], two[6], adders.start(one[7], two[7])["Carry"])))))
    output += adders.sum(one[1], two[1], adders.findCarry(one[2], two[2], adders.findCarry(one[3], two[3], adders.findCarry(one[4], two[4], adders.findCarry(one[5], two[5], adders.findCarry(one[6], two[6], adders.start(one[7], two[7])["Carry"]))))))
    output += adders.sum(one[0], two[0], adders.findCarry(one[1], two[1], adders.findCarry(one[2], two[2], adders.findCarry(one[3], two[3], adders.findCarry(one[4], two[4], adders.findCarry(one[5], two[5], adders.findCarry(one[6], two[6], adders.start(one[7], two[7])["Carry"])))))))
    return output[::-1]
