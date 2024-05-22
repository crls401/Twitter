import json
import sys 


HEAD_node = "nodedef> name VARCHAR, label VARCHAR"
HEAD_edge = "edgedef> node1 VARCHAR, node2 VARCHAR, weight INTEGER, directed BOOLEAN"

output = open("grafo.gdf", "w")
relations = open(sys.argv[1], "r")

relaciones = {} # format {(user1, user2): weight}
users = {} # format {user: label}

l = relations.readline()
while l != "":
    data = json.loads(l)
    user1 = data["user"].split("/")[-1]

    if user1 not in users:
        users[user1] = user1

    for user2 in data["following"]:
        if user2 not in users:
            users[user2] = user2
        if (user1, user2) not in relaciones:
            relaciones[(user1, user2)] = 1
        else:
            relaciones[(user1, user2)] += 1
    l = relations.readline()

output.write(HEAD_node + "\n")
# write nodes
for user in users:
    output.write(user + ", " + users[user] + "\n")

# write edges
output.write(HEAD_edge + "\n")
for relation in relaciones:
    output.write(relation[0] + ", " + relation[1] + ", " + str(relaciones[relation]) + ", " + "true" + "\n")

output.close()

