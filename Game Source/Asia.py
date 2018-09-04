#Asia
class Ural:
    def __init__(self):
        self.name = "Ural"
        self.adjCountries = ("Ukraine", "Afghanistan", "China", "Siberia")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [665,0, 740,0, 740,165, 665,165]

class Siberia:
    def __init__(self):
        self.name = "Siberia"
        self.adjCountries = ("Ural", "China", "Mongolia", "Irkutsk", "Yakutsk")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [745,0, 805,0, 805,170, 745,170]

class Yakutsk:
    def __init__(self):
        self.name = "Yakutsk"
        self.adjCountries = ("Siberia", "Irkutsk", "Kamchatka")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [810,0, 955,0, 955,55, 810,55]

class Irkutsk:
    def __init__(self):
        self.name = "Irkutsk"
        self.adjCountries = ("Siberia", "Mongolia", "Kamchatka", "Yakutsk")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [810,60, 880,60, 880,165, 810,165]

class Kamchatka:
    def __init__(self):
        self.name = "Kamchatka"
        self.adjCountries = ("Yakutsk", "Irkutsk", "Mongolia", "Japan", "Alaska")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [885,65, 1000,65, 1000,170, 885,170]

class MiddleEast:
    def __init__(self):
        self.name = "Middle East"
        self.adjCountries = ("Southern Europe", "Ukraine", "Afghanistan", "India", "East Africa", "Egypt")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [585,305, 680,305, 680,395, 585,395]

class Afghanistan:
    def __init__(self):
        self.name = "Afghanistan"
        self.adjCountries = ("Ukraine", "Ural", "China", "India", "Middle East")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [620,205, 735,205, 735,295, 620,295]

class India:
    def __init__(self):
        self.name = "India"
        self.adjCountries = ("Middle East", "Afghanistan", "China", "Siam")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [680,300, 765,300, 765,390, 680,390]

class China:
    def __init__(self):
        self.name = "China"
        self.adjCountries = ("Afghanistan", "Ural", "Siberia", "Mongolia", "Siam", "India")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [740,220, 865,220, 865,305, 740,305]

class Mongolia:
    def __init__(self):
        self.name = "Mongolia"
        self.adjCountries = ("Siberia", "Irkutsk", "Kamchatka", "Japan", "China")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [785,170, 890,170, 890,225, 785,225]

class Japan:
    def __init__(self):
        self.name = "Japan"
        self.adjCountries = ("Kamchatka", "Mongolia")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [905,175, 940,175, 940,255, 905,255]

class Siam:
    def __init__(self):
        self.name = "Siam"
        self.adjCountries = ("China", "India", "Indonesia")
        self.curPlayer = ""
        self.curPeople = 0
        self.colliderPoints = [775,305, 845,305, 845,355, 775,355]

asia = {
    "ural": Ural(),
    "siberia": Siberia(),
    "yakutsk": Yakutsk(),
    "irkutsk": Irkutsk(),
    "kamchatka": Kamchatka(),
    "middle east": MiddleEast(),
    "afghanistan": Afghanistan(),
    "india": India(),
    "china": China(),
    "mongolia": Mongolia(),
    "japan": Japan(),
    "siam": Siam()
}
