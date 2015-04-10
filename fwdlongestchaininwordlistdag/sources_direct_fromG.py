#A:dictionary G:graph D:list of alphagrams
#I think this works
import cPickle as pickle
import copy 

#loading DAG into memory 
with open('graph.txt', 'rb') as f:
  G = pickle.load(f)

f.close()

#G = {"v1":["v2","v3"],"v2":[],"v3":["v2"]}
#G = {"v1":["v2","v7"],"v2":[],"v3":["v2","v4"], "v4":["v5"], "v5":[], "v6":["v5","v7"], "v7":[]}
#G = {"v1":["v2","v4"], "v2":["v3"],"v3":["v4"], "v4":[]}


temp = {}

print "len of graph ::", len(G.keys())
for key,value in G.iteritems():
	for vx in value: 
		temp[vx] = False 

non_source_lst = temp.keys()

print "len non source lst :: ", len(non_source_lst)

full_lst = G.keys()

source_lst = list(set(full_lst) - set(non_source_lst))

print "source :: ", len(source_lst)


with open('sources_direct.txt', 'wb') as f:
  pickle.dump(source_lst, f)

f.close()


