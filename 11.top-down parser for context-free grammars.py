grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased"], ["saw"]]
}

input_sentence = ["the", "cat", "chased", "the", "dog"]

def parse(symbol, tokens, pos):
    if pos >= len(tokens):
        return False, pos

    if symbol not in grammar:
        if pos < len(tokens) and tokens[pos] == symbol:
            return True, pos + 1
        return False, pos

    for rule in grammar[symbol]:
        current_pos = pos
        matched = True
        for sub_symbol in rule:
            success, current_pos = parse(sub_symbol, tokens, current_pos)
            if not success:
                matched = False
                break
        if matched:
            return True, current_pos

    return False, pos

def parse_sentence():
    success, final_pos = parse("S", input_sentence, 0)
    return success and final_pos == len(input_sentence)

print(parse_sentence())
