def dfs_iter(graph, start, path=[]):
    """
    Iterative version of depth first search.
    Arguments:
        graph - a dictionary of lists that is your graph and who you're connected to.
        start - the node you wish to start at
        path - a list of already visited nodes for a path
    Returns:
        path - a list of strings that equal a valid path in the graph
    """
    q=[start]
    while q:
        v = q.pop(0)
        if v not in path:
            path += [v]
            q += graph[v]
    return path

def dfs_rec(graph, start, path=[]):
    """
    Recursive version of depth first search.
    Arguments:
        graph - a dictionary of lists that is your graph and who you're connected to.
        start - the node you wish to start at
        path - a list of already visited nodes for a path
    Returns:
        path - a list of strings that equal a valid path in the graph
    """
    path = path + [start]
    for node in graph[start]:
        if not node in path:
            path = dfs_rec(graph, node, path)
    return path




if __name__ == '__main__':
    graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
    print "Iterative DFS"
    print dfs_iter(graph, 'A')
    print "Recursive DFS"
    print dfs_rec(graph, 'A')
    
    