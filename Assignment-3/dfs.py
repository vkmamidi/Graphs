# Depth-First Search (DFS)

from collections import OrderedDict
from vertex import Vertex

class Graph(object):

    def __init__(self, G):
        self.G = G
        self.timestamp = 0
        self.finished = []

    def reset(self):
        self.finished = []
        self.timestamp = 0
        for v in self.G.keys():
            v.reset()

    def DFSvisit(self, s):
        self.timestamp += 1
        s.start = self.timestamp

        for v in self.G[s]:
            if v.start == None:
                v.level  = s.level + 1
                v.parent = s
                self.DFSvisit(v)

        self.timestamp += 1
        self.finished.append(s)
        s.finish = self.timestamp


    def DFS(self):
        self.reset()
        for v in self.G.keys():
            if v.start == None:
                v.level = 0
                self.DFSvisit(v)

    def classifyedges(self):
        tree = []
        cross = []
        forward = []
        backward = []
        if self.timestamp == 0:
            print "Error: need to run DFS first!"
            return
        for v in self.G.keys():
            print 'discover/finish', v, ':  ', v.start, ' ', v.finish;
        for v in self.G.keys():
            for u in self.G[v]:
                if u.parent == v:
                    tree.append([int(v.name), int(u.name)])
                elif v.start < u.start and v.finish > u.finish:
                    forward.append([int(v.name), int(u.name)])
                elif v.start > u.start and v.finish < u.finish:
                    backward.append([int(v.name), int(u.name)])
                else:
                    cross.append([int(v.name), int(u.name)])
        print 'tree edge :' , tree
        print 'forward edge :', forward
        print 'backward edge :', backward
        print 'cross edge :', cross

    def toposort(self):
        print "toposort:", " ".join([str(v) for v in reversed(self.finished)])