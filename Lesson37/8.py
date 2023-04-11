from nltk import word_tokenize,sent_tokenize,pos_tag

sentences = sent_tokenize('Google is one of the best companies. I constantly google myself to see what happens')
nouns = ['NN','NNS','NNP','NNPS']
for sentence in sentences:
    if 'google' in sentence.lower():
        tagged_words = pos_tag(word_tokenize(sentence))
        for word in tagged_words:
            if word[0].lower() == 'google' and word[1] in nouns:
                print(sentence)
