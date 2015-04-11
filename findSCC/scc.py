from collections import defaultdict

# opening sources.txt in read mode
fobj = open("small.txt", "r")
# to read a single line
#print fobj.readline();

# split each line and store in a list
# [['0', '0'], ['0', '1'] ......]
words = []
for line in fobj:
    words.append(line.split())

#print words

# create a dictionary for graph
dic = {}

for line in words:
	if line[0] in dic:
		dic[line[0]].append(line[1]) # append the new number to the existing array at this slot
	else:
		dic[line[0]] = [line[1]] # create a new array in this slot

# traverse the dictionary: works fine!!
key='0'
print key, dic[key]
key1='1'
print key1, dic[key1]

# create reverse dictionary for graph
revdic = {}
for line in words:
	if line[1] in revdic:
		revdic[line[1]].append(line[0]) # append the new number to the existing array at this slot
	else:
		revdic[line[1]] = [line[0]] # create a new array in this slot
print key, revdic[key]
