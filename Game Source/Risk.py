""" im going to take notes on ideas before any real programming
have each country as a dictionary with

"""
import allCountries

class Board:
    def __init__(self, places):
        self.countryInfo = places

board = Board(allCountries.countries)

print(board.countryInfo)
