#####################################################################
# freight_service.py
#####################################################################


# Node Definition
class Node(object):
    def __init__(self, city_label):
        self.city_label = city_label
        self.set_of_associated_trains = set()
        self.set_of_connected_edges = set()
        self.visited = False

    def get_city_label(self):
        return self.city_label

    def get_set_of_associated_trains(self):
        return self.set_of_associated_trains

    def get_number_of_associated_trains(self):
        return len(self.set_of_associated_trains)

    def get_set_of_connected_edges(self):
        return self.set_of_connected_edges

    def is_visited(self):    
        return self.visited
    
    def visit_the_node(self):
        self.visited = True

    def unvisit_the_node(self):
        self.visited = False


#####################################################################


# Edge Definition
class Edge(object):
    def __init__(self, source, target, train_label):
        self.source_node = source
        self.target_node = target
        self.train_label = train_label

    def get_source(self):
        return self.source_node

    def get_target(self):
        return self.target_node

    def get_train_label(self):
        return self.train_label


#####################################################################


# Custom Graph Implementation
class Graph(object):
    list_of_distinct_nodes = list()
    list_of_distinct_cities = list()
    set_of_distinct_edges = set()
    adjacency_matrix = []

    def __init__(self, number_of_distinct_cities, list_of_trains, list_of_routes, set_of_distinct_cities):
        self.number_of_distinct_cities = number_of_distinct_cities
        self.list_of_trains = list_of_trains
        self.list_of_routes = list_of_routes
        self.set_of_distinct_cities = set_of_distinct_cities
        self.initialize_adjacenct_matrix()

    def initialize_adjacenct_matrix(self):
        self.adjacency_matrix = [[0] * self.number_of_distinct_cities for x in range(self.number_of_distinct_cities)]
        self.adjacency_matrix = self.adjacency_matrix * self.number_of_distinct_cities

    def initializeGraph(self):
        for city in self.set_of_distinct_cities:
            self.list_of_distinct_cities.append(city)
            self.list_of_distinct_nodes.append(self.create_node(city))
        print(self.list_of_distinct_cities)
        for i in range(len(self.list_of_trains)):
            train_label = self.list_of_trains[i]
            list_of_cities = self.list_of_routes[i]
            for f in range(len(list_of_cities)):
                for g in range(f, len(list_of_cities)):
                    source_city = list_of_cities[f]
                    target_city = list_of_cities[g]
                    if (source_city != target_city):
                        source_index = self.list_of_distinct_cities.index(source_city)
                        target_index = self.list_of_distinct_cities.index(target_city)
                        source_node = self.list_of_distinct_nodes[source_index]
                        target_node = self.list_of_distinct_nodes[target_index]
                        e1 = self.create_edge(source_node, target_node, train_label)
                        self.set_of_distinct_edges.add(e1)
                        e2 = self.create_edge(target_node, source_node, train_label)
                        self.set_of_distinct_edges.add(e2)
                        self.update_adjacency_matrix(source_index, target_index)
                        source_node.set_of_associated_trains.add(train_label)
                        source_node.set_of_connected_edges.add(e1)
                        target_node.set_of_associated_trains.add(train_label)
                        target_node.set_of_connected_edges.add(e2)

    def create_node(self, city_label):
        return Node(city_label)
    
    def create_edge(self, source, target, train_label):
        return Edge(source, target, train_label)

    def update_adjacency_matrix(self, index_of_source_city, index_of_target_city):
        if (index_of_source_city != index_of_target_city):
            self.adjacency_matrix[index_of_source_city][index_of_target_city] = 1
            self.adjacency_matrix[index_of_target_city][index_of_source_city] = 1
        else:
            self.adjacency_matrix[index_of_source_city][index_of_target_city] = 0

    def print_adjacency_matrix(self):
        for i in range(self.number_of_distinct_cities):
            for k in range(self.number_of_distinct_cities):
                print((self.adjacency_matrix[i][k]), end="  ")
            print()
    
    def print_edge_list(self):
        for edge in self.set_of_distinct_edges:
            print(edge.train_label,":", edge.get_source().get_city_label(),"<--->", edge.get_target().get_city_label())

    def get_adjacency_matix(self):
        return self.adjacency_matrix

    def get_nodes_with_highest_edge(self):
        list_of_number_of_connected_trains = []
        for node in self.list_of_distinct_nodes:
            list_of_number_of_connected_trains.append(node.get_number_of_associated_trains())
        max_number_of_connected_trains = max(list_of_number_of_connected_trains)
        candidate_hub = []
        for node in self.list_of_distinct_nodes:
            if(node.get_number_of_associated_trains() == max_number_of_connected_trains):
                candidate_hub.append(node)
        final_hub = []
        for node in candidate_hub:
            if(node.get_number_of_associated_trains() == max_number_of_connected_trains):
                final_hub.append(node)
        return final_hub            

    def is_city_available(self, city):
        return (city in self.list_of_distinct_cities)

    def does_direct_train_exist(self, city_a, city_b):
        city_a_index = self.list_of_distinct_cities.index(city_a)
        city_b_index = self.list_of_distinct_cities.index(city_b)
        if (self.adjacency_matrix[city_a_index][city_b_index] == 1):
            city_a_node = self.list_of_distinct_nodes[city_a_index]
            city_b_node = self.list_of_distinct_nodes[city_b_index]
            train_id = None
            for edge in city_a_node.get_set_of_connected_edges():
                if (edge.get_target() == city_b_node):
                    train_id = edge.get_train_label()
            return (True, train_id)
        else:
            return (False, None)

    def find_number_of_cities_connected_by(self, train_id):
        set_of_cities_connected_by_train = set()
        for edge in self.set_of_distinct_edges:
            if (edge.get_train_label() == train_id):
                set_of_cities_connected_by_train.add(edge.get_source().get_city_label())
                set_of_cities_connected_by_train.add(edge.get_target().get_city_label())
        return (len(set_of_cities_connected_by_train), set_of_cities_connected_by_train)

    def is_reachable(self, city_a, city_b):
        source_node_index = self.list_of_distinct_cities.index(city_a)
        source_node = self.list_of_distinct_nodes[source_node_index]

        queue= []
        source_node.visit_the_node()
        for edge in source_node.get_set_of_connected_edges():
            queue.append(edge)
        
        while (len(queue) != 0):
            edge = queue.pop()
            next_node = edge.get_target()
            if (next_node.get_city_label() == city_b):
                return True
            else:
                if (not next_node.is_visited()):
                    for e in next_node.get_set_of_connected_edges():
                        if (e.get_target().is_visited()):
                            continue
                        else:
                            queue.append(e)
                    next_node.visit_the_node()
                else:
                    continue
        return False

    def unvisit_all_nodes(self):
        for node in self.list_of_distinct_nodes:
            node.unvisit_the_node()


