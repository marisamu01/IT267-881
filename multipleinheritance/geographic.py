class Geographic:

    def setCordinate(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def getCordinate(self):
        return str(self.latitude) + ', ' + str(self.longitude)

    def getTimeZone(self):
        timezone = round(self.longitude / 12 - 1)
        if timezone > 0:
            return '+' + str(timezone)
        else:
            return str(timezone)

    def getClimate(self):
        if self.latitude <= -66.5 or self.latitude >= 66.5:
            return 'Polar zone'
        elif self.latitude <= -23.5 or self.latitude >= 23.5:
            return 'Temperate zone'
        else:
            return 'Tropical zone'
