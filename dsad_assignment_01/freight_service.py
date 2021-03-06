#####################################################################
# freight_service.py
#####################################################################


# Node Definition
class Node(object):
    def __init__(self, city_label):
        self.city_label = city_label
        self.set_of_associated_trains = set()
        self.set_of_connected_edges = set()

    def get_city_label(self):
        return self.city_label

    def get_set_of_associated_trains(self):
        return self.set_of_associated_trains

    def get_number_of_associated_trains(self):
        return len(self.set_of_associated_trains)

    def get_set_of_connected_edges(self):
        return self.set_of_connected_edges


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
        self.adjacency_matrix = [[0] * self.number_of_distinct_cities for _ in range(self.number_of_distinct_cities)]

    def initializeGraph(self):
        for city in self.set_of_distinct_cities:
            self.list_of_distinct_cities.append(city)
            self.list_of_distinct_nodes.append(self.create_node(city))
        # print(self.list_of_distinct_cities)    # uncomment while debugging
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

    # method for printing the adjacency matrix
    def print_adjacency_matrix(self):
        for i in range(self.number_of_distinct_cities):
            for k in range(self.number_of_distinct_cities):
                print((self.adjacency_matrix[i][k]), end="  ")
            print()

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

    def copy_adjacency_matrix(self):
        temp = [[0] * self.number_of_distinct_cities for _ in range(self.number_of_distinct_cities)]
        for i in range(self.number_of_distinct_cities):
            for k in range(self.number_of_distinct_cities):
                temp[i][k] = self.adjacency_matrix[i][k]
        return temp
    
    def is_reachable(self, city_a, city_b):
        temp_adjacency_matrix = self.copy_adjacency_matrix()
        source_node_index = self.list_of_distinct_cities.index(city_a)
        target_node_index = self.list_of_distinct_cities.index(city_b)
        self.visited_node_list = [0 for _ in range(self.number_of_distinct_cities)]
        for _ in range(len(temp_adjacency_matrix[0])):
            self.path = [source_node_index]
            self.is_connected(source_node_index, target_node_index, temp_adjacency_matrix, self.path)
            if (self.path[-1] == target_node_index):
                return (True, self.path)
        if (self.path[-1] != target_node_index):
            return (False, self.path)

    def is_connected(self, source_node_index, target_node_index, temp_adjacency_matrix, path):
        self.visited_node_list[source_node_index] = 1
        lm = temp_adjacency_matrix[source_node_index][target_node_index]
        if (lm == 1):
            self.path.append(target_node_index)
            return(target_node_index)
        else:
            for i in range(len(temp_adjacency_matrix[0])):
                if (temp_adjacency_matrix[source_node_index][i] == 1):
                    if (self.visited_node_list[i] == 0):
                        temp_adjacency_matrix[source_node_index][i] = 0
                        temp_adjacency_matrix[i][source_node_index] = 0
                        mp = self.path[-1]
                        self.path.append(i)
                        result = self.is_connected(i, target_node_index, temp_adjacency_matrix, self.path)
                        if (result == target_node_index):
                            return(result)                
                        while(self.path[-1] != mp):
                            self.path.pop()
                    else:
                        temp_adjacency_matrix[source_node_index][i] = 0
                        temp_adjacency_matrix[i][source_node_index] = 0

    def get_node_for_index(self, i):
        return self.list_of_distinct_nodes[i]

    def get_train_number_for(self, src, des):
        all_edges_for_src = src.get_set_of_connected_edges()
        for edge in all_edges_for_src:
            train_number = edge.get_train_label()
            if (edge.get_target().get_city_label() == des.get_city_label()):
                return train_number


#####################################################################


# InputFileProcessor
class InputFileProcessor(object):
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


