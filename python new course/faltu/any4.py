cities = {1:"Agra",2:"Chennai",3: "Lucknow",4:"Mumbai",5:"Surat"}
def countChar(cities):
    city = cities.values()
    for i in city:
        if len(i) <= 5:
            print(i)
        else:
            pass

countChar(cities)