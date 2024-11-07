import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, BigramTagger
from nltk.tag import BrillTagger, BrillTransformer

nltk.download('treebank')
nltk.download('punkt')

train_sents = treebank.tagged_sents()

unigram_tagger = UnigramTagger(train_sents)
bigram_tagger = BigramTagger(train_sents, backoff=unigram_tagger)

brill_tagger = BrillTagger(
    bigram_tagger,
    transformations=[
        BrillTransformer(r'\b(?:is|are|was|were)\b', 'VB'),
        BrillTransformer(r'\b(?:I|you|he|she|it|we|they)\b', 'PRP')
    ]
)

sentence = "I am learning NLP".split()

tagged_sentence = brill_tagger.tag(sentence)

print(tagged_sentence)
