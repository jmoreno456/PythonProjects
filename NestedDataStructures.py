## list of lists
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(matrix[1][2])  # output = 6


## List of Dictionaries
# users = [{"name": "Jesse", "age": 28}, {"name": "Mary", "age": 24}]

# print(users[0]["name"])  # output = Jesse


## Dictionary of Lists
# grades = {"Math": [88, 92, 95], "Science": [90, 85, 80]}

# print(grades["Science"][1])  # output = 85


## Dictionary of Dictionaries
# employee = {
# "Jesse": {"postion": "Engineer", "salary": 85000},
# "Mary": {"position": "Data Analyst", "salary": 75000},
# }

# print(employee["Mary"]["salary"])  # output = 75000


## quiz
# people = [{"name": "Tom", "age": 25}, {"name": "Lily", "age": 30}]

# print(people[1]["name"])  # output = Lily


## practice: Dictionary of lists
# students = {"Jesse": [80, 90, 95], "Mary": [90, 70, 92], "Tom": [80, 77, 90]}

# for key, value in students.items():
# average = sum(value) / len(value)
# print(f"{key}'s average: {average:.1f}")


## bonus: list of dictionaries
# books = [
# {"Title": "Normal People", "Author": "Sally Rooney", "Year": 2010},
# {"Title": "A Game of Thrones", "Author": "GRRM", "Year": 1996},
# {"Title": "Clown in a corn field", "Author": "Adam Cesare", "Year": 2020},
# ]

# user_input = int(input("Enter a year: "))

# for book in books:
# if book["Year"] >= user_input:
# print(f"Title: {book['Title']}, Author: {book['Author']}")


## bonus: movie night organizer
movies = [
    {"Title": "Scream", "Genre": "Horror", "Year": 1996},
    {"Title": "Interstellar", "Genre": "Sci-Fi", "Year": 2014},
    {"Title": "Get Out", "Genre": "Horror", "Year": 2017},
]


user_input = input("Enter a genre (e.g., Horror): ").strip().lower()

found = False
for movie in movies:
    if user_input == movie["Genre"].lower():
        print(f"Title: {movie['Title']}, Year: {movie['Year']}")
        found = True

if not found:
    print("There are no movies with that genre listed")
