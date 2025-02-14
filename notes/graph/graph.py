from abc import abstractmethod


class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        # self.adj_list = {node:[] for node in self.nodes}
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def degree(self,node):
        '''
        Return the degree of a node
        Degree = number of edges  connected to the node
        '''
        return len(self.adj_list[node])

    def print_adj_list(self):
        for node in self.nodes:
            print(f'{node} -> {self.adj_list[node]}')

class GraphAbstract:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []

    @abstractmethod
    def add_edge(self, u, v):
        pass

    def degree(self, node):
        return len(self.adj_list[node])
    
    def display(self):
        for node in self.nodes:
            print(f'{node} -> {self.adj_list[node]}')

class UndirectedGraph(GraphAbstract):
    def __init__(self, Nodes):
        super().__init__(Nodes)
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)


class DirectedGraph(GraphAbstract):
    def  _init__(self, Nodes):
        super().__init__(Nodes)

    def add_edge(self, u, v):
        try:
        # directed graphs have only one edge in a direction
            self.adj_list[u].append(v)
        except KeyError:
            print(f"Node {u} does not exist")

def main():
    # print('Hello World')

    nodes = ['A', 'B', 'C', 'D', 'E']
    # declare all edges
    all_edges = [
        ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')
    ]

    graph = Graph(nodes)
    print('Just created a graph')
    graph.print_adj_list()

    # graph.add_edge('A', 'B')
    # print('\nAdded an edge between A and B')
    # graph.print_adj_list()

    # better way to add all edges using `loop`
    for edge in all_edges:
        graph.add_edge(u=edge[0], v=edge[1])

    print('\nAdded all edges')
    graph.print_adj_list()

    print('\nDegree of node A:', graph.degree('A'))
    print('Degree of node D:', graph.degree('D'))

def use_directed_graph():
    nodes = ['A', 'B', 'C', 'D', 'E']
    # declare all edges
    all_edges = [
        ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')
    ]

    graph = DirectedGraph(nodes)

    for u,v in all_edges:
        graph.add_edge(u, v)

    graph.display()

    print(f"Degree of C: {graph.degree('C')}")

if __name__ == '__main__':
    # main()
    use_directed_graph()