import random
from collections import defaultdict

text = "the quick brown fox jumps over the lazy dog the quick fox is quick and the dog is lazy"
words = text.split()
bigram_model = defaultdict(list)

for i in range(len(words) - 1):
    word1, word2 = words[i], words[i + 1]
    bigram_model[word1].append(word2)

def generate_text(start_word, num_words):
    current_word = start_word
    generated_text = [current_word]
    
    for _ in range(num_words - 1):
        next_words = bigram_model.get(current_word)
        if not next_words:
            break
        current_word = random.choice(next_words)
        generated_text.append(current_word)
    
    return ' '.join(generated_text)

start_word = "the"
generated_text = generate_text(start_word, 10)
print("Generated Text:", generated_text)
