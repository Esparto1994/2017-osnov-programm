import sys 

wiki =  open('corpus/wiki.txt', encoding = 'utf-8-sig')

wiki = wiki.read()

lines = 0
tokens = 0
characters = 0

for c in wiki :
	if c == ' ':
		tokens = tokens + 1
	if c == '\n':
		lines = lines + 1
	characters = characters + 1

print("The number of lines is: ", lines)
print("The number of tokens is: ", tokens)
print("The number of character is: ", characters)