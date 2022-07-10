class Temperature:

    def setCelsius(self, celsius):
        self.celsius = celsius

    def getFahrenheit(self):
        return self.celsius * 1.8 + 32

    def getWeather(self):
        if self.celsius <= 0:
            return 'freezing'
        elif self.celsius <= 18:
            return 'cold'
        elif self.celsius <= 28:
            return 'warm'
        else:
            return 'hot'

from geographic import Geographic
from temprature import Temperature

class Country(Geographic,Temperature):
    def __init__(self, name, area, population):
        self.name = name
        self.area = area
        self.population = population

    def getPopulationDensity(self):
       return self.population / self.area

    def showDetails(self):
        print(f'Country: {self.name}')
        print(f'Area: {self.area:,.2f} sq km')
        print(f'Population: {self.population:,}')
        print(f'Density: {self.getPopulationDensity():,.2f} person per sq km')
        print(f'Decimal cordinate: {self.getCordinate()}')
        print(f'Time zone: {self.getTimeZone()}')
        print(f'Climate: {self.getClimate()}')
        print(f'Temperature in Celsius: {self.celsius:.2f} degree')
        print(f'Temperature in Fahrenheit: {self.getFahrenheit():.2f} degree')
        print(f'The weather is {self.getWeather()}')
        print()

if __name__ == "__main__":
    c1 = Country('Thailand', 513120, 68863514)
    c1.setCordinate(13.75, 100.483333)
    c1.setCelsius(28.5)
    c1.showDetails()

    c2 = Country('England', 130279, 55268100)
    c2.setCordinate(51.5, -0.116667)
    c2.setCelsius(9)
    c2.showDetails()

    c3 = Country('Canada', 9984670, 35151728)
    c3.setCordinate(45.4, -75.666667)
    c3.setCelsius(-3)
    c3.showDetails()
