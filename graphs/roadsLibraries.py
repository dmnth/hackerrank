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
        





if __name__ == "__main__":

    c_road = 2
    c_lib = 3
    cities = [[1,7], [1,3], [1,2], [2,3], [5,6], [6,8]]

#    findConnectedCities(cities)
    graphRepresentation(cities)
