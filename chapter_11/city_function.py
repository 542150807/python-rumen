def describe_city(city, country, population=""):
    if population:
        des_city = city + ", " + country + " - population " + population
    else:
        des_city = city + ", " + country
    return des_city.title()
