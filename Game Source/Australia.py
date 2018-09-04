#Australia
class Indonesia:
    def __init__(self):
        self.name = "Indonesia"
        self.adjCountries = ("Siam", "Western Australia", "New Guinea")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [795,365, 910,365, 910,420, 795,420]

class NewGuinea:
    def __init__(self):
        self.name = "New Guinea"
        self.adjCountries = ("Indonesia", "Western Australia", "Eastern Australia")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [915,370, 1000,370, 1000,435, 915,435]

class WesternAustralia:
    def __init__(self):
        self.name = "Western Australia"
        self.adjCountries = ("Indonesia", "New Guinea", "Eastern Australia")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [850,440, 930,440, 930,555, 850,555]

class EasternAustralia:
    def __init__(self):
        self.name = "Eastern Australia"
        self.adjCountries = ("New Guinea", "Western Australia")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [930,440, 1000,440, 1000,550, 930,550]

australia = {
    "indonesia": Indonesia(),
    "new guinea": NewGuinea(),
    "western australia": WesternAustralia(),
    "eastern australia": EasternAustralia()
}
