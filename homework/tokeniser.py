import sys

wiki =  open('corpus/wiki.txt', encoding = 'utf-8-sig')

wiki = wiki.read()


tokeniser  = wiki.replace ('. ', '. \n')

tokeniser = tokeniser.replace('.', ' . ')
tokeniser = tokeniser.replace(',', ' , ')
tokeniser = tokeniser.replace('(', ' ( ')
tokeniser = tokeniser.replace(')', ' ) ')
tokeniser = tokeniser.replace(':', ' : ')
tokeniser = tokeniser.replace(';', ' ; ')
tokeniser  = tokeniser.replace (' ', '\n')
print(tokeniser)





