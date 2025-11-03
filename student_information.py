def main():
    student_info = {}

    student_info['Daniel'] = {
        "student id" : 441236,
       "student gpa" : 4.0,
       "credits completed" : 1000000,
       "student grades" : [70, 80, 90, 100]
    }
    student_info['Austin'] = {
        "student id" : 123456,
        "student gpa" : 4.0,
        "credits completed" : 1,
        "student grades" : [100, 100, 100]
    }
    
    print(student_info)
    
    print("\nList of Students:")
    
    for student in student_info.keys():
        print(student)
    print("\nStudent Information:")
    print("Name\t ID\t GPA\t Credits Completed\t Grades\t")
    
    for student, info in student_info.items():
        print(f"{student}\t{info['student id']}\t{info['student gpa']}\t{info['credits completed']}\t\t\t{info['student grades']}")
    
    print("\nAccessing student information...")

    for student, info in student_info.items():
        print(f"{student}: id {info ['student id']} gpa {info['student gpa']} credits completed {info['credits completed']} student grades {info['student grades']}")

    print("\nAustin has dropped the course. Removing Austin from directory...")
    removed_student = student_info.pop('Austin')
    print("\nUpdated Student List:", student_info)

    print("\nAccessing student GPA information...")
    for student in student_info:
        gpa = student_info.get(student).get("student gpa")
        print(f"{gpa}")
    
    print("\nStudents have graduated! Woohoo! \nClearing the student registry...")
    student_info.clear()
    print(student_info)
    
    print("\nCompleted by Daniel Arterbury AKA Mustache McGee")
    
    
    
    
    
if __name__ == "__main__": 
    main()
    