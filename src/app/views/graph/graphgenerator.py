from QGraphViz.QGraphViz import QGraphViz
from QGraphViz.DotParser import Graph
from QGraphViz.Engines import Dot

class GraphGenerator(object):
    def __init__(self): 
        self.setup()

    def setup(self):
        self.avlbIndex = 0
        self.nodes = dict()
        self.qgv = QGraphViz(node_invoked_callback=self.nodeInvoked)
        self.qgv.new(Dot(Graph("Main_Graph")))

    def addNode(self, name, label=(False, None)):
        if name == None: 
            name = "Node" + self.avlbIndex
            self.avlbIndex += 1
        
        lbl = None
        if label[0]:
            if label[1] == None:  
                lbl = "N" + self.avlbIndex
            else: 
                lbl = label[1]
        
        node = self.qgv.addNode(self.qgv.engine.graph, name, label=lbl)
        self.nodes[name] = node

    def addEdge(self, source, dest): 
        if source in self.nodes: 
            srcNode = self.nodes[source]
        else: 
            raise Exception("No such node exists")

        if dest in self.nodes: 
            dstNode = self.nodes[dest]
        else: 
            raise Exception("No such node exists")

        self.qgv.addEdge(srcNode, dstNode, {})

    def build(self):
        self.qgv.build()

    def save(self, name):
        filename = name + ".gv"
        self.qgv.save(filename)

    def getGraph(self): 
        return self.qgv 

    def nodeInvoked(self, node): 
        print(node)
