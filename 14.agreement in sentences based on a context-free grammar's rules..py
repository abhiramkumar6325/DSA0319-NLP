import nltk
from nltk import CFG

# Define a grammar with agreement rules
grammar = CFG.fromstring("""
    S -> NP[sg] VP[sg] | NP[pl] VP[pl]
    NP[sg] -> Det[sg] N[sg]
    NP[pl] -> Det[pl] N[pl]
    VP[sg] -> V[sg]
    VP[pl] -> V[pl]
    Det[sg] -> 'the'
    Det[pl] -> 'the'
    N[sg] -> 'cat'
    N[pl] -> 'cats'
    V[sg] -> 'sleeps'
    V[pl] -> 'sleep'
""")

def check_agreement(sentence, grammar):
    parser = nltk.ChartParser(grammar)
    try:
        parse_trees = list(parser.parse(sentence))
        if parse_trees:
            print("The sentence has agreement.")
            for tree in parse_trees:
                print(tree)
        else:
            print("The sentence does not have agreement.")
    except ValueError as e:
        print(f"Error parsing the sentence: {e}")

sentence1 = ["the", "cat", "sleeps"]   
sentence2 = ["the", "cats", "sleep"]   
sentence3 = ["the", "cat", "sleep"]    
sentence4 = ["the", "cats", "sleeps"]  
print("Checking sentence 1:")
check_agreement(sentence1, grammar)
print("\nChecking sentence 2:")
check_agreement(sentence2, grammar)
print("\nChecking sentence 3:")
check_agreement(sentence3, grammar)
print("\nChecking sentence 4:")
check_agreement(sentence4, grammar)
