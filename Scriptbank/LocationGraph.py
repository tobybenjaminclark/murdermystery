
class LocationGraph():

    def __init__(self):

        # Initialize graph dictionary
        self.connections = {}

    def addNode(self, node):

        # Adds node to the graph with no connections
        self.connections.update({node:[]})

    def removeNode(self, node):

        # Removes Node from all connections
        for key in self.connections:
            item = self.connections[key]
            if node in item:
                item.remove(node)
            else:
                continue
        
        # Removes the Node from the graph
        self.connections.pop(node)
    
    def addEdge(self, node1, node2):

        # Adds edge NodeA -> NodeB
        current_connections = self.connections[node1]
        
        if node2 not in current_connections:
            current_connections.append(node2)
        else:
            pass

        self.connections[node1] = current_connections

        # Adds edge NodeB -> NodeA
        current_connections = self.connections[node2]
        if node1 not in current_connections:
            current_connections.append(node1)
        else:
            pass
        self.connections[node2] = current_connections
        

    def removeEdge(self, node1, node2):

        # Removes edge NodeA -> NodeB
        current_connections = self.connections[node1]
        if node2 in current_connections:
            current_connections.remove(node2)
            self.connections[node1] = current_connections

        # Removes Edge NodeB -> NodeA
        current_connections = self.connections[node2]
        if node1 in current_connections:
            current_connections.remove(node1)
            self.connections[node2] = current_connections
    
    
    def showGraph(self):

        # Iterates through to show connections
        for key in self.connections:
            item = self.connections[key]
            print("[",key,"] : ",item)

    def returnConnections(self, node):
        item = self.connections[node]
        return item
