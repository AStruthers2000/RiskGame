#Europe
class Iceland:
    def __init__(self):
        self.name = "Iceland"
        self.adjCountries = ("Greenland", "Scandinavia", "Great Britain")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [445,75, 480,75, 480,100, 445,100]

class Scandinavia:
    def __init__(self):
        self.name = "Scandinavia"
        self.adjCountries = ("Iceland", "Ukraine", "Northern Europe", "Great Britain")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [485,60, 550,60, 550,190, 485,190]

class Ukraine:
    def __init__(self):
        self.name = "Ukraine"
        self.adjCountries = ("Scandinavia", "Northern Europe", "Southern Europe", "Middle East", "Afghanistan", "Ural")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [550,55, 660,55, 660,200, 550,200]

class GreatBritain:
    def __init__(self):
        self.name = "Great Britain"
        self.adjCountries = ("Iceland", "Scandinavia", "Northern Europe", "Western Europe")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [415,195, 470,195, 470,250, 415,250]

class NorthernEurope:
    def __init__(self):
        self.name = "Northern Europe"
        self.adjCountries = ("Great Britain", "Scandinavia", "Ukraine", "Southern Europe", "Western Europe")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [475,210, 540,210, 540,265, 475,265]

class WesternEurope:
    def __init__(self):
        self.name = "Western Europe"
        self.adjCountries = ("Great Britain", "Northern Europe", "Southern Europe", "North Africa")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [405,270, 490,270, 490,330, 405,330]

class SouthernEurope:
    def __init__(self):
        self.name = "Southern Europe"
        self.adjCountries = ("Northern Europe", "Western Europe", "Middle East", "Ukraine", "Egypt", "North Africa")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [495,265, 550,265, 550,320, 495,320]

europe = {
    "iceland": Iceland(),
    "scandinavia": Scandinavia(),
    "ukraine": Ukraine(),
    "great britain": GreatBritain(),
    "northern europe": NorthernEurope(),
    "western europe": WesternEurope(),
    "southern europe": SouthernEurope()
}
