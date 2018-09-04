#North America
class Alaska:
    def __init__(self):
        self.name = "Alaska"
        self.adjCountries = ("Northwest Territory", "Alberta", "Kamchatka")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [0,0,75,0,75,125,0,125]

class NWTerritory:
    def __init__(self):
        self.name = "Northwest Territory"
        self.adjCountries = ("Alaska", "Alberta", "Greenland", "Ontario")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [80,15, 205,15, 205,105, 80,105]

class Greenland:
    def __init__(self):
        self.name = "Greenland"
        self.adjCountries = ("Northwest Territory", "Ontario", "Quebec", "Iceland")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [210,0, 440,0, 440,110, 210,110]

class Alberta:
    def __init__(self):
        self.name = "Alberta"
        self.adjCountries = ("Northwest Territory", "Ontario", "Western United States", "Alaska")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [80,110, 170,110, 170,185, 80,185]

class Ontario:
    def __init__(self):
        self.name = "Ontario"
        self.adjCountries = ("Alberta", "Northwest Territory", "Quebec", "Greenland", "Eastern United States")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [180,110, 250,110, 250,200, 180,200]

class Quebec:
    def __init__(self):
        self.name = "Quebec"
        self.adjCountries = ("Ontario", "Eastern United States", "Greenland")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [265,115, 350,115, 350,215, 265,215]

class WestUS:
    def __init__(self):
        self.name = "Western United States"
        self.adjCountries = ("Alberta", "Central America", "Eastern United States", "Ontario")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [60,195, 150,195, 150,280, 60,280]

class EastUS:
    def __init__(self):
        self.name = "Eastern United States"
        self.adjCountries = ("Ontario", "Western United States", "Quebec", "Central America")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [160,225, 295,225, 295,305, 160,305]

class CentralAmerica:
    def __init__(self):
        self.name = "Central America"
        self.adjCountries = ("Western United States", "Eastern United States", "Venezuela")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [70,285, 155,285, 155,370, 70,370]

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
