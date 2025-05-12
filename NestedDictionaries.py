## loops with dictionaries and nested structures


## imagine you're storing multiple students and their scores in
## different subjects. you can use a nested dictionary for that
students = {
    "Alice": {"Math": 95, "Science": 88},
    "Bob": {"Math": 72, "Science": 65},
    "Cara": {"Math": 83, "Science": 91},
}

for name, subjects in students.items():
    print(f"{name}'s grades:")
    for subjects, score in subjects.items():
        print(f" {subjects}: {score}")


## practice
## 1. create a dictionary called grades with at least 2 students,
## each having 2 subjects with scores
## 2. use nested for loops to print each student's name and
## their subject scores
grades = {"Jesse": {"English": 70, "Gym": 90}, "Mary": {"English": 95, "Gym": 70}}

print(grades["Jesse"]["Gym"])  # outputs 90

for name in grades.keys():
    print(name)

for name, subjects in grades.items():
    print(f"{name}'s grades")
    for (
        subjects_name,
        score,
    ) in subjects.items():  # use value in nested for loop to retrieve nested dictionary
        print(f" {subjects_name}: {score}")
## change key name in nested for loop to keep the dictionary intact
## and loop properly through each subject and score
grades = {"Jesse": {"English": 70, "Gym": 90}, "Mary": {"English": 95, "Gym": 70}}

for name, subjects in grades.items():
    print(f"{name}'s grades")
    total = 0
    count = 0

for subjects_name, score in subjects.items():
    print(f" {subjects_name}: {score}")
    total += score
    count += 1

average = total / count
print(f"Average: ", average)
## initialize a total score for each student inside the outer loop
## count the number of subjects
## calculate the average after the inner loop


## Bonus challenge: Grade report with averages
## you are given a dictionary of students and their grades
## your task is to print each student's name
## their individual subject grades
## and their average score
grades = {
    "Jesse": {"Math": 88, "Science": 92, "English": 81},
    "Mary": {"Math": 95, "Science": 85, "English": 78},
    "Sam": {"Math": 70, "Science": 75, "English": 80},
}

for name, subject in grades.items():
    print(f"{name}")
    total = 0
    count = 0
for subject_name, score in subject.items():
    print(f" {subject_name}: {score}")
    total += score
    count += 1  # dynamic

average = round(total / count, 2)
print(f"Average: ", average)
