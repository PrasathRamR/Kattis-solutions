#Programmer : Prasath Ram R

string1 = input()
flag = False
for index in range(len(string1) - 1): 
	if(string1[index] == 's' and string1[index + 1] == 's'):
		print('hiss')
		flag = True
		break
if(not flag):
	print('no hiss')
