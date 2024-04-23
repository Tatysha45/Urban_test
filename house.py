class House:
    def __init__(self):
        self.HouseType = 'panel'
        self.color = 'white'
        self.numberOfFloors = 10
        self.entrance = 5

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

my_house = House()

my_house.setNewNumberOfFloors(8)

print('HouseType',my_house.HouseType)
print('color',my_house.color)
print('numberOfFloors',my_house.numberOfFloors)
print('entrance',my_house.entrance)





# class House:
#     def __init__(self):
#         self.numberOfFloors = 10
#
#     print("Текущий этаж равен 1")



# class House:
#     numberOfFloors = 10
#     entrance = 5
# print(dir(House))
