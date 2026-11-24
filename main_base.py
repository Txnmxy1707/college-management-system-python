import sqlite3

# ================= STUDENT TABLE =================

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT,
    phone TEXT
)
""")

conn.commit()
conn.close()


def addStudent():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    phone = input("Enter Phone Number: ")

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (roll, name, course, phone)
    )

    conn.commit()
    conn.close()

    print("Student Added Successfully")


def viewStudents():
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if len(students) == 0:
        print("No Students Found")
    else:
        for student in students:
            print(f"Roll Number: {student[0]} | Name: {student[1]}")

    conn.close()


def searchStudent():
    roll = int(input("Enter Roll Number: "))

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll = ?",
        (roll,)
    )

    student = cursor.fetchone()

    if student:
        print(f"Roll Number: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Course: {student[2]}")
        print(f"Phone: {student[3]}")
    else:
        print("Student Not Found")

    conn.close()


def deleteStudent():
    roll = int(input("Enter Roll Number to Delete: "))

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE roll = ?",
        (roll,)
    )

    conn.commit()
    conn.close()

    print("Student Deleted Successfully")


def updateStudent():
    roll = int(input("Enter Roll Number: "))
    newName = input("Enter New Name: ")

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name = ? WHERE roll = ?",
        (newName, roll)
    )

    conn.commit()
    conn.close()

    print("Student Updated Successfully")


# ================= ATTENDANCE TABLE =================

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    roll INTEGER,
    date TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Attendance Table Created")


def markAttendance():
    roll = int(input("Enter Roll Number: "))
    date = input("Enter Date (YYYY-MM-DD): ")
    status = input("Enter Status (Present/Absent): ")

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attendance VALUES (?, ?, ?)",
        (roll, date, status)
    )

    conn.commit()
    conn.close()

    print("Attendance Marked Successfully")


def viewAttendance():
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")

    records = cursor.fetchall()

    for record in records:
        print(
            f"Roll: {record[0]} | "
            f"Date: {record[1]} | "
            f"Status: {record[2]}"
        )

    conn.close()


def calculateAttendance():
    roll = int(input("Enter Roll Number: "))

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE roll = ?",
        (roll,)
    )

    totalClasses = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attendance
        WHERE roll = ?
        AND status = 'Present'
        """,
        (roll,)
    )

    presentClasses = cursor.fetchone()[0]

    if totalClasses > 0:
        percentage = (presentClasses / totalClasses) * 100
        print(f"Attendance Percentage: {percentage:.2f}%")
    else:
        print("No Attendance Records Found")

    conn.close()


def minimumAttendance():
    roll = int(input("Enter Roll Number: "))

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE roll = ?",
        (roll,)
    )

    totalClasses = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attendance
        WHERE roll = ?
        AND status = 'Present'
        """,
        (roll,)
    )

    presentClasses = cursor.fetchone()[0]

    if totalClasses > 0:
        percentage = (presentClasses / totalClasses) * 100

        if percentage > 75:
            print("Attendance is above 75%")
        else:
            print("Attendance is below 75%")
    else:
        print("No Attendance Records Found")

    conn.close()


# ================= MARKS TABLE =================

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS marks(
    roll INTEGER,
    python INTEGER,
    dbms INTEGER,
    java INTEGER,
    maths INTEGER
)
""")

conn.commit()
conn.close()

print("Marks Table Created")


def addMarks():
    roll = int(input("Enter Roll Number: "))

    pythonMarks = int(input("Enter Python Marks: "))
    dbmsMarks = int(input("Enter DBMS Marks: "))
    javaMarks = int(input("Enter Java Marks: "))
    mathsMarks = int(input("Enter Maths Marks: "))

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO marks
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            roll,
            pythonMarks,
            dbmsMarks,
            javaMarks,
            mathsMarks
        )
    )

    conn.commit()
    conn.close()

    print("Marks Added Successfully")


def viewMarks():
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM marks")

    records = cursor.fetchall()

    for record in records:
        print(
            f"Roll: {record[0]} | "
            f"Python: {record[1]} | "
            f"DBMS: {record[2]} | "
            f"Java: {record[3]} | "
            f"Maths: {record[4]}"
        )

    conn.close()


