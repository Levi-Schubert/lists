planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus","Neptune"])
planet_list.append("Pluto")
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
rocky_planets = planet_list[0:4]
del planet_list[(len(planet_list) - 1)]
print(planet_list)
print(rocky_planets)