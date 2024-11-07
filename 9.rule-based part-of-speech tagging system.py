import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')

train_sents = [
    [("NLTK", "NNP"), ("is", "VBZ"), ("a", "DT"), ("tool", "NN")],
    [("It", "PRP"), ("is", "VBZ"), ("useful", "JJ")],
    [("Natural", "JJ"), ("Language", "NN"), ("Processing", "NNP")]
]

regexp_tagger = RegexpTagger(
    [
        (r'^[-a-zA-Z]+$', 'NNP'),
        (r'^[A-Za-z]+$', 'NN'),
        (r'^[.,;?!]+$', '.'),
        (r'\b(?:I|you|he|she|it|we|they)\b', 'PRP'),
        (r'\b(?:is|are|was|were)\b', 'VBZ'),
        (r'\b(?:a|an|the)\b', 'DT'),
        (r'\b(?:useful|good|best|powerful)\b', 'JJ')
    ]
)

sentence = "NLTK is a powerful tool".split()

tagged_sentence = regexp_tagger.tag(sentence)

print(tagged_sentence)
