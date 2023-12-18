from support import house, road
from collections import deque

class RoadNetwork:
    def __init__(self) -> None:
        self.houses = {}
        self.roads = {}
        
    def add_road_connection(self, road1, road2):
        # Check if road1 is already in the list of roads
        if road1 not in self.roads:
            # If not, create a new road with road1
            self.create_road(road1)
        
        # Check if road2 is already in the list of roads
        if road2 not in self.roads:
            # If not, create a new road with road2
            self.create_road(road2)
        
        # Add road2 as a connection to road1
        self.roads[road1].add_connection(road2)
        
        # Add road1 as a connection to road2
        self.roads[road2].add_connection(road1)


    def create_road(self, name):
        # Create a new road object with the given name
        new_road = road(name)
        
        # Append the new road object to the list of roads
        self.roads[name] = new_road


    def create_house(self, name, road):
        # Check if the road already exists in the roads dictionary
        if road not in self.roads:
            # Create a new house for the road
            self.create_road(road)
        # Create a new house with the given name and road
        self.houses[name] = (house(name, road))


    def bfs(self, road1, road2):
        # Check if both roads exist
        if road1 not in self.roads or road2 not in self.roads:
            return [road1]

        # Create a queue with the starting road
        queue = deque([(road1, [road1])])

        # Create a set to keep track of visited roads
        visited = set([road1])

        # Loop until the queue is empty
        while queue:
            # Get the first road and its path in the queue
            road, path = queue.popleft()

            # Check if the road is the target road
            if road == road2:
                return path

            # Get the connections of the road
            connections = self.roads[road].connections

            # Loop through the connections
            for connection in connections:
                # Check if the connection has been visited
                if connection not in visited:
                    # Add the connection to the queue with the updated path
                    queue.append((connection, path + [connection]))
                    # Add the connection to the visited set
                    visited.add(connection)

        # No path found
        return ['no path found']

    def find_path(self, house1, house2):
        road1 = self.houses[house1].road
        road2 = self.houses[house2].road
        path = self.bfs(road1, road2)
        return path



if __name__ == '__main__':
    n1 = RoadNetwork()
    n1.create_house('house1', 'road1')
    n1.create_house('house2', 'road2')
    n1.create_road('road3')
    n1.add_road_connection('road1', 'road3')
    n1.add_road_connection('road2', 'road3')

    print('Network 1 shortest path is - road1 -> road3 -> road2')
    print(f"Shortest path network 1: {n1.find_path('house1', 'house2')}")
    print()

    n2 = RoadNetwork()
    n2.create_house('house1', 'road1')
    n2.create_house('house2', 'road2')
    n2.create_road('road3')
    n2.add_road_connection('road1', 'road3')
    n2.add_road_connection('road1', 'road2')
    n2.add_road_connection('road2', 'road3')

    print('Network 2 shortest path is - road1 -> road2')
    print(f"Shortest path network 2: {n2.find_path('house1', 'house2')}")
    print()

    
    n3 = RoadNetwork()
    n3.create_house('house1', 'road1')
    n3.create_house('house2', 'road2')
    n3.create_road('road3')
    n3.create_road('road4')
    n3.add_road_connection('road1', 'road3')
    n3.add_road_connection('road2', 'road4')

    print('Network 3 has no connecting roads')
    print(f"Shortest path network 3: {n3.find_path('house1', 'house2')}")