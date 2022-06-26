class Car:
    brand = "Toyota"

    def __init__(self,model,colour,year,price) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price

    def printCarDetail(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price:,.2f}")

    def __del__(self) -> None:
        print("odject was destroyed")

if __name__ == "__main__":
    my_car = Car("Cross","white",2022,1500000)
    my_car.printCarDetail()