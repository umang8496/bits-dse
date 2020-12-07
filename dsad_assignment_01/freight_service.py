# freight_service.py

# Graph Node
class Node(object):
    city_label = None

    def __init__(self, city_label):
        self.city_label = city_label


# Graph Edge
class Edge(object):
    source = None
    target = None
    train_label = None

    def __init__(self, source, target, train_label):
        self.source = source
        self.target = target
        self.train_label = train_label

    def get_source(self):
        return self.source

    def get_target(self):
        return self.target

    def get_train_label(self):
        return self.train_label


# Custom Graph Implementation
class Graph(object):
    set_of_distinct_nodes = set()
    set_of_distinct_edges = set()
    number_of_nodes = 0
    number_of_edges = 0
    set_of_freight_trains = set()
    # adjacency_matrix = []
    adjacency_list = set()  

    def create_node(self, city):
        node = Node(city)
        self.number_of_nodes += 1
        self.set_of_distinct_nodes.add(node)
        return node
    
    def connect_nodes(self, node_A, node_B, train_id):
        edge = Edge(node_A, node_B, train_id)
        self.set_of_freight_trains.add(train_id)
        self.number_of_edges += 1
        self.set_of_distinct_edges.add(edge)

    def get_number_of_nodes(self):
        return len(self.set_of_distinct_nodes)
    
    def get_number_of_freight_trains(self):
        return len(self.set_of_freight_trains)


# Utility Functions
class Utility(object):
    input_file = None
    READ_MODE = None

    def __init__(self):
        self.input_file = "inputPS22.txt"
        self.prompt_file = "promptsPS22.txt"
        self.READ_MODE = "r"

    def read_input_file(self):
        file = open(self.input_file, self.READ_MODE)
        for line in file:
            print(line)
        file.close()

    def read_prompt_file(self):
        file = open(self.prompt_file, self.READ_MODE)
        for line in file:
            print(line)
        file.close()

    def write_output_file(self):
        pass


#####################################################################
if __name__ == "__main__":
    # utility = Utility()
    # utility.read_input_file()

    g = Graph()

    a = g.create_node("New Delhi")
    b = g.create_node("Chennai")
    train_id = "T1235"
    g.connect_nodes(a, b, train_id)
    c = g.create_node("Calcutta")
    train_id = "T2342"
    g.connect_nodes(a, c, train_id)

    p = g.create_node("Vishakhapatnam")
    q = g.create_node("Hyderabad")
    train_id = "T5623"
    g.connect_nodes(p, q, train_id)

    l = g.create_node("ahmedabad")
    m = g.create_node("Mumbai")
    n = g.create_node("nagpur")
    train_id = "T1122"
    g.connect_nodes(l, m, train_id)
    g.connect_nodes(m, n, train_id)
    g.connect_nodes(l, n, train_id)

    train_id = "T2341"
    g.connect_nodes(a, l, train_id)
    print("Number of Cities:", g.get_number_of_nodes())
    print("Number of Trains:", g.get_number_of_freight_trains())


# Challenges
# 1. For adjacency matrix the number of nodes is required in advance
# 2. Reading the input file in correct format and then performing the instructions
# 3. Creating an output file in the required format
# 4. Cannot implement adjacency list as the dictionary data structure is not allowed

