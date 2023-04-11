
from nltk.book import text6
from nltk import FreqDist
fdist = FreqDist(text6)
print(fdist.most_common(15))