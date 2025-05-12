## Installing and using external libraries
## In python, you can extend your programs by using external libraries
## these are collections of code written by others to solve
## common problems - like data analysis, web development,
## or working with APIs


## we use a tool called pip to install these libraries
## example: Install and use requests (a popular library for web requests)
## in terminal use: pip install requests
## to upgrade: pip install --upgrade pip

import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())


## practice
## 1. imports the requests library
## 2. sends a get request to https://api.chucknorris.io/jokes/random
## 3. parses the json response
## prints the joke text to the screen

import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()  # json response
print("Joke:", data["value"])  # access "value" key from json response
## response.status_code == 200 to confirm the request was successful
## a bad URL or server issue usually raises a
## requests.exceptions.RequestException


## bonus
## write a program that gets a random joke from the chuck norris API
## and includes error handling
## make sure the program prints "Unable to retrieve joke"
## if there's a connection error or bad response

import requests

try:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    response.raise_for_status()  # raises HTTPError for bad responses
    data = response.json()
    print("Joke: ", data["value"])
except requests.exceptions.RequestException as errex:
    print("Unable to retrive joke:", errex)


## bonus: chuck norris joke saver
## 1. fetches 5 random chuck norris jokes from the api https://api.chucknorris.io/jokes/random
## 2. saves them (only the jokes) to a file called jokes.txt,
## with each joke on a new line
## after saving, read and print all the jokes from the file

import requests

# open a file for the api jokes
with open("jokes.txt", "w") as file:
    for _ in range(5):
        response = requests.get("https://api.chucknorris.io/jokes/random")
        joke = response.json()["value"]
        file.write(joke + "\n")

with open("jokes.txt", "r") as file:
    print(file.read())


## ask the user to input how many jokes they would like

import requests

try:
    count = int(input("How many Chuck Norris jokes would you like? "))

    with open("jokes.txt", "w") as file:
        for _ in range(count):
            response = requests.get("https://api.chucknorris.io/jokes/random")
            joke = response.json()["value"]
            file.write(joke + "\n")

    print(f"{count} jokes saved to jokes.txt!\n")

    with open("jokes.txt", "r") as file:
        print("Here are your jokes:\n")
        print(file.read())

except ValueError:
    print("Please enter a valid number.")
except requests.exceptions.RequestException:
    print("There was a problem fetching jokes from the API.")
