from nltk import word_tokenize
from nltk import Text
from nltk.book import text6
from nltk import FreqDist

tokens = word_tokenize('My name is Polina I  a a I Polina is is is is am a python teacher')
text = Text(tokens)

print(text6)

print(len(text)/len(set(text)))
# print(len(text6)/len(set(text6)))
