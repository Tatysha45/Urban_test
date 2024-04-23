class Buiding:
    def __init__(self, numberOfFloors=18,
                 buildingType='panel'):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors
                and self.buildingType == other.buildingType)

    def __init__(other, numberOfFloors=10,
                 buildingType='brick'):
        other.numberOfFloors = numberOfFloors
        other.buildingType = buildingType


House1 = Buiding(numberOfFloors=18)
Buiding(buildingType='panel')
House2 = Buiding(numberOfFloors=10)
Buiding(buildingType='brick')
if Buiding.eq(self=House1):
    print('ЖК')
else:
    print('улица')
