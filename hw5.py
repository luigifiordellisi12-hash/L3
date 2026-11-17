
# My School Subject Planner

# A: Student card
card = ("Oliver", 10, "A")

# TODO 1: Print student name, grade and section
print("Student:", card[0])
print("Grade and section:", card[1:3])

# B: Subjects for each day
monday_list = ["Biology", "Maths", "Geography", "Maths", "Drama"]
tuesday_list = ["Biology", "History", "French", "Music", "History"]

# TODO 2: Create sets
monday = set(monday_list)
tuesday = set(tuesday_list)

print("Monday:", len(monday), sorted(monday))

# TODO 3: Update subjects
monday.discard("Drama")
tuesday.add("Computing")
monday.discard("Dance")

print("Monday:", sorted(monday))
print("Tuesday:", sorted(tuesday))

# TODO 4: Set operations
print("Both days:", sorted(monday & tuesday))
print("Either day:", sorted(monday | tuesday))
print("Only Monday:", sorted(monday - tuesday))
print("Exactly one day:", sorted(monday ^ tuesday))
