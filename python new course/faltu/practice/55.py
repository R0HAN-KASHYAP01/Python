def countNow(place):
    for value in place.values():
        if len(value) > 5:
            print(value.upper())
        
places = {1: "Delhi",
          2: "London",
          3: "Paris",
          4: "New York",
          5: "Doha"}

countNow(places)
