#! /usr/bin/env python3


def checkConnection(cities):
    checkedCities = {}
    for connectedCityPair in cities:
        print(connectedCityPair)
        currentCity = connectedCityPair[0]
        if currentCity not in checkedCities:
            checkedCities[currentCity]=[]
                

def findConnectedCities(cities):
    checkedCities = {}
    for i in range(len(cities)):
        currentCity = cities[i][0]
        if currentCity not in checkedCities.keys():
            checkedCities[currentCity] = []
            for c in cities:
                if currentCity in c:
                    checkedCities[currentCity].append(c)
            print(f'city {currentCity} can be connected with {len(checkedCities[currentCity])} cities: {checkedCities[currentCity]}')
    return checkedCities

# Add first city to searched, check what cities is connected to,  
def graphRepresentation(cities):
    q = []
    searched = {}
    while len(cities) != 0:
        currentElement = cities.pop(0)
        print(currentElement)
        root = currentElement[0]
        child = currentElement[1]
        print(f"{root} -> {child}")
        # Check if child has any connections:
        for element in cities:
            if child in element:
                print(element)
        

# Right now this DFS does not add nodes that are not directly connected with others.
def breadthFirstSearch(citiesList):
    print(citiesList)
    # Add first node to empty stack
    myStack = []
    # Track nodes that were seen:
    seen = []
    # Save paths here:
    paths = {}
    currentNode = citiesList[0][0]
    print(currentNode)
    myStack.append(currentNode)
    while True:
        print("Fired up")
        # if stack is empty and result is not returned 
        if len(myStack) == 0:
            print("No path")
            break
        # Pop a node from stack and check if it is connected to any other nodes 
        currentNode = myStack.pop() 
        print(currentNode)
        # Check if this node has been checked before
        if currentNode not in seen:
            seen.append(currentNode)
        if currentNode not in paths.keys():
            paths[currentNode] = []
        # Check if current node has children
        for pair in citiesList:
            if currentNode in pair:
                for el in pair:
                    if el != currentNode and el not in seen:
                        paths[currentNode].append(el)
                        myStack.append(el)
    print(paths)


if __name__ == "__main__":

    c_road = 2
    c_lib = 3
    cities = [[1,7], [1,3], [1,2], [2,3], [5,6], [6,8]]
#    findConnectedCities(cities)
#    graphRepresentation(cities)
    breadthFirstSearch(cities)
