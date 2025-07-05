class Rect:
    def __init__(self,l,w):
        self.l= l
        self.w = w
    def area(self):
        return self.l*self.w
r = Rect(5,2)
print(f"Area of the rectangle: {r.area()}")