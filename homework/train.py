# The file with the annotated parts of speech is called 'POS.txt' in the same directory

import sys
import re
import string

ListOfWords = []
POS = []
RES = []
RES1 = []
dic = {}
dic1 = {}
dic2 = {}
dic3 = {}

for c in sys.stdin.readlines(): 
	if not "#" in c:
		if c.strip():
			ListOfWords.append(c.split('\t')[1])
			if c.split('\t')[3] in '_':
				POS.append(c.split('\t')[4])
			else:
				POS.append(c.split('\t')[3])

else:
	for val1, val2 in zip(ListOfWords, POS):
		RES.append(val2+" " + val1)
	for newValue in RES:
		if newValue in strlist:
			dic[newValue] += 1
		else:
			dic[newValue] = 1
	for posValue in POS:
		RES1.append(posValue)
	for newValue1 in RES1:
		if newValue1 in dic2:
			dic2[newValue1] += 1
		else:
			dic2[newValue1] = 1
	else:
		dic_list = dic.keys()
		dic_list1 = dic.values()
		dic_list2 = dic2.keys()
		dic_list3 = dic2.values()
		print("# P", "count", "tag", " " + "form")
		for words1,values1 in zip(dic_list2, dic_list3):
			print(values1/len(ListOfWords), values1, " " + words1.strip(), "_")
		for words, values in zip(dic_list, dic_list):
			print(values/values, values, " "+words)






