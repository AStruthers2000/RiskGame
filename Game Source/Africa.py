#Africa
class NorthAfrica:
    def __init__(self):
        self.name = "North Africa"
        self.adjCountries = ("Brazil", "Egypt", "Southern Europe", "Western Europe", "East Africa", "Congo")
        self.curPlayer = ""
        self.curPeople = 0

class Egypt:
    def __init__(self):
        self.name = "Egypt"
        self.adjCountries = ("North Africa", "Southern Europe", "Middle East", "East Africa")
        self.curPlayer = ""
        self.curPeople = 0

class EastAfrica:
    def __init__(self):
        self.name = "East Africa"
        self.adjCountries = ("Egypt", "North Africa", "Middle East", "Congo", "South Africa", "Madagascar")
        self.curPlayer = ""
        self.curPeople = 0

class Congo:
    def __init__(self):
        self.name = "Congo"
        self.adjCountries = ("North Africa", "East Africa", "South Africa")
        self.curPlayer = ""
        self.curPeople = 0

class SouthAfrica:
    def __init__(self):
        self.name = "South Africa"
        self.adjCountries = ("Madagascar", "Congo", "East Africa")
        self.curPlayer = ""
        self.curPeople = 0

class Madagascar:
    def __init__(self):
        self.name = "Madagascar"
        self.adjCountries = ("East Africa", "South Africa")
        self.curPlayer = ""
        self.curPeople = 0

africa = {
    "north africa": NorthAfrica(),
    "egypt": Egypt(),
    "east africa": EastAfrica(),
    "congo": Congo(),
    "south africa": SouthAfrica(),
    "madagascar": Madagascar()
}
