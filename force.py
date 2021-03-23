class Force:
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    def get_horizontal(self):
        return self.magnitude*cos(radians(self.angle))
    def get_vertical(self):
        return self.magnitude*sin(radians(self.angle))

    def get_angle(self, use_degrees = True):
        if use_degrees:
            return self.angle
        else:
            return radians(self.angle)

def find_net_force(list_of_forces):
    runHorizontal = 0
    runVertical = 0
    for force in list_of_forces:
        runHorizontal += force.get_horizontal()
        runVertical += force.get_vertical()
    magnitude = round((runHorizontal ** 2 + runVertical ** 2)**0.5,1)
    angle = round(degrees(atan2(runVertical , runHorizontal)),1)
    return Force(magnitude, angle)
    
