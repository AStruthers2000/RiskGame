import NorthAmerica, SouthAmerica, Europe, Asia, Africa, Australia

northAm = NorthAmerica.northAmerica
southAm = SouthAmerica.southAmerica
#europe = Europe.europe
#asia = Asia.asia
africa = Africa.africa
australia = Australia.australia

continents = {
    "North America": northAm,
    "South America": southAm,
    #"Europe": europe,
    #"Asia": asia,
    "Africa": africa,
    "Australia": australia
}

for continent, var in continents.items():
    for var2, country in continents[continent].items():
        print(country.name + " is touching: ")
        for adjCount in country.adjCountries:
            print("\t" + adjCount)
