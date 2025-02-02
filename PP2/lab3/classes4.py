class Point:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def show(self):
        print(f"Coordinates: {self.p1}, {self.p2}")
    def move(self, new_p1, new_p2):
        self.p1 = new_p1
        self.p2 = new_p2
    def dist(self):
        return (self.p1 ** 2 + self.p2 ** 2) ** 0.5

points = Point(2,6)
points.show() 
points.move(3,4)
points.show()
print(f"Distance between 2 points: {points.dist()}") 