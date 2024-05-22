import json
import sys 



anos = ['2022','2021']
f = open(sys.argv[1],'r')
total = 0
l = f.readline()
while l != "":
	data = json.loads(l)
	if int(data['retweetCount']) > 2 :
		total += 1
#		total += int(data['retweetCount'])
	l = f.readline()
print(total)
