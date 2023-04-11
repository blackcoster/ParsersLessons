from nltk import ngrams, FreqDist
from nltk.book import text6

fourgrams = ngrams(text6,4)
bigramsDist = FreqDist(fourgrams)
print(bigramsDist[('father','smelt','of','elderberries')])
