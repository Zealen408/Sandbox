class house:
    def __init__(self, name, road):
        self.name = name
        self.road = road



class road:
    def __init__(self, name):
        self.name = name
        self.connections = []
    
    def add_connection(self, road):
        self.connections.append(road)
    
