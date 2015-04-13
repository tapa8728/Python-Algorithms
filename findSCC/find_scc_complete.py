from collections import defaultdict
import cPickle as pickle


# Original graph
G = defaultdict(list)
# reverse graph
GR = defaultdict(list)

# functon to create the graph
lst = [] 	
#the source file loaded into f
f =  open("source.txt","r")

for line in f:
	left, right = line.strip().split()
	lst.append(left)
	lst.append(right)
	G[left].append(right)
	GR[right].append(left)

total_nodes = list(set(lst))
left_nodes = G.keys()
side_left = list(set(total_nodes) - set(left_nodes))

for vx in side_left:
	G[vx] = []	

side_right = GR.keys()
side_right = list(set(total_nodes) - set(right_nodes))

for vx in right_diff:
	GR[vx] = []		
print "keys :: ", len(G.keys()), len(GR.keys())
	
"""
#create reverse graph 
GR = defaultdict(list)
for e in G.keys():
	GR[e] = []

for k, v in G.items():
	for e in v:
             GR[e].append(k)

print "GR :: ", GR
"""

starttime = {}
endtime = {}
time = 0
visited = {}

max_lst_lst = []
temp_lst = [] 

def previsit(v):
	global time
	time = time + 1
	starttime[v] = time

def postvisit(v):
	global time
	time = time + 1
	endtime[v] = time
	#print "node, time :: ", v, time
	#print "parent stack :: ", parent_stack

def explore(graph, s):
    temp_lst = [] 
    stack = []
    stack.append(s)
    parent_stack = [] 


    while(len(stack)>0):
		#print "stack :: ", stack
		v = stack.pop()
		temp_lst.append(v)
        previsit(v)

        if(not visited[v]):
            visited[v] = True
 
	    unmarked_children = False
        # check all the children of graph v
        for w in graph[v]:
            	if(not visited[w] and w not in stack):
                	stack.append(w)
					unmarked_children = True
	    # there are some children left to be visited
	    if unmarked_children == True:
		   	parent_stack.append(v)
	    else:	#all children have been visited
	    	postvisit(v)
		
		#go to parent stack
		#if the node is a dead-end with no children or all visited children
		while (parent_stack):
			p = parent_stack.pop()
			marked = True
			for u in graph[p]:
				if (visited[u] == False):   #if even single child is left, no postvisit
					marked = False 
			# all the children of parents have been visited
			if marked == True:
				postvisit(p)
			else:
				parent_stack.append(p)
				break
	#empty parent stack 
    max_lst_lst.append(temp_lst)
    print "end of explore"
		
# call explore on all the vertices of the graph	
def dfs(graph):
	for vx in graph:
		visited[vx] = False
	
	for vx in graph:
		if visited[vx] == False:
			explore(graph,vx)
		print "vertex done is - ", vx


#call dfs on GR to get sorted end time array of sources in GR/ sinks in G
dfs(GR) 


#topological sort 
import operator
sorted_x = sorted(endtime.items(), key=operator.itemgetter(1), reverse=True)

print "original sorted x" , sorted_x

# call dfs on original unreversed G in order of sorted vertices
def dfs_iterative(graph):
	for vx in graph:
		visited[vx] = False
	
	for k in sorted_x:
		vx = k[0]
		if visited[vx] == False:
			explore(graph,vx)
		print "processed vertex :: ", vx

dfs(G)

#finding max scc 
max_lst = [] 
max_count = 0 

#print "max lst lst :: ", max_lst_lst
for scc in max_lst_lst:
	len_scc = len(scc)
	if len_scc > max_count:
		max_count = len_scc
		max_lst = scc

print "Length of longest SCC will be :: ", max_lst, max_count

#counting edges 
num_edges = 0 
for u in max_lst:
	for w in G[u]:
		if w in max_lst:
			num_edges += 1 	

print "The mavimum number of edges :: ", num_edges
