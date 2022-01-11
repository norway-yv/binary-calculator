import logic


def start(one, two):
    return {
        "Output": logic.XOR(one, two),
        "Carry": logic.AND(one, two)
    }


def sum(one, two, carried):
    return logic.XOR(carried, logic.XOR(one, two))


def findCarry(one, two, carried):
    return logic.OR(logic.AND(carried, logic.XOR(one, two)), logic.AND(one, two))