# FreightService
class FreightService(object):
    def __init__(self, o_file):
        self.graph = None
        self.fileProcessor = InputFileProcessor()
        self.fw = o_file

    def readCityTrainfile(self, inputfile):
        # read the input file
        self.fileProcessor.read_input_file(inputfile)
        # create the collections of trains and cities
        number_of_distinct_cities = self.fileProcessor.get_number_of_distinct_cities()
        list_of_trains = self.fileProcessor.get_list_of_trains()
        list_of_routes = self.fileProcessor.get_list_of_routes()
        set_of_distinct_cities = self.fileProcessor.get_set_of_distinct_cities()
        # now create the Graph object and then initialize it
        self.graph = Graph(number_of_distinct_cities, list_of_trains, list_of_routes, set_of_distinct_cities)
        self.graph.initializeGraph()
        # self.graph.print_adjacency_matrix()  # uncomment while debugging

    def showAll(self):
        # print("--------Function showAll--------")
        self.fw.write("--------Function showAll--------" + str("\n"))
        # print("Total no. of freight trains:", self.fileProcessor.get_number_of_freight_trains())
        self.fw.write("Total no. of freight trains: " + str(self.fileProcessor.get_number_of_freight_trains()) + str("\n"))
        # print("Total no. of cities:", self.fileProcessor.get_number_of_distinct_cities())
        self.fw.write("Total no. of cities: " + str(self.fileProcessor.get_number_of_distinct_cities()) + str("\n"))
        # print()
        self.fw.write(str("\n"))
        if (self.fileProcessor.get_number_of_freight_trains() != 0) and (self.fileProcessor.get_number_of_distinct_cities() != 0):
            # print("List of Freight trains:")
            self.fw.write("List of Freight trains: " + str("\n"))
            for train in self.fileProcessor.get_list_of_trains():
                # print(train)
                self.fw.write(train + str("\n"))
            # print()
            self.fw.write(str("\n"))
            # print("List of cities:")
            self.fw.write("List of cities: " + str("\n"))
            for city in self.fileProcessor.get_set_of_distinct_cities():
                # print(city)
                self.fw.write(city + str("\n"))
        # print("---------------------------------------")
        self.fw.write("---------------------------------------" + str("\n"))
        self.fw.write(str("\n"))

    def displayTransportHub(self):
        # print("--------Function displayTransportHub--------")
        self.fw.write("--------Function displayTransportHub--------" + str("\n"))
        list_of_hubs = self.graph.get_nodes_with_highest_edge()
        for node in list_of_hubs:
            # print("Main transport hub:", node.get_city_label())
            self.fw.write("Main transport hub: " + str(node.get_city_label()) + str("\n"))
            # print("Number of trains visited:", node.get_number_of_associated_trains())
            self.fw.write("Number of trains visited: " + str(node.get_number_of_associated_trains()) + str("\n"))
            # print("List of Freight trains:")
            self.fw.write("List of Freight trains: " + str("\n"))
            for trains in node.get_set_of_associated_trains():
                # print(trains)
                self.fw.write(trains + str("\n"))
        # print("---------------------------------------")
        self.fw.write("---------------------------------------" + str("\n"))
        self.fw.write(str("\n"))

    def displayConnectedCities(self, train_id):
        # print("--------Function displayConnectedCities--------")
        self.fw.write("--------Function displayConnectedCities--------" + str("\n"))
        # print("Freight train number:", train_id)
        self.fw.write("Freight train number: " + str(train_id) + str("\n"))
        if (train_id in self.graph.list_of_trains):
            connected_cities = self.graph.find_number_of_cities_connected_by(train_id)
            number_of_connected_cities = connected_cities[0]
            list_of_connected_cities = connected_cities[1]
            # print("Number of cities connected:", number_of_connected_cities)
            self.fw.write("Number of cities connected: " + str(number_of_connected_cities) + str("\n"))
            # print("List of cities connected directly by", train_id, ":")
            self.fw.write("List of cities connected directly by " + str(train_id) + " : " + str("\n"))
            for cities in list_of_connected_cities:
                # print(cities)
                self.fw.write(cities + str("\n"))
        else:
            # print(train_id, "does not exist.")
            self.fw.write(train_id + str(" does not exist.") + str("\n"))
        # print("---------------------------------------")
        self.fw.write("---------------------------------------" + str("\n"))
        self.fw.write(str("\n"))

    def displayDirectTrain(self, city_a, city_b):
        # print("--------Function displayDirectTrain--------")
        self.fw.write("--------Function displayDirectTrain--------" + str("\n"))
        # print("City A:", city_a)
        self.fw.write("City A: " + str(city_a) + str("\n"))
        # print("City B:", city_b)
        self.fw.write("City B: " + str(city_b) + str("\n"))
        if (city_a == city_b):
            # print("Source and destination cities are same, hence no freight service is available.")
            self.fw.write("Source and destination cities are same, hence no freight service is available." + str("\n"))
        elif (self.graph.is_city_available(city_a) and self.graph.is_city_available(city_b)):
            status_tuple = self.graph.does_direct_train_exist(city_a, city_b)
            if (status_tuple[0]):
                # print("Package can be sent directly: Yes,", status_tuple[1])
                self.fw.write("Package can be sent directly: Yes, " + str(status_tuple[1]) + str("\n"))
            else:
                # print("Package can be sent directly: No")
                self.fw.write("Package can be sent directly: No" + str("\n"))
        else:
            if(not self.graph.is_city_available(city_a)):
                # print("City", city_a, "is not available.")
                self.fw.write("City " + str(city_a) + " is not available, hence no freight service is available." + str("\n"))
            if(not self.graph.is_city_available(city_b)):
                # print("City", city_b, "is not available.")
                self.fw.write("City " + str(city_b) + " is not available, hence no freight service is available." + str("\n"))
        # print("---------------------------------------")
        self.fw.write("---------------------------------------" + str("\n"))
        self.fw.write(str("\n"))

    def findServiceAvailable(self, city_a, city_b): 
        # print("--------Function findServiceAvailable--------")
        self.fw.write("--------Function findServiceAvailable--------" + str("\n"))
        # print("City A:", city_a)
        self.fw.write("City A: " + str(city_a) + str("\n"))
        # print("City B:", city_b)
        self.fw.write("City B: " + str(city_b) + str("\n"))
        if (self.graph.is_city_available(city_a) and self.graph.is_city_available(city_b)):
            if(city_a == city_b):
                # print("Freight Service is not available.")
                self.fw.write("Freight Service is not available." + str("\n"))
                # print("(Source and Target cities are same)")
                self.fw.write("(Source and Target cities are same)" + str("\n"))
            elif (city_a != city_b):
                (result, path) = self.graph.is_reachable(city_a, city_b)
                if (result):
                    # print("Can the package be sent: Yes, ", end=" ")
                    self.fw.write("Can the package be sent: Yes, ")
                    self.print_the_path(path)
                else:
                    # print("Can the package be sent: No, Freight Service is not available.")
                    self.fw.write("Can the package be sent: No, Freight Service is not available." + str("\n"))
        else:
            if(not self.graph.is_city_available(city_a)):
                # print("City", city_a, "is not available.")
                self.fw.write("City " + str(city_a) + " is not available." + str("\n"))
            if(not self.graph.is_city_available(city_b)):
                # print("City", city_b, "is not available.")
                self.fw.write("City " + str(city_b) + " is not available." + str("\n"))
        # print("---------------------------------------")
        self.fw.write("---------------------------------------" + str("\n"))
        self.fw.write(str("\n"))

    def print_the_path(self, node_index):
        connected_nodes = []
        for n in node_index:
            connected_nodes.append(self.graph.get_node_for_index(n))
        printable_path = []
        printable_path.append(connected_nodes[0].get_city_label())
        for f in range(1, len(connected_nodes)):
            src = connected_nodes[f-1]
            des = connected_nodes[f]
            train_number = self.graph.get_train_number_for(src, des)
            printable_path.append(train_number)
            printable_path.append(des.get_city_label())
        for f in printable_path:
            # print(f, end=" ")
            self.fw.write(str(f))
            if (f != printable_path[-1]):
                # print(">", end=" ")
                self.fw.write(" > ")
        # print()
        self.fw.write(str("\n"))