def searchMarks():
    roll = int(input("Enter Roll Number: "))

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM marks WHERE roll = ?",
        (roll,)
    )

    record = cursor.fetchone()

    if record:
        print(
            f"Roll: {record[0]} | "
            f"Python: {record[1]} | "
            f"DBMS: {record[2]} | "
            f"Java: {record[3]} | "
            f"Maths: {record[4]}"
        )
    else:
        print("No Marks Found")

    conn.close()


def calculateResult():
    roll = int(input("Enter Roll Number: "))

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM marks WHERE roll = ?",
        (roll,)
    )

    record = cursor.fetchone()

    if record:
        total = (
            record[1] +
            record[2] +
            record[3] +
            record[4]
        )

        percentage = (total / 400) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"

        print("\n===== RESULT =====")
        print(f"Roll Number: {record[0]}")
        print(f"Total Marks: {total}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print("==================")
    else:
        print("No Marks Found For This Student")

    conn.close()


def topScorer():
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT students.name,
           marks.roll,
           marks.python,
           marks.dbms,
           marks.java,
           marks.maths
    FROM students
    JOIN marks
    ON students.roll = marks.roll
    """)

    records = cursor.fetchall()

    highestTotal = 0
    topStudent = ""
    topRoll = 0

    for record in records:
        total = (
            record[2] +
            record[3] +
            record[4] +
            record[5]
        )

        if total > highestTotal:
            highestTotal = total
            topStudent = record[0]
            topRoll = record[1]

    print("\n===== TOP SCORER =====")
    print(f"Name: {topStudent}")
    print(f"Roll Number: {topRoll}")
    print(f"Total Marks: {highestTotal}")

    conn.close()


def top3Scorers():
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT students.name,
           marks.roll,
           marks.python,
           marks.dbms,
           marks.java,
           marks.maths
    FROM students
    JOIN marks
    ON students.roll = marks.roll
    """)

    records = cursor.fetchall()

    studentTotals = []

    for record in records:
        total = (
            record[2] +
            record[3] +
            record[4] +
            record[5]
        )

        studentTotals.append(
            (record[0], record[1], total)
        )

    studentTotals.sort(
        key=lambda x: x[2],
        reverse=True
    )

    print("\n===== TOP 3 SCORERS =====")

    for i in range(min(3, len(studentTotals))):
        print(
            f"Rank {i+1}: "
            f"{studentTotals[i][0]} "
            f"(Roll: {studentTotals[i][1]}) "
            f"- Total: {studentTotals[i][2]}"
        )

    conn.close()


# ================= MENU =================

while True:

    print("\n===================================")
    print("     COLLEGE MANAGEMENT SYSTEM")
    print("===================================")

    print("\n--- STUDENT MODULE ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")

    print("\n--- ATTENDANCE MODULE ---")
    print("6. Mark Attendance")
    print("7. View Attendance")
    print("8. Calculate Attendance")
    print("9. Check Minimum Attendance")

    print("\n--- MARKS MODULE ---")
    print("10. Add Marks")
    print("11. View Marks")
    print("12. Search Marks")
    print("13. Calculate Result")

    print("\n--- ANALYTICS MODULE ---")
    print("14. Top Scorer")
    print("15. Top 3 Scorers")

    print("\n16. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        addStudent()

    elif choice == "2":
        viewStudents()

    elif choice == "3":
        searchStudent()

    elif choice == "4":
        updateStudent()

    elif choice == "5":
        deleteStudent()

    elif choice == "6":
        markAttendance()

    elif choice == "7":
        viewAttendance()

    elif choice == "8":
        calculateAttendance()

    elif choice == "9":
        minimumAttendance()

    elif choice == "10":
        addMarks()

    elif choice == "11":
        viewMarks()

    elif choice == "12":
        searchMarks()

    elif choice == "13":
        calculateResult()

    elif choice == "14":
        topScorer()

    elif choice == "15":
        top3Scorers()

    elif choice == "16":
        print("Thank You For Using College Management System")
        break

    else:
        print("Invalid Choice")
