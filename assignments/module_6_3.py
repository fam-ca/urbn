class Horse:
    def __init__(self, x_distance: int = 0, y_distance: int =0, sound: str = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__(y_distance)
    
    def run(self, dx):
        return self.x_distance + dx

class Eagle:
    def __init__(self, y_distance: int = 0, 
                 sound: str = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        return self.y_distance + dy
    
    def about(self):
        print(self.y_distance)


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
    
    def move(self, dx, dy):
        self.x_distance = self.run(dx)
        self.y_distance = self.fly(dy)
        return (self.x_distance, self.y_distance)
    
    def get_pos(self):
        return (self.x_distance, self.y_distance)
    
    def voice(self):
        print(self.sound)

# print(Pegasus.mro())
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
