class Auto:
    def ride(self):
        print("Riding on a ground")


class Boat:
    def swim(self):
        print("Sailing in the ocean")


class Amphibian(Auto, Boat):
    pass


class ChildAmphibian(Amphibian):
    pass


a = Amphibian()
a.ride()  # Riding on a ground
a.swim()  # Sailing in the ocean

# инстанс класса Amphibian, будет одновременно инстансом класса Auto и Boat
print(isinstance(a, Auto))  # True
print(isinstance(a, Boat))  # True
print(isinstance(a, Amphibian))  # True
print(isinstance(a, ChildAmphibian))  # False
