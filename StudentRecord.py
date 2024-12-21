# A program to manage student details:     

def display_options():
    print("\nStudent Records Management \n 1. Add student record\n 2. Update Student records\n 3. Delete student Records\n 4. Display All Records\n 5. Calculate and Display Ranking\n 6. Eixt\n")

def add_student(records):
    student_id = input("Enter Student ID: ")
    if student_id in records:
        print("Student ID already exists!")
        return
 
    subjects = {}
    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        marks = float(input(f"Enter marks for {subject}: "))
        subjects[subject] = marks

    records[student_id] = subjects
    print("Student record added successfully!")


   
def update_student(records):
    student_id = input("Enter Student ID to update: ")
    if student_id not in records:
        print("Student ID not found!")
        return

    print("Current subjects and marks:")
    for subject, marks in records[student_id].items():
        print(f"{subject}: {marks}")

    while True:
        subject = input("Enter subject name to update (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        if subject in records[student_id]:
            marks = float(input(f"Enter new marks for {subject}: "))
            records[student_id][subject] = marks
            print(f"Marks updated for {subject}!")
        else:
            print(f"Subject {subject} not found!")

def delete_student(records):
    student_id = input("Enter Student ID to delete: ")
    if student_id in records:
        del records[student_id]
        print("Student record deleted successfully!")
    else:
        print("Student ID not found!")

def display_all_records(records):
    if not records:
        print("No records to display!")
        return

    for student_id, subjects in records.items():
        print(f"\nStudent ID: {student_id}")
        for subject, marks in subjects.items():
            print(f"  {subject}: {marks}")

def calculate_rankings(records):
    if not records:
        print("No records to process!")
        return


    results =[]
    for student_id, subjects in records.items():
        total_marks = sum(subjects.values())
        percentage = total_marks / len(subjects)
        results.append((student_id, total_marks, percentage))
        
     results.sort(key=lambda x: x[1], reverse=True)

    print("\nRankings:")
    for rank, (student_id, total_marks, percentage) in enumerate(results, start=1):
        print(f"Rank {rank}: Student ID: {student_id}, Total Marks: {total_marks}, Percentage: {percentage:.2f}%")


def main():
    student_records = {}

    while True:
        display_options()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_student(student_records)
        elif choice == '2':
            update_student(student_records)
        elif choice == '3':
            delete_student(student_records)
        elif choice == '4':
            display_all_records(student_records)
        elif choice == '5':
            calculate_rankings(student_records)
        elif choice == '6':
            print("Exiting program. THANK YOU!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
