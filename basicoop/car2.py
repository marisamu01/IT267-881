class Car:
    brand = "Toyota"

    def __init__(self,model,colour,year,price) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price
    #in

    def printCarDetail(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price:,.2f}")
    #static method ไม่มี self
    @staticmethod
    def get_static_method():
        text = "stat"
        print(f"In {text} method")

    
    @classmethod
    def get_class_method(cls):
        my_text = "Class"
        print(f"This is {my_text} method")

    def __del__(self) -> None:
        print("odject was destroyed")

if __name__ == "__main__":
    my_car = Car("Cross","white",2022,1500000)
    my_car.printCarDetail()

    #เรียกใช้ static_method
    Car.get_static_method()
    my_car.get_static_method()

    Car.get_class_method()
    my_car.get_class_method()