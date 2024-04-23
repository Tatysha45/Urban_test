class Buiding:
    def __init__(self, numberOfFloors=18,
                 buildingType='panel'):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


a = Buiding()
b = Buiding(numberOfFloors=10, buildingType='brick')

print(a == b)