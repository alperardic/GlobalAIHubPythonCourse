import json

def get_students_info():
    students_info = {"students": []}
    for i in range(5):
        student = {
            "name": input("Name: "),
            "surname": input("Surname: "),
            "midterm_grade": float(input("Midterm: ")),
            "project_grade": float(input("Project: ")),
            "final_grade": float(input("Final: ")),
            "passing_grade": 0.0
        }
        passing_grade = calculate_grade(student)
        student["passing_grade"] = passing_grade
        students_info["students"].append(student)
    return students_info

def calculate_grade(student):
    return (student["midterm_grade"] * 0.3) + (student["project_grade"] * 0.3) + (student["final_grade"] * 0.4)

def sort_by_passing_grade(students):
    sorted_students={"sorted_students": []}
    for i in range(len(students["students"])):
        max_passing_grade = 0
        for student in students["students"]:
            if student["passing_grade"] >= max_passing_grade:
                max_passing_grade = student["passing_grade"]
                max_student = student
        students["students"].remove(max_student)
        sorted_students["sorted_students"].append(max_student)
    return sorted_students

if __name__ == "__main__":
    students = get_students_info()
    print(json.dumps(sort_by_passing_grade(students)))
        
