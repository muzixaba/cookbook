# Dijkstra's Algorithm
# Works well to measure the shortest distance from one to another in a graph
graph = {} # initialise graph
graph['start'] = {} # initialise start node
graph['start']['a'] = 6 # from node 'start' to node 'a' there's a weight of 6
graph['start']['b'] = 2

# initialise node 'a' plus its neighbours
graph['a'] = {}
graph['a']['fin'] = 1

# initialise node 'b' plus its neighbours
graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['fin'] = 5

# init the last node
graph['fin'] = dict()

# design a costs table
infinity = float('inf')
costs = dict()
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# Hash table for parents
parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# An array to keep track of processed nodes
processed = list()

# find lowest cost node
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Execute algorithm
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


print(f"costs: {costs}")
print(f"processed: {processed}")
