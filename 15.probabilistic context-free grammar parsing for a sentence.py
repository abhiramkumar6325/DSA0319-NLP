import nltk
from nltk import PCFG
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.8] | 'John' [0.2]
    VP -> V NP [0.6] | V [0.4]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'dog' [0.5] | 'cat' [0.5]
    V -> 'sees' [1.0]
""")

sentence = ["John", "sees", "the", "dog"]

parser = nltk.ViterbiParser(pcfg_grammar)

print("Parsing the sentence with PCFG:")
for tree in parser.parse(sentence):
    print(tree)
