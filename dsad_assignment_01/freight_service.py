# freight_service.py
#####################################################################


# Node Definition
class Node(object):
    city_label = None

    def __init__(self, city_label):
        self.city_label = city_label
    
    def get_city_label(self):
        return self.city_label


#####################################################################


# Edge Definition
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


#####################################################################


# Custom Graph Implementation
class Graph(object):
    set_of_distinct_nodes = set()
    set_of_distinct_edges = set()
    set_of_freight_trains = set()
    set_of_distinct_cities = set()
    number_of_nodes = 0
    number_of_edges = 0
    adjacency_matrix = []

    def __init__(self, number_of_distinct_cities, list_of_trains, list_of_routes):
        self.number_of_distinct_cities = number_of_distinct_cities
        self.list_of_trains = list_of_trains
        self.list_of_routes = list_of_routes
        self.initialize_adjacenct_matrix()

    def initialize_adjacenct_matrix(self):
        self.adjacency_matrix.append([0 for i in range(self.number_of_distinct_cities)])

    def initializeGraph(self):
        for i in range(len(self.list_of_routes)):
            train_label = self.list_of_trains[i]
            # create nodes out of the list of cities
            list_of_cities = self.list_of_routes[i]
            print(train_label,"<-->", list_of_cities)
            # Work In Progress

    def get_number_of_nodes(self):
        return len(self.set_of_distinct_nodes)
    
    def get_number_of_freight_trains(self):
        return len(self.set_of_freight_trains)


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

    def get_list_of_trains(self):
        return self.list_of_trains

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

        # now create the Graph object and then initialize it
        self.graph = Graph(number_of_distinct_cities, list_of_trains, list_of_routes)
        self.graph.initializeGraph()

    def showAll(self):
        pass

    def displayTransportHub(self):
        pass

    def displayConnectedCities(self, train):
        pass

    def displayDirectTrain(self, city_a, city_b):
        pass

    def findServiceAvailable(self, city_a, city_b): 
        pass
    
    def readPromptFile(self, promptfile):
        pass


#####################################################################
if __name__ == "__main__":
    freightService = FreightService()
    freightService.readCityTrainfile("inputPS22.txt")
    # freightService.showAll()


    