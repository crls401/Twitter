import json
from sys import argv



f = open(argv[1],'r')
g = open(argv[1]+'.csv','w')
l = f.readline()
headers = []
while l != "":
	data = json.loads(l)
	if headers == [] :
		headers = list(data.keys());
		g.write(';'.join(headers) + '\n')
	for d in data.values():
		if d != list(data.values())[0]:
			g.write(';')
		d = str(d)
		d = d.replace('\n','').replace(';',':')
		g.write("'"+str(d)+"'")
	g.write('\n')
	
	l = f.readline()
