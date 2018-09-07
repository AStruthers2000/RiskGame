import NorthAmerica, SouthAmerica, Europe, Asia, Africa, Australia


northAm = NorthAmerica.northAmerica
southAm = SouthAmerica.southAmerica
europe = Europe.europe
asia = Asia.asia
africa = Africa.africa
australia = Australia.australia

continents = {
    "North America": northAm,
    "South America": southAm,
    "Europe": europe,
    "Asia": asia,
    "Africa": africa,
    "Australia": australia
}

"""for continent, var in continents.items():
    for var2, country in continents[continent].items():
        print(country.name + " is touching: ")
        for adjCount in country.adjCountries:
            print("\t" + adjCount)
"""

"""def isValidAttack(self, countryFrom, countryTo, playerName):
        countryFrom = countryFrom.lower()
        countryTo = countryTo.lower()

        if playerName == GetCurrentOccupent(countryTo):
            """

class CountryInfo:
    def LookupContinentByCountry(self, userCountryName):
        userCountryName = userCountryName.lower()
        for continentName, countryGroup in continents.items():
            for countryName, country in continents[continentName].items():
                if countryName.lower() == userCountryName.lower():
                    return continentName

    def GetBorderingCountries(self, userCountryName):
        userCountryName = userCountryName.lower()
        for continentName, countryGroup in continents.items():
            for countryName, country in continents[continentName].items():
                if countryName.lower() == userCountryName.lower():
                    return country.adjCountries

    def GetCurrentOccupent(self, userCountryName):
        userCountryName = userCountryName.lower()
        for continentName, countryGroup in continents.items():
            for countryName, country in continents[continentName].items():
                if countryName.lower() == userCountryName.lower():
                    return country.curPlayer

    def GetCurrentSoliderCount(self, userCountryName):
        userCountryName = userCountryName.lower()
        for continentName, countryGroup in continents.items():
            for countryName, country in continents[continentName].items():
                if countryName.lower() == userCountryName.lower():
                    return country.curPeople

    def GetCountryNameByClick(self, click):
        import Rectangle
        Rectangle = Rectangle.Rectangle()
        for continentName, countryGroup in continents.items():
            for countryName, country in continents[continentName].items():
                if Rectangle.contains(click, country.colliderPoints):
                    return country.name

    def GetCountryTextPos(self, userCountryName):
        userCountryName = userCountryName.lower()
        for continentName, countryGroup in continents.items():
            for countryName, country in continents[continentName].items():
                if countryName.lower() == userCountryName.lower():
                    return country.textPos

    def ChangeCountryColor(self, userCountryName, newColor):
        for continentName, countryGroup in continents.items():
            for countryName, country in continents[continentName].items():
                if countryName.lower() == userCountryName.lower():
                    country.textColor = newColor

    def ChangeCountryArmyCount(self, userCountryName, numChange):
        for continentName, countryGroup in continents.items():
            for countryName, country in continents[continentName].items():
                if countryName.lower() == userCountryName.lower():
                    country.curPeople += numChange
