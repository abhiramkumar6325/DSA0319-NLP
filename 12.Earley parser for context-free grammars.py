class State:
    def __init__(self, rule, dot, start, end):
        self.rule = rule
        self.dot = dot
        self.start = start
        self.end = end

    def is_complete(self):
        return self.dot >= len(self.rule[1])

    def next_symbol(self):
        return self.rule[1][self.dot] if not self.is_complete() else None

    def __repr__(self):
        return f"{self.rule[0]} -> {' '.join(self.rule[1][:self.dot])} . {' '.join(self.rule[1][self.dot:])} [{self.start}, {self.end}]"

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased"], ["saw"]]
}

input_sentence = ["the", "cat", "chased", "the", "dog"]

def earley_parse(sentence, grammar, start_symbol="S"):
    chart = [[] for _ in range(len(sentence) + 1)]
    start_rule = (start_symbol, grammar[start_symbol][0])
    chart[0].append(State(start_rule, 0, 0, 0))

    for i in range(len(chart)):
        for state in chart[i]:
            if not state.is_complete():
                next_symbol = state.next_symbol()
                if next_symbol in grammar:
                    predict(next_symbol, i, grammar, chart)
                else:
                    scan(state, i, sentence, chart)
            else:
                complete(state, i, chart)

    return any(state.rule[0] == start_symbol and state.is_complete() and state.start == 0 and state.end == len(sentence) for state in chart[-1])

def predict(symbol, position, grammar, chart):
    for rule in grammar[symbol]:
        chart[position].append(State((symbol, rule), 0, position, position))

def scan(state, position, sentence, chart):
    if position < len(sentence) and sentence[position] == state.next_symbol():
        chart[position + 1].append(State(state.rule, state.dot + 1, state.start, position + 1))

def complete(state, position, chart):
    for prev_state in chart[state.start]:
        if prev_state.next_symbol() == state.rule[0]:
            chart[position].append(State(prev_state.rule, prev_state.dot + 1, prev_state.start, position))

print(earley_parse(input_sentence, grammar))
