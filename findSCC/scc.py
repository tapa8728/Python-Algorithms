from collections import defaultdict

""" ALGORTIHM FOR FINDING THE LARGEST STRONGLY CONNECTED COMPONENT IN THE GIVEN D.A.G
1. Reverse the Graph and store in dictionary "revdic"
2. Run iterative DFS on revdic. In the iterative approach: You first insert all the elements into the stack - ang then handle the head of the stack [which is the last node inserted] - thus the first node you handle is the last son.
3. 
"""

# opening sources.txt in read mode
fobj = open("sources.txt", "r")
# to read a single line
#print fobj.readline();

# split each line and store in a list
# [['0', '0'], ['0', '1'] ......]
words = []
for line in fobj:
    words.append(line.split())

# print words

# create an orriginal dictionary for graph
dic = {}

for line in words:
	if line[0] in dic:
		dic[line[0]].append(line[1]) # append the new number to the existing array at this slot
	else:
		dic[line[0]] = [line[1]] # create a new array in this slot

# traverse the dictionary: works fine!!
# key='0'
# print key, dic[key]
# key1='1'
# print key1, dic[key1]

# create reverse dictionary for graph
revdic = {}
for line in words:
	if line[1] in revdic:
		revdic[line[1]].append(line[0]) # append the new number to the existing array at this slot
	else:
		revdic[line[1]] = [line[0]] # create a new array in this slot

#print key, revdic[key]

# Iterative DFS
path =[]
def dfs_iter(graph, start):
    """
    Iterative version of depth first search.
    Arguments:
        graph (revdic)- a dictionary of lists that is your graph and who you're connected to.
        start - the node you wish to start at
        path - a list of already visited nodes for a path
    Returns:
        path - a list of strings that equal a valid path in the graph
    """
    global path
    q=[start]
    while q:
        v = q.pop(0)
        if v not in path:
            path += [v]
            q += graph[v]
    return path

#graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
graph = {'A':['C'], 'B':['C','D'], 'C':['E'], 'D':[], 'E':[]}
print "Iterative DFS"
print dfs_iter(graph, 'A')
# path will be in decreasing order of post number
# the first vertex in path will be the source of the Reverse Graph annd hence the sink of the original graph
print "path is:", path , "of length: ", len(path)

# we have to call explore() for all the vertices which have not been visited in "path" list
# let "visited" dictionary contain all the vertices that have been visited
visited = {}
# let "SCC" dictionary contain "vx" : [v1, v2, v3 ..] that form a stongly-connected-component
SCC = {}
# initialize all the keys(vertices) of "dic" to "False"
for k, v in graph.items():
	visited[k] = "False"
print "visited (initial): ", visited

"""
explore(graph, vx)
graph: The original dictionary (dic)
vx: Pick out each vertex from "path" list and call explore on it
"""
def explore(graph, vx):
	visited[vx] = "True"
	value = graph[vx]	#get vertices to which vx is connected, "value" will be a list
	for v in value:
		if visited[v] == "False":
			#add to the SCC dictionary
			if vx in SCC:
				SCC[vx].append(v)
			else:
				SCC[vx] = v
			#call explore on v
			explore(graph, v)

# call explore() on each vertex in the "path" list that has still not been visited
for p in path:
	if visited[p] == "False":
		explore(graph, p)

# Print "visited" dictionary
print "visited (final): ", visited

# Print "SCC" dictionary
print "SCC :", SCC



