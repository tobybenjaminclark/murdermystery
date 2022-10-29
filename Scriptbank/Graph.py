
class LocationGraph():

    def __init__(self):
        self.connections = {}

    def addNode(self, node):
        self.connections.update(node,[])

    def removeNode(self, node):
        self.connections.pop(node)
        for key, item in self.connections:
            if node in item:
                item.remove(node)
            else:
                continue

    def addEdge(self, node1, node2):
        self.connections.update(node1:node2)

    def removeEdge(self, node1, node2):
        pass

class LocationNode():

    def __init__(self, data = None):
        pass

# connections = {
# node1: [node2, node3],
# node2: [node1, node5],
# node3: [node1],
# node4: [],
# node5: [node2]
# }
