from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self,name,wheels,max,vin) -> None:
        Vehicle.__init__(self,name,wheels,max,vin)

    def set_color(self,color):
        self.color = color

    def set_capacity(self,capacity):
        self.capacity = capacity

    def v_detail(self):
        Vehicle.V_detail(self)
        print(f'color:{self.color}')
        print(f'capacity:{self.capacity}')