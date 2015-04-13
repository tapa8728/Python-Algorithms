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
time=0
starttime = {}
endtime = {}

def previsit(v):
	global time
	time = time + 1
	starttime[v] = time

def postvisit(v):
	global time
	time = time + 1
	endtime[v] = time

# Iterative DFS

def dfs_iter(Graph, start):
	parent=[]
	#mark start node as visted
	dfs_visited[start] = "True"
	stack = [start]
	while stack:
		v = stack.pop()
		print "popped :::: ", v
		if v not in starttime:
			previsit(v)
       	# check if v is legitimate parent (unvisited children)
		parent_check=0 # will be 1 if parent is legitimate
		for child in graph[v]:
   			if dfs_visited[child] == "False":
   				stack.append(child)		# add un-visited nodes in stack
   				parent_check=1
   		print "Stack is ::", stack
		#if parent legit add it to parent stack
		if parent_check==1:
			parent.append(v)
		print "Parent is ::", parent

   		# check if v is dead-end
   		# no children
   		# not a parent node
   		child_done=0
   		if parent_check==0:
   			postvisit(v)
   			while parent:
   				p=parent.pop()
	   			#check if all children are visited
		   		for child in graph[p]:
		   			if dfs_visited[child]=="True":	#all children visited
		   				child_done=1
		   			else:
		   				child_done=0
		   				break;	# parent still has unvisited children

			   		if child_done == 1: 
			   			postvisit(p)
			   		elif child_done == 0:	# parent still has unvisited children
			   			parent.append(p)
			   			break	#add it back
	print "Stack is over now what to do"


graph = {'A':['B','D'],'B':['C'],'C':[],'D':['A']}
#graph = {'A':['C'], 'B':['C','D'], 'C':['E'], 'D':[], 'E':[]}
print "Iterative DFS"

dfs_visited={}
for k, v in graph.items():
	dfs_visited[k]= "False"


dfs_iter(graph, 'A')
for k, v in graph.items():
	#global dfs_visited
	"""if dfs_visited[k] == "False":
		print k, "*******: ", dfs_iter(graph, k)"""

print "dfs_visited :", dfs_visited
print "previsit :", starttime
print "postvisit :", endtime

"""
# we have to call explore() for all the vertices which have not been visited in "path" list
# let "visited" dictionary contain all the vertices that have been visited
visited = {}
# let "SCC" dictionary contain "vx" : [v1, v2, v3 ..] that form a stongly-connected-component
SCC = {}
# initialize all the keys(vertices) of "dic" to "False"
for k, v in dic.items():
	visited[k] = "False"
print "visited (initial): ", visited


explore(graph, vx)
graph: The original dictionary (dic)
vx: Pick out each vertex from "path" list and call explore on it

def explore(graph, vx):
	visited[vx] = "True"
	q=[vx]
	while q:
		v = q.pop(0)
		if visited[v] == "False":
			#add to the SCC dictionary
			if v in SCC:
				SCC[vx].append(v)
			else:
				SCC[vx] = v
			# add the vertices of "v" to queue
			q += graph[v]

# call explore() on each vertex in the "path" list that has still not been visited
for p in path:
	if visited[p] == "False":
		explore(graph, p)

# Print "visited" dictionary
print "visited (final): ", visited

# Print "SCC" dictionary
print "SCC :", SCC

# Count how many nodes each SCC has 
key_values_list = []
for key in SCC:
    key_name = ''
    num = 0 
    for item in SCC[key]:
        num +=1
    key_values_list.append((key,num))

for  k,v in key_values_list:
    print k,v

"""

