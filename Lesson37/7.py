from nltk import ngrams, FreqDist
from nltk.book import text6

fourgrams = ngrams(text6,4)
for fourgram in fourgrams:
    if fourgram[0] == 'coconut':
        print(fourgram)
