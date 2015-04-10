# Python-Algorithms
Programs for Algos CSCI-5454  

### Fibonacci
The text spends a lot of time talking about fib(200). Compute this number exactly using Python. Submit your code listing along with the value of fib(200), on paper.

### Modular Exponentiation
One of the largest naturally-occurring integer constants we know of is M=808017424794512875886459904961710757005754368000000000. This is the size of an object of mathematics that is just there (humans didn't invent it). 
Just for fun, compute MMmod22015. Use a computer for this one; include source code with your solution.

### Next Prime
write a python program that computes the average distance from a random 100-digit integer to the nextprime after it. Use 1 thousand samples to obtain your average. In other words, define a function getrand100() that generates random 100-digit random positive integers and let s=getrand100(); then compute the average value of nextprime(s)-s using 1000 samples. Include source code with your answer.

### chain of words
A chain of words is a list of words where the i-th word is the (i-1)st word with one extra character and some mixing of letters. For example, AN, TAN, RANT, TRAIN, RETINA, NASTIER is a chain of length 6. Find the longest chain you can in our wordlist.

In order to do this, first build a dag. The dag will consist of a node for each word (you might want to collapse words into a single node when it makes sense to), and an edge from word x to word y if y can follow x in a chain. Then run DFS from each source node in the dag and keep track of the maximum depth you reach. Print out an example chain that has maximum length (there will be a TON... just give one chain).

Please hand in your source code along with the longest chain your code found.

### Find the largest SCC
Consider the digraph given by this graph where each line of the file indicates an edge. There are 77,360 nodes and 905,468 directed edges. What is the number of nodes in the largest SCC? What is the number of edges in the largest SCC? Include your code with your answer.