#####################################################################
if __name__ == "__main__":
    # Read the prompts file for processing the further instructions
    promptsfile = "promptsPS22.txt"
    outputfile = "outputPS22.txt"
    inputfile = "inputPS22.txt"
    p_file = None
    o_file = None
    SEARCH_TRANSPORT_HUB = "searchTransportHub"
    SEARCH_TRAIN = "searchTrain"
    SEARCH_CITIES = "searchCities"
    SERVICE_AVAILABILITY = "ServiceAvailability"
    try:
        p_file = open(promptsfile, "r")
        o_file = open(outputfile, "w")
        if (p_file != None) and (o_file != None):
            freightService = FreightService(o_file)
            # read the input file and create the graph
            freightService.readCityTrainfile(inputfile)
            # write the summary details of the entire graph
            freightService.showAll()
            for line in p_file:
                entries = line.split(":")
                normalized_entries = [values.strip(" ").strip(":").strip("\n") for values in entries]
                if (normalized_entries[0] == SEARCH_TRANSPORT_HUB):
                    freightService.displayTransportHub()
                elif (normalized_entries[0] == SEARCH_TRAIN):
                    freightService.displayConnectedCities(normalized_entries[1])
                elif (normalized_entries[0] == SEARCH_CITIES):
                    freightService.displayDirectTrain(normalized_entries[1], normalized_entries[2])
                elif (normalized_entries[0] == SERVICE_AVAILABILITY):
                    freightService.findServiceAvailable(normalized_entries[1], normalized_entries[2])
                else:
                    print("Unidentified Instruction Found :", normalized_entries[0])
            o_file.close()
            p_file.close()
        else:
            print("Unable to read the prompt file.")
    except FileNotFoundError:
        print("Prompt File:", promptsfile, "is not found.")


    # freightService = FreightService()
    # Following function calls are meant for testing purpose
    #
    # freightService.readCityTrainfile("inputPS22.txt")
    # freightService.showAll()
    # freightService.displayTransportHub()
    #
    # freightService.displayDirectTrain("Mumbai", "Pune")
    # freightService.displayDirectTrain("Bangalore", "Bangalore")
    # freightService.displayDirectTrain("Mumbai", "Calcutta")
    # freightService.displayDirectTrain("Nagpur", "Chennai")
    # freightService.displayDirectTrain("Mumbai", "Ahmedabad")
    # freightService.displayDirectTrain("Ahmedabad", "New Delhi")
    # freightService.displayDirectTrain("Vishakhapatnam", "Hyderabad")
    # freightService.displayDirectTrain("New Delhi", "Chennai")
    # freightService.displayDirectTrain("Calcutta", "New Delhi")
    #
    # freightService.displayConnectedCities("T1122")
    # freightService.displayConnectedCities("T0000")
    # freightService.displayConnectedCities("T1235")
    # freightService.displayConnectedCities("T3344")
    #
    # freightService.findServiceAvailable("Calcutta", "Chennai")
    # freightService.findServiceAvailable("Calcutta", "Mumbai")
    # freightService.findServiceAvailable("Calcutta", "Nagpur")
    # freightService.findServiceAvailable("Nagpur", "Vishakhapatnam")
    # freightService.findServiceAvailable("Nagpur", "Ahmedabad")
    # freightService.findServiceAvailable("Chennai", "Bangalore")
    # freightService.findServiceAvailable("Bangalore", "Chennai")
    # freightService.findServiceAvailable("Bangalore", "Bangalore")


