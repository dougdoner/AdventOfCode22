def calc_rock_paper_scissors():
    with open('rps.txt', 'r') as file:
        counter = 0
        for line in file:
            opponent_shape, my_shape = line.split(' ')
            counter += calc_round_and_my_hand(parse_my_shape(opponent_shape.strip()), parse_my_shape(my_shape.strip()))

        print(counter)


def parse_my_shape(shape):
    # rock
    if shape == 'X' or shape == 'A':
        return 1
    # paper
    elif shape == 'Y' or shape == 'B':
        return 2
    # scissors
    else:
        return 3


def calc_round(opponent, me):
    if me == opponent:
        return me + 3
    elif (opponent - me) % 3 == 2:
        return me + 6
    else:
        return me


def calc_round_and_my_hand(opponent, round_type):
    # if draw
    if round_type == 2:
        return opponent + 3
    # if win
    elif round_type == 3:
        # if rock
        if opponent == 1:
            return 8
        # if paper
        elif opponent == 2:
            return 9
        # if scissor
        else:
            return 7
    # if lose
    else:
        if opponent == 1:
            return 3
        elif opponent == 2:
            return 1
        else:
            return 2
