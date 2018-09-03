#South America
class Venezuela:
    def __init__(self):
        self.name = "Venezuela"
        self.adjCountries = ("Central America", "Brazil", "Peru")
        self.curPlayer = ""
        self.curPeople = 0

class Peru:
    def __init__(self):
        self.name = "Peru"
        self.adjCountries = ("Venezuela", "Brazil", "Argentina")
        self.curPlayer = ""
        self.curPeople = 0

class Brazil:
    def __init__(self):
        self.name = "Brazil"
        self.adjCountries = ("Venezuela", "Peru", "Argentina", "North Africa")
        self.curPlayer = ""
        self.curPeople = 0

class Argentina:
    def __init__(self):
        self.name = "Argentina"
        self.adjCountries = ("Peru", "Brazil")
        self.curPlayer = ""
        self.curPeople = 0

southAmerica = {
    "venezuela": Venezuela(),
    "peru": Peru(),
    "brazil": Brazil(),
    "argentina": Argentina()
}
