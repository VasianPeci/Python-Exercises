grades = [73, 60, 95, 52, 100, 45, 81, 92, 88, 67]

def highest_grade(grades):
    max = grades[0]
    for grade in grades:
        if grade > max:
            max = grade
    return max

def lowest_grade(grades):
    min = grades[0]
    for grade in grades:
        if grade < min:
            min = grade
    return min

def average(grades):
    return sum(grades)/len(grades)

def sort(grades):
    return sorted(grades)

print(f"Highest grade: {highest_grade(grades)}")
print(f"Lowest grade: {lowest_grade(grades)}")
print(f"Average grade: {average(grades)}")
print(f"Grades in ascending order: {sort(grades)}")

