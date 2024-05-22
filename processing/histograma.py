import json
import matplotlib.pyplot as plt
import sys 




filename = sys.argv[1]

f = open(filename, "r")

# get the tweet for eac line in json file
fechas = {}
rets = {}
l = f.readline()
while l != "":
    data = json.loads(l)
#    fecha = "".join(str(data["date"]).split("-")[0:2])
    fecha = '-'.join(str(data["date"]).split("-")[0:2])
    if fecha in fechas:
        fechas[fecha] += 1
    else:
        fechas[fecha] = 1
    if fecha in rets:
        rets[fecha] += data["retweetCount"]
    else:
        rets[fecha] = data["retweetCount"]
    l = f.readline()


print(fechas)

# set x labels in vertical
plt.xticks(rotation=90)
plt.yscale("log")
plt.plot(list(fechas.keys())[::-1], list(fechas.values())[::-1])
plt.plot(list(rets.keys())[::-1], list(rets.values())[::-1])
plt.show()
