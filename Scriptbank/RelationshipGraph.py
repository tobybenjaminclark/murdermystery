
class RelationshipGraph():

    def __init__(self):

        # Initialize graph dictionary
        self.connections = {}

    def addNode(self, node):

        # Adds node to the graph with no connections
        self.connections.update({node:[]})

    def removeNode(self, node):
        
        # Removes the Node from all connections
        for key in self.connections:
            node_connections = self.connections[key]
            for tup in node_connections:
                if tup[0] == node:
                    node_connections.remove(tup)
                else:
                    pass
            self.connections[key] = node_connections
        
        # Removes the Node from the graph
        self.connections.pop(node)
    
    def addEdge(self, node1, node2, type):

        # Adds edge NodeA -> NodeB (Type)
        current_connections = self.connections[node1]
        tup = (node2, type)
        current_connections.append(tup)
        self.connections[node1] = current_connections
        
    def removeEdge(self, node1, node2):

        # Removes edge NodeA -> NodeB
        current_connections = self.connections[node1]

        #[(Person1, Father),(Person2, Friend)]

        for connect in current_connections:
            if connect[0] == node2:
                current_connections.remove(connect)

    def showGraph(self):

        # Iterates through to show connections
        for key in self.connections:
            item = self.connections[key]
            print("[",key,"] : ",item)