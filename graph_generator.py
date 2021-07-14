import sys
import random

args = list(sys.argv[1:])

def weight_chance(i, j, total):
    dist = abs(i - j)
    limit = (dist * 3 / 2) / total
    chance = random.uniform(0, 1)
    return chance > limit and dist < total / 2

def get_edge_weights(nodes):
    weights = list()
    for i in range(nodes):
        weights.append([0] * nodes)
    for i in range(nodes):
        for j in range(i, nodes):
            boolean = weight_chance(i, j, nodes)
            if i != j and boolean:
                weight = random.randint(4000, 5000) / 1000
                weights[i][j] = weight
    return weights

def write_graph(name, graph, nodes):
    lines = []
    lines.append(str(nodes))
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            weight = graph[i][j]
            if weight > 0:
                lines.append('\n' + str(i) + ' ' + str(j) + ' ' + str(weight))
    f = open(name, 'w')
    f.writelines(lines)
    f.close()

nodes = int(args[1])

graph = get_edge_weights(nodes)

write_graph(args[0], graph, nodes)

