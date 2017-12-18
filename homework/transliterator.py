# This is a transliterator prog from latin to cyr, and it is a preliminary work to my latin to IPA transliterator project work.
# does not go with the pipe segmenter -> tokeniser
# launch corpus/wiki.txt | python3 transliterator.py or corpus/wiki.txt | python3 segmenter1.py | python3 transliterator.py
import sys
sent_id = 1

CYRdict = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "абкдефгхижклмнопкрстувокызАБКДЕФГХИЖКЛМНОПКРСТУВОКЫЗ")

for c in sys.stdin.readlines():
	number = 1
	c = c.replace('.', ' . ')
	c = c.replace(',', ' , ')
	c = c.replace('(', ' ( ')
	c = c.replace(')', ' ) ')
	c = c.replace(':', ' : ')
	c = c.replace(';', ' ; ')
	c = c.split(' ')
	print('#sent_id=%d'%(sent_id))
	for i in c:
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\ttranslit=%s'%(number,i,i.translate(CYRdict)))
		number = number + 1
	sent_id=sent_id+1




	