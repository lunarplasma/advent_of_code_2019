DAY2_DATA = [
    1, 0, 0, 3,
    1, 1, 2, 3,
    1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 6, 23,
    2, 13, 23, 27, 1, 27, 13, 31, 1, 9, 31, 35, 1, 35, 9, 39, 1, 39, 5, 43, 2,
    6, 43, 47, 1, 47, 6, 51, 2, 51, 9, 55, 2, 55, 13, 59, 1, 59, 6, 63, 1, 10,
    63, 67, 2, 67, 9, 71, 2, 6, 71, 75, 1, 75, 5, 79, 2, 79, 10, 83, 1, 5, 83,
    87, 2, 9, 87, 91, 1, 5, 91, 95, 2, 13, 95, 99, 1, 99, 10, 103, 1, 103, 2,
    107, 1, 107, 6, 0, 99, 2, 14, 0, 0]

DAY_2_PART2 = [
    1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 6, 23, 2, 13,
    23, 27, 1, 27, 13, 31, 1, 9, 31, 35, 1, 35, 9, 39, 1, 39, 5, 43, 2, 6, 43, 47, 1, 47,
    6, 51, 2, 51, 9, 55, 2, 55, 13, 59, 1, 59, 6, 63, 1, 10, 63, 67, 2, 67, 9, 71, 2, 6,
    71, 75, 1, 75, 5, 79, 2, 79, 10, 83, 1, 5, 83, 87, 2, 9, 87, 91, 1, 5, 91, 95, 2, 13,
    95, 99, 1, 99, 10, 103, 1, 103, 2, 107, 1, 107, 6, 0, 99, 2, 14, 0, 0
]


def but_first(data):
    """
    ...before running the program, replace position 1 with the value 12 and
    replace position 2 with the value 2.
    :param data:
    :return:
    """
    data[1] = 12
    data[2] = 2
    return data


def add(data, ip1, ip2, op):
    data[op] = data[ip1] + data[ip2]
    return data


def multiply(data, ip1, ip2, op):
    data[op] = data[ip1] * data[ip2]
    return data


def solve_day2():
    """
    The opcode indicates what to do; for example, 99 means that the program is finished
    and should immediately halt. Encountering an unknown opcode means something went wrong.

    Opcode 1 adds together numbers read from two positions and stores the result
    in a third position. The three integers immediately after the opcode tell you
    these three positions - the first two indicate the positions from which you
    should read the input values, and the third indicates the position at which the
    output should be stored.

    For example, if your Intcode computer encounters 1,10,20,30, it should read
    the values at positions 10 and 20, add those values, and then overwrite the value
    at position 30 with their sum.

    Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead
    of adding them. Again, the three integers after the opcode indicate where the inputs
    and outputs are, not their values.

    Once you're done processing an opcode, move to the next one
    by stepping forward 4 positions.
    :return:
    """

    data = but_first(DAY2_DATA)
    opcode_map = {1: add, 2: multiply}
    data_end = len(data)

    position = 0

    while position <= data_end:
        raw = data[position: position + 4]
        input_1 = input_2 = output = 0
        if len(raw) is 4:
            opcode, input_1, input_2, output = raw
        else:
            opcode = raw[0]

        if opcode is 99:
            break
        operation = opcode_map[opcode]
        data = operation(data, input_1, input_2, output)
        position = position + 4

    print(data)


solve_day2()
