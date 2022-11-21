import csv

students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)


# def get_name(student):
#     return student["name"]
#
#
#
# def get_house(student):
#     return student["house"]


# for student in sorted(students, key=get_house, reverse=True):
#     print(f"{student['name']} is in {student['house']}")

# with open("students.csv") as file:
#     # reader = csv.reader(file)
#     reader = csv.DictReader(file)
#     # for name, home in reader:
#     for row in reader:
#         # students.append({"name": name, "home": home})
#         students.append({"name": row["name"], "home": row["home"]})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

name = input("Whats your name? ")
home = input("Wheres your home? ")


with open("students.csv", "a") as file:
    # writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home": home})
