import sys

wiki =  open('corpus/wiki.txt', encoding = 'utf-8-sig')

wiki = wiki.read()

segmenter = wiki.replace('. ', '. \n')
print(segm





