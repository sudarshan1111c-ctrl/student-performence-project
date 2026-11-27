import csv
import random

# Create a CSV file
with open("students.csv", "w", newline="") as file:

    # Create CSV writer
    writer = csv.writer(file)

    # Write column headings
    writer.writerow([
        "Student_ID",
        "Name",
        "Department",
        "Attendance",
        "Marks",
        "Result"
    ])

    # Generate 20,000 student records
    for i in range(1, 20001):

        student_id = i
        name = "Student_" + str(i)

        department = random.choice([
            "CSD",
            "ISE",
            "CSE",
            "ECE"
        ])

        attendance = random.randint(50, 100)
        marks = random.randint(0, 100)

        if marks >= 35:
            result = "Pass"
        else:
            result = "Fail"

        # Write student details into CSV file
        writer.writerow([
            student_id,
            name,
            department,
            attendance,
            marks,
            result
        ])

print("Student dataset created successfully!")
print("Total student records: 20000")