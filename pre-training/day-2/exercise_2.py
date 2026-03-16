# Store 5 students as a list of dicts: [{name, scores: [list of scores], subject}].
# Write functions: calculate_average(scores), get_grade(avg), class_topper(students).
# Print a formatted report: student name | avg score | grade. Bold the top scorer's row (add '***
# TOP ***' to their line).
# Bonus: sort the report by average score (descending) without modifying the original list

def calculate_average(scores) -> float:
    return sum(scores) / len(scores)

def get_grade(avg) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    else:
        return "C"

def class_topper(students) -> str:
    top_student = max(students, key=lambda x: calculate_average(x["scores"]))
    return top_student["name"]

students = [
    {"name": "Rohaan", "scores": [85, 90, 88], "subject": "PF"},
    {"name": "Waseeq", "scores": [92, 95, 98], "subject": "SE"},
    {"name": "Rashid", "scores": [70, 75, 72], "subject": "DSA"},
    {"name": "Ali", "scores": [88, 82, 91], "subject": "OOP"},
    {"name": "Hamza", "scores": [60, 65, 58], "subject": "OS"}
]
# Processing and Sorting
topper_name = class_topper(students)

sorted_report = sorted(
    students, 
    key=lambda s: calculate_average(s['scores']), 
    reverse=True
)

print(f"{'Student Name':<15} | {'Avg Score':<10} | {'Grade':<5}")
print("-" * 40)

for student in sorted_report:
    avg = calculate_average(student['scores'])
    grade = get_grade(avg)
    name = student['name']
    
    # Check if this student is the topper
    line = f"{name:<15} | {avg:<10.2f} | {grade:<5}"
    if name == topper_name:
        print(f"{line} *** TOP ***")
    else:
        print(line)
