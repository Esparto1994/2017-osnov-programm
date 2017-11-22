import sys
sent_id=1

for c in sys.stdin.readlines():
	number=1
	c = c.replace('.', ' . ')
	c = c.replace(',', ' , ')
	c = c.replace('(', ' ( ')
	c = c.replace(')', ' ) ')
	c = c.replace(':', ' : ')
	c = c.replace(';', ' ; ')
	c = c.split(' ')
	print(sent_id)
	for i in c:
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_'%(number,i))
		number=number+1
	sent_id=sent_id+1