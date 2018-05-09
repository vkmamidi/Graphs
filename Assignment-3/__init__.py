from collections import defaultdict
from collections import OrderedDict
from dfs import Graph
from vertex import Vertex

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "Connecting path doesn't exist"


def implement_bfs(nodeset):
    starting_node = 1;
    path_for_n_node = [];
    for i in range(1,11):
        if i == starting_node:
            path_for_n_node.append(i)
            print i , '\t  :\t\t' , path_for_n_node.__len__()-1, '\t\t' ,path_for_n_node
        else:
            path_for_n_node = bfs_shortest_path(nodeset,starting_node,i)
            print i, '\t  :\t\t', path_for_n_node.__len__() - 1, '\t\t', path_for_n_node
        path_for_n_node = []

def graphfunction():
    print "****************************Output for graph one*********************************\n"
    f = open('input.txt', 'r')
    node = []
    connecting_node = []
    for line in f:
        temp = line.split(" ");
        node.append(int(temp[0].strip()))
        connecting_node.append(int(temp[1].strip()))
    counter = 1
    temp = []
    nodeset = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
    while (counter <= 10):
        temp = [];
        for i in range(0, node.__len__()):
            if (node[i] == counter):
                temp.append(connecting_node[i])
        nodeset[counter] = temp
        counter += 1;
    print 'Vertex  Distance  [Path]'
    implement_bfs(nodeset)

    a = Vertex('1')
    b = Vertex('2')
    c = Vertex('3')
    d = Vertex('4')
    e = Vertex('5')
    f = Vertex('6')
    g = Vertex('7')
    h = Vertex('8')
    i = Vertex('9')
    j = Vertex('10')

    # directed graph in form of vertices for keeping track of discovery and finish time of a node.
    G = Graph(OrderedDict(
        [(a, [i, j]), (b, [e, f]), (c, [d, e]), (d, [e, h, i]), (e, [a]), (f, [j]), (g, [i]), (h, [a, b]), (i, [g]),
         (j, [c, e, g])]))
    G.DFS()
    G.classifyedges()
    G.toposort()
    print "**********************************************************************************\n\n\n\n"


def graphfunction2():
    print "****************************Output for graph two*********************************\n"
    f = open('input2.txt', 'r')
    node = []
    connecting_node = []
    for line in f:
        temp = line.split(" ");
        node.append(int(temp[0].strip()))
        connecting_node.append(int(temp[1].strip()))
    counter = 1
    temp = []
    nodeset = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
    while (counter <= 10):
        temp = [];
        for i in range(0, node.__len__()):
            if (node[i] == counter):
                temp.append(connecting_node[i])
        nodeset[counter] = temp
        counter += 1;
    print 'Vertex  Distance  [Path]'
    implement_bfs(nodeset)
    print nodeset
    a = Vertex('1')
    b = Vertex('2')
    c = Vertex('3')
    d = Vertex('4')
    e = Vertex('5')
    f = Vertex('6')
    g = Vertex('7')
    h = Vertex('8')
    i = Vertex('9')
    j = Vertex('10')

    # directed graph in form of vertices for keeping track of discovery and finish time of a node.
    G = Graph(OrderedDict(
        [(a, [h]), (b, [a, c, e]), (c, [d, i, j]), (d, [h, j]), (e, [d, j]), (f, [e, j]), (g, [i]), (h, [i]), (i, [a, b]),
         (j, [f])]))


    G.DFS()
    G.classifyedges()
    G.toposort()
    print "**********************************************************************************\n\n\n\n"


def graphfunction3():
    print "****************************Output for graph three********************************\n"
    f = open('input3.txt', 'r')
    node = []
    connecting_node = []
    for line in f:
        temp = line.split(" ");
        node.append(int(temp[0].strip()))
        connecting_node.append(int(temp[1].strip()))
    counter = 1
    temp = []
    nodeset = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
    while (counter <= 10):
        temp = [];
        for i in range(0, node.__len__()):
            if (node[i] == counter):
                temp.append(connecting_node[i])
        nodeset[counter] = temp
        counter += 1;
    print 'Vertex  Distance  [Path]'
    implement_bfs(nodeset)
    print nodeset

    a = Vertex('1')
    b = Vertex('2')
    c = Vertex('3')
    d = Vertex('4')
    e = Vertex('5')
    f = Vertex('6')
    g = Vertex('7')
    h = Vertex('8')
    i = Vertex('9')
    j = Vertex('10')

    # directed graph in form of vertices for keeping track of discovery and finish time of a node.
    G = Graph(OrderedDict(
        [(a, [h]), (b, [a, c, g]), (c, [b, f]), (d, [ b]), (e, [f]), (f, []), (g, [c, h]), (h, [c, d, i]), (i, [f, h, j]),
         (j, [a, i])]))
    G.DFS()
    G.classifyedges()
    G.toposort()
    print "**********************************************************************************\n\n\n\n"


def main():
    graphfunction();
    graphfunction2();
    graphfunction3();

if __name__ == "__main__":
    main();
