print("========Enter student details=====")
name = input("Enter Student Name:")
subjects = ["Maths", "Science", "English","Economics","AI"]
marks = []
for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject}:"))
            if mark <0 or mark > 100:
                print("Invalid marks.")
            else :
                marks.append(mark)
                break
        except ValueError:
            print("Please enter a valid number.")
total = sum(marks)
percentage = total / len(subjects)
highest_marks = max(marks)
lowest = min(marks)
passed_subjects = 0
failed_subjects = 0
for i in range(len(subjects)):
    if marks[i]>= 35:
        passed_subjects += 1
    else:
        failed_subjects += 1
print("=======STUDENT REPORT CARD=====")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest)
print("Passed Subjects:", passed_subjects)
print("Failed Subjects:", failed_subjects)
