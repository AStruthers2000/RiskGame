#Australia
class Indonesia:
    def __init__(self):
        self.name = "Indonesia"
        self.adjCountries = ("Siam", "Western Australia", "New Guinea")
        self.curPlayer = ""
        self.curPeople = 0

class NewGuinea:
    def __init__(self):
        self.name = "New Guinea"
        self.adjCountries = ("Indonesia", "Western Australia", "Eastern Australia")
        self.curPlayer = ""
        self.curPeople = 0

class WesternAustralia:
    def __init__(self):
        self.name = "Western Australia"
        self.adjCountries = ("Indonesia", "New Guinea", "Eastern Australia")
        self.curPlayer = ""
        self.curPeople = 0

class EasternAustralia:
    def __init__(self):
        self.name = "Eastern Australia"
        self.adjCountries = ("New Guinea", "Western Australia")
        self.curPlayer = ""
        self.curPeople = 0

australia = {
    "indonesia": Indonesia(),
    "new guinea": NewGuinea(),
    "western australia": WesternAustralia(),
    "eastern australia": EasternAustralia()
}
