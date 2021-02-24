import json
data=json.load(open('data.json'))
from difflib import get_close_matches 


def meaning(a):
	a=a.lower()
	if a in data:
		return data[get_close_matches(a,data)[0]]
	elif a.title() in data:
		return data[a.title()]
	elif a.upper() in data:
		return data[a.upper()]
'''	elif get_close_matches(a,data.keys()) !=[]:
		print('did u mean %s ??'%get_close_matches(a,data.keys())[0])
		x=input('press y for yes ....n for no')
		if x=='y':
			return data[get_close_matches(a,data.keys())[0]]
		elif x=='n':
			return('Word doesn\'t exist.. Sorryy :)')
		else:
			return('wrong response! idk what to do... \nBye!!!')
	else:
		return('Word doesn\'t exist.. Sorryy :)')
'''
	#return a

#word=input('enter your search: ')
word='NASA'
op=meaning(word)
if type(op) is list:
	for i in op:
		print(i,'\n')
else:
	print(op)