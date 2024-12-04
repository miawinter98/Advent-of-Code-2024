from pathlib import Path
from enum import Enum

class State(Enum):
    Mul = 0,
    Number = 1,

legal_mul_characters = ["m", "u", "l"]
legal_transition_characters = ["(", ",", ")"]
legal_num_characters = list(map(lambda x: str(x), range(10)))
legal_do_characters = ["d", "o", "(", ")"]
legal_dont_characters = ["d", "o", "n", "'", "t", "(", ")"]
max_sequence = 3

if __name__ == '__main__':
    program = Path("inputs/day3.txt").read_text()
    print(program)

    result = 0

    state = (State.Mul, 0)
    meta_state = 0
    number1 = -1
    number2 = -1
    number_constructor = ""

    do = True
    do_counter = 0

    for character in program:
        if state == (State.Mul, 0):
            if do and character == legal_dont_characters[do_counter]:
                do_counter += 1
                if do_counter == len(legal_dont_characters):
                    do_counter = 0
                    do = False
                continue
            elif not do and character == legal_do_characters[do_counter]:
                do_counter += 1
                if do_counter == len(legal_do_characters):
                    do_counter = 0
                    do = True
                continue
            elif do_counter > 0:
                # do / don't seek got interrupted
                do_counter = 0

        if state[0] is State.Mul:
            if state[1] == 0 and character != legal_mul_characters[0]:
                # ignore, seek start of mul
                continue
            elif state[1] >= max_sequence:
                # check state transition
                if character == legal_transition_characters[meta_state]:
                    if meta_state < max_sequence:
                        meta_state += 1
                        state = (State.Number, 0)
                        continue
                # reset
                state = (State.Mul, 0)
                number1 = -1
                number2 = -1
                meta_state = 0
                number_constructor = ""
                continue
            elif state[1] != 0 and character != legal_mul_characters[state[1]]:
                # mul is interrupted, reset
                state = (State.Mul, 0)
                number1 = -1
                number2 = -1
                meta_state = 0
                number_constructor = ""
                continue
            state = (State.Mul, state[1] + 1)
        elif state[0] is State.Number:
            if state[1] == max_sequence or (state[1] < max_sequence and character not in legal_num_characters):
                # check state transition
                if character == legal_transition_characters[meta_state] and len(number_constructor) > 0:
                    if meta_state < max_sequence:
                        if meta_state == 1:
                            number1 = int(number_constructor)
                            state = (State.Number, 0) # seek next number
                            meta_state += 1
                            number_constructor = ""
                        else:
                            # valid mul
                            number2 = int(number_constructor)
                            if do:
                                result += (number1 * number2)
                                print("{0:3d} * {1:3d} = {2:6d} Total: {3:9d}".format(number1, number2, (number1 * number2), result))
                            else:
                                print("Mul ignored by don't")
                            # reset
                            state = (State.Mul, 0)
                            number1 = -1
                            number2 = -1
                            meta_state = 0
                            number_constructor = ""
                        continue
                else:
                    # num is interrupted, reset
                    state = (State.Mul, 0)
                    number1 = -1
                    number2 = -1
                    meta_state = 0
                    number_constructor = ""
                    continue
            state = (State.Number, state[1] + 1)
            number_constructor += character



    print("[Part 1] Result:", result)