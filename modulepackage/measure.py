import numbers

class Measure:
    def __init__(self) -> None:
        self.result = 0

    def inch_cm(self,number):
        self.result = number * 2.54
        return self.result

    def cm_inch(self,numbers):
        self.result = numbers / 2.54
        return self.result