class vehicle:
    def __init__(self,name,wheels,max,vin) -> None:
        self.name = name
        self.wheels = wheels
        self._max = max
        self.__vin = vin

    def set_vin(self,vin):
        self.__vin = vin

    def v_detall(self):
        print("===============")
        print(f'mame:{self.name}')
        print("===============")
        print(f'wheels:{self.wheels}')
        print(f'max speed:{self._maxspeed}')
        print(f'vin:{self.vin}')