#North America
class Alaska:
    def __init__(self):
        self.name = "Alaska"
        self.adjCountries = ("Northwest Territory", "Alberta", "Kamchatka")
        self.curPlayer = ""
        self.curPeople = 0

class NWTerritory:
    def __init__(self):
        self.name = "Northwest Territory"
        self.adjCountries = ("Alaska", "Alberta", "Greenland", "Ontario")
        self.curPlayer = ""
        self.curPeople = 0

class Greenland:
    def __init__(self):
        self.name = "Greenland"
        self.adjCountries = ("Northwest Territory", "Ontario", "Quebec", "Iceland")
        self.curPlayer = ""
        self.curPeople = 0

class Alberta:
    def __init__(self):
        self.name = "Alberta"
        self.adjCountries = ("Northwest Territory", "Ontario", "Western United States", "Alaska")
        self.curPlayer = ""
        self.curPeople = 0

class Ontario:
    def __init__(self):
        self.name = "Ontario"
        self.adjCountries = ("Alberta", "Northwest Territory", "Quebec", "Greenland", "Eastern United States")
        self.curPlayer = ""
        self.curPeople = 0

class Quebec:
    def __init__(self):
        self.name = "Quebec"
        self.adjCountries = ("Ontario", "Eastern United States", "Greenland")
        self.curPlayer = ""
        self.curPeople = 0

class WestUS:
    def __init__(self):
        self.name = "Western United States"
        self.adjCountries = ("Alberta", "Central America", "Eastern United States", "Ontario")
        self.curPlayer = ""
        self.curPeople = 0

class EastUS:
    def __init__(self):
        self.name = "Eastern United States"
        self.adjCountries = ("Ontario", "Western United States", "Quebec", "Central America")
        self.curPlayer = ""
        self.curPeople = 0

class CentralAmerica:
    def __init__(self):
        self.name = "Central America"
        self.adjCountries = ("Western United States", "Eastern United States", "Venezuela")
        self.curPlayer = ""
        self.curPeople = 0

northAmerica = {
    "alaska": Alaska(),
    "northwest territory": NWTerritory(),
    "greenland": Greenland(),
    "alberta": Alberta(),
    "ontario": Ontario(),
    "quebec": Quebec(),
    "western united states": WestUS(),
    "eastern united states": EastUS(),
    "central america": CentralAmerica()
}
