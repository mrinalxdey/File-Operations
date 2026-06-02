#Student Enrollment System
print("Student Enrollment System")
available_courses = ("Math", "Science", "History", "English")

students = ["Alice", "Bob", "Charlie"]

enrollment = {
    "Alice": ["Math", "Science"],
    "Bob": ["History"],
    "Charlie": ["English", "Science"]
}
unique_courses = set()

students.append("Diana")
enrollment["Diana"] = ["Math", "History"]

for courses in enrollment.values():
    unique_courses.update(courses)

print("Available Course: ", available_courses)
print("Students: ", students)
print("Enrollment: ", enrollment)
print("Unique courses enrolled: ", unique_courses)