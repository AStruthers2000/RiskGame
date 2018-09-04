""" im going to take notes on ideas before any real programming
have each country as a dictionary with

"""
import allCountries
import GraphicsMain

import _thread as thread

GraphicsMain = GraphicsMain.GraphicsMain()

thread.start_new_thread(GraphicsMain.mainThread, ("MainGraphicsThread", ))

CountryInfo = allCountries.CountryInfo()

"""while True:
    country = str(input("Choose a country: "))
    print(CountryInfo.LookupContinentByCountry(country))
    print(CountryInfo.GetBorderingCountries(country))
    print(CountryInfo.GetCurrentOccupent(country))
    print(CountryInfo.GetCurrentSoliderCount(country))
    
"""
