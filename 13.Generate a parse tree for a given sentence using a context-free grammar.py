import nltk
from nltk import CFG
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'saw'
""")
sentence = ["the", "cat", "chased", "the", "dog"]
parser = nltk.ChartParser(grammar)
for tree in parser.parse(sentence):
    tree.pretty_print()  
