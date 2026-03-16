# 11-1 city, country: write a function that accepts two parameters: a
# city name and a country name.
# the function should return a single string of the form city, country,
# such as santiago chile.
# store the function in a module called city_function.py, and save this
# in a new folder so pytest won't try to run the tests we've already
# written.
# create a file called test_cities.py that tests the function you just
# wrote.
# write a function called test_city_country() to verify that calling
# your function with values such as 'santiago' and 'chile' results in
# the correct string.
# run the test, and make sure test_city_country() passes

# def get_city_country(city, country):
#   """return a city, country string"""
#  formatted_city_country = f"{city}, {country}"
# return formatted_city_country.title()


# 11-2 population: modify your function so it requires a third parameter,
# population.
# it should now return a single string of the form city, country -
# population xxx, such as santiago, chile - population 5000000.
# run the test again, and make sure test_city_country() fails this time.
# modify the function so the parameter is optional. run the test, and
# make sure test_city_country() passes again
# write a second test called test_city_country_population() that verifies
# you can call your function with the values 'santiago', 'chile', and
# 'population=5000000'.
# run the tests one more time, and make sure this new test passes.


def get_city_country(city, country, population=""):
    """return a city, country, and population string."""
    if population:
        formatted_city_country = f"{city}, {country} - {population}"
    else:
        formatted_city_country = f"{city}, {country}"
    return formatted_city_country.title()
