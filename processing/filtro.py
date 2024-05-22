import json
import sys 



HELP_MESSAGE = """
	Usage: ./filtrp.py <datafile> <mes inferior> <mes superior>
	mes: YYYY-MM
"""

f = open(sys.argv[1], 'r')
outfile = sys.argv[1].split('.')[0]+"_filtro.json"
g = open(outfile, 'w')


# linf = sys.argv[2]
# lsup = sys.argv[3]


anyos = ['2022','2021','2020']

l = f.readline()
while l != "":
	data = json.loads(l)
	mes = '-'.join(data['date'].split('-')[0:2])
	anyo = data['date'].split('-')[0]
	if anyo in anyos:
		g.write(l)
	l = f.readline()

f.close()
g.close()