#####################################################################


# FileUtilities Functions
class FileUtilities(object):
    def __init__(self):
        self.READ_MODE = "r"
        self.list_of_trains = []
        self.list_of_routes = []
        self.set_of_distinct_cities = set()

    def read_input_file(self, inputfile):
        file = open(inputfile, self.READ_MODE)
        for line in file:
            entries = line.split("/")
            stripped_entries = [item.strip() for item in entries]
            self.list_of_trains.append(stripped_entries[0])
            self.list_of_routes.append(stripped_entries[1:])
            self.set_of_distinct_cities.update(set(stripped_entries[1:]))
        file.close()

    def get_number_of_distinct_cities(self):
        return len(self.set_of_distinct_cities)

    def get_set_of_distinct_cities(self):
        return self.set_of_distinct_cities

    def get_list_of_trains(self):
        return self.list_of_trains

    def get_number_of_freight_trains(self):
        return len(self.list_of_trains)

    def get_list_of_routes(self):
        return self.list_of_routes


#####################################################################


class FreightService(object):
    def __init__(self):
        self.graph = None
        self.fileUtilities = FileUtilities()

    def readCityTrainfile(self, inputfile):
        # read the input file
        self.fileUtilities.read_input_file(inputfile)
        
        # create the collections of trains and cities
        number_of_distinct_cities = self.fileUtilities.get_number_of_distinct_cities()
        list_of_trains = self.fileUtilities.get_list_of_trains()
        list_of_routes = self.fileUtilities.get_list_of_routes()
        set_of_distinct_cities = self.fileUtilities.get_set_of_distinct_cities()

        # now create the Graph object and then initialize it
        self.graph = Graph(number_of_distinct_cities, list_of_trains, list_of_routes, set_of_distinct_cities)
        self.graph.initializeGraph()
        # self.graph.print_adjacency_matrix()  # remove this function call

    def showAll(self):
        print("--------Function showAll --------")
        print("Total no. of freight trains:", self.fileUtilities.get_number_of_freight_trains())
        print("Total no. of cities:", self.fileUtilities.get_number_of_distinct_cities())
        print()
        if (self.fileUtilities.get_number_of_freight_trains() != 0) and (self.fileUtilities.get_number_of_distinct_cities() != 0):
            print("List of Freight trains:")
            for train in self.fileUtilities.get_list_of_trains():
                print(train)
            print()
            print("List of cities:")
            for city in self.fileUtilities.get_set_of_distinct_cities():
                print(city)
        print("---------------------------------------")

    def displayTransportHub(self):
        print("--------Function displayTransportHub--------")
        list_of_hubs = self.graph.get_nodes_with_highest_edge()
        for node in list_of_hubs:
            print("Main transport hub:", node.get_city_label())
            print("Number of trains visited:", node.get_number_of_associated_trains())
            print("List of Freight trains:")
            for trains in node.get_set_of_associated_trains():
                print(trains)
        print("---------------------------------------")

    def displayConnectedCities(self, train_id):
        print("--------Function displayConnectedCities--------")
        print("Freight train number:", train_id)
        if (train_id in self.graph.list_of_trains):
            connected_cities = self.graph.find_number_of_cities_connected_by(train_id)
            number_of_connected_cities = connected_cities[0]
            list_of_connected_cities = connected_cities[1]
            print("Number of cities connected:", number_of_connected_cities)
            print("List of cities connected directly by", train_id, ":")
            for cities in list_of_connected_cities:
                print(cities)
        else:
            print(train_id, "does not exist.")
        print("---------------------------------------")

    def displayDirectTrain(self, city_a, city_b):
        print("--------Function displayDirectTrain--------")
        print("City A:", city_a)
        print("City B:", city_b)

        if (city_a == city_b):
            print("Source and destination cities are same, hence no freight service is available.")
        elif (self.graph.is_city_available(city_a) and self.graph.is_city_available(city_b)):
            status_tuple = self.graph.does_direct_train_exist(city_a, city_b)
            if (status_tuple[0]):
                print("Package can be sent directly: Yes,", status_tuple[1])
            else:
                print("Package can be sent directly: No")
        else:
            if(not self.graph.is_city_available(city_a)):
                print("City", city_a, "is not available.")
            if(not self.graph.is_city_available(city_b)):
                print("City", city_b, "is not available.")
        print("---------------------------------------")

    def findServiceAvailable(self, city_a, city_b): 
        print("--------Function findServiceAvailable--------")
        print("City A:", city_a)
        print("City B:", city_b)
        
        if (self.graph.is_city_available(city_a) and self.graph.is_city_available(city_b)):
            if(city_a == city_b):
                print("No Freight Service is available.")
                print("(Source and Target cities are same)")
            elif (city_a != city_b):
                result = self.graph.is_reachable(city_a, city_b)
                if (result):
                    print("Freight Service is available.")
                else:
                    print("No Freight Service is available.")
        else:
            if(not self.graph.is_city_available(city_a)):
                print("City", city_a, "is not available.")
            if(not self.graph.is_city_available(city_b)):
                print("City", city_b, "is not available.")
        print("---------------------------------------")
        self.graph.unvisit_all_nodes()


