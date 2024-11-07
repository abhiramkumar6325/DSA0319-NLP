import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, BigramTagger

nltk.download('treebank')
nltk.download('universal_tagset')

train_sents = treebank.tagged_sents()

unigram_tagger = UnigramTagger(train_sents)
bigram_tagger = BigramTagger(train_sents, backoff=unigram_tagger)

sentence = "NLTK is a powerful tool for natural language processing".split()

tagged_sentence = bigram_tagger.tag(sentence)

print(tagged_sentence)
