import random
print("Yo yo yo, welcome to Grade Calculator!")
def main():
    total_grades = []

    # while True :
    #     grades = int(input("Enter your grade here: "))
    #     if grades == -1:
    #         break
    #     total_grades.append(grades)

    # grades = int(input("Enter your grade here: "))
    # while grades != -1:
    #    total_grades.append(grades)
    #    grades = int(input("Enter your grade here: "))

    while (grades := int(input("Enter your grade or '-1' to exit:"))) != -1:
        total_grades.append(grades)
        print(total_grades)
    
    else:
        total_grades.pop(total_grades.index(min(total_grades))) , print("Dropping the lowest grade")
        print(total_grades) 
        total_grades.remove((random.choice(total_grades))) , print("Removing a random grade")
        print(total_grades)
        print("Edit a grade:")
        for counter, item in enumerate(total_grades, start=1):
            print(f"{counter}. {item}")
        while(True):
            edits = (int(input("Which grade do you want to edit: "))-1)
            if edits >= len(total_grades) or edits < 0: 
                print("Please enter a valid grade!") 
            else:
                new_grade = int(input("Enter the new grade value: ")) 
                total_grades[edits] = new_grade
                print(total_grades)
                break   
        print("Sorting/Reversing the grades...")
        total_grades.sort()
        total_grades.reverse()
        print(total_grades)

        print("Calculating grade total and grade average...")
        total = sum(total_grades)
        average = total / len(total_grades)
        print("Total of grades:", total)
        print("Average grade:", round(average, 2))       
    print("Bye fam!")
    print("Completed by Daniel Arterbury AKA Mustache McGee")

if __name__ == "__main__":
 main()