#####################################################################
if __name__ == "__main__":
    freightService = FreightService()
    freightService.readCityTrainfile("inputPS22.txt")
    
    # freightService.showAll()
    # freightService.displayTransportHub()

    # freightService.displayDirectTrain("Mumbai", "Pune")
    # freightService.displayDirectTrain("Bangalore", "Bangalore")
    # freightService.displayDirectTrain("Mumbai", "Calcutta")
    # freightService.displayDirectTrain("Nagpur", "Chennai")
    # freightService.displayDirectTrain("Mumbai", "Ahmedabad")
    # freightService.displayDirectTrain("Ahmedabad", "New Delhi")
    # freightService.displayDirectTrain("Vishakhapatnam", "Hyderabad")
    # freightService.displayDirectTrain("New Delhi", "Chennai")
    # freightService.displayDirectTrain("Calcutta", "New Delhi")
    
    # freightService.displayConnectedCities("T1122")
    # freightService.displayConnectedCities("T0000")
    # freightService.displayConnectedCities("T1235")
    # freightService.displayConnectedCities("T3344")

    freightService.findServiceAvailable("Calcutta", "Chennai")
    freightService.findServiceAvailable("Calcutta", "Mumbai")
    # freightService.findServiceAvailable("Nagpur", "Vishakhapatnam")
    # freightService.findServiceAvailable("Chennai", "Bangalore")
    # freightService.findServiceAvailable("Bangalore", "Chennai")
    # freightService.findServiceAvailable("Bangalore", "Bangalore")


