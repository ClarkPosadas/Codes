import mysql.connector
from mysql.connector import Error


def connect():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )

        if mydb.is_connected():
            print("Connected to database")
            return mydb
    except Error as e:
        print("Database Connection Failed:", e)
        return None


def addrecords(mydb):
    print("\nADD RECORD")

    name = input("Enter your name: ")
    section = input("Enter section: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    try:
        mycursor = mydb.cursor()

        sql = """
              INSERT INTO students (name, section, phone, email)
              VALUES (%s, %s, %s, %s)
              """

        values = (name, section, phone, email)

        mycursor.execute(sql, values)
        mydb.commit()

        print("Record added")
    except Error as e:
        print("Error:", e)

    finally:
        mycursor.close()


def updaterecords(mydb):
    print("\nUPDATE RECORDS")
    mycursor = mydb.cursor()
    try:
        command = input("Search by ID or by NAME?: ").lower()
        if command == "name":
            name = input("Enter the name of the user to be updated: ")

            sql = """
                  SELECT *
                  FROM students
                  WHERE name = %s \
                  """
            values = (name,)
        elif command == "id":
            studentid = input("Enter ID: ")

            sql = """
                  SELECT *
                  FROM students
                  WHERE id = %s \
                  """
            values = (studentid,)
        else:
            print("Invalid input")
            return

        mycursor.execute(sql, values)
        student = mycursor.fetchone()
        if student is None:
            print("Student not found")
            return

        print("Leave the field blank if you don't want any changes")

        studentid = student[0]
        print(f"ID: {student[0]}")
        name = input(f"Name [{student[1]}]: ")
        section = input(f"Section [{student[2]}]: ")
        phone = input(f"Phone [{student[3]}]: ")
        email = input(f"Email [{student[4]}]: ")

        if name == "":
            name = student[1]
        if section == "":
            section = student[2]
        if phone == "":
            phone = student[3]
        if email == "":
            email = student[4]

        sql = """
              UPDATE students
              SET name    = %s,
                  section = %s,
                  phone   = %s,
                  email   = %s
              WHERE id = %s
              """
        values = (name, section, phone, email, studentid)
        mycursor.execute(sql, values)
        mydb.commit()

        print("Record updated")
    except ValueError:
        print("Input a valid input: ")
    except Error as e:
        print("Error: ", e)
    finally:
        mycursor.close()


def deleterecords(mydb):
    print("\nDELETE RECORDS")
    mycursor = mydb.cursor()
    try:
        command = input("Search by ID or by NAME?: ").lower()
        if command == "name":
            name = input("Enter the name of the user to be updated: ")

            sql = """
                  SELECT * \
                  FROM students \
                  WHERE name = %s \
                  """
            values = (name,)
        elif command == "id":
            studentid = input("Enter ID: ")

            sql = """
                  SELECT * \
                  FROM students \
                  WHERE id = %s \
                  """
            values = (studentid,)
        else:
            print("Invalid input")
            return

        mycursor.execute(sql, values)
        student = mycursor.fetchone()
        if student is None:
            print("Student not found")
            return

        studentid = student[0]

        sql = """
              DELETE
              FROM STUDENTS
              WHERE id = %s \
              """
        values = (studentid,)

        print(f"ID: [{student[0]}]")
        print(f"Name: [{student[1]}]")
        print(f"Section: [{student[2]}]")
        print(f"Phone: [{student[3]}]")
        print(f"Email: [{student[4]}]")
        command = input("Do you want to delete the record? (y/n): ").lower()
        if command == "n":
            print("Cancelled")
            return
        elif command == "y":
            mycursor.execute(sql, values)
            mydb.commit()
            print("Record deleted")
        else:
            print("Invalid input")
            return

    except ValueError:
        print("Input a valid input: ")
    except Error as e:
        print("Error: ", e)
    finally:
        mycursor.close()

def viewrecords(mydb):
    print("\nVIEW RECORDS")
    mycursor = mydb.cursor()
    try:
        sql = """
        SELECT * FROM STUDENTS
              """
        mycursor.execute(sql)
        students = mycursor.fetchall()

        if students is None:
            print("Student not found")
            return

        print("-" * 70)
        print(f"{'ID':<5}{'Name':<25}{'Section':<15}{'Phone Number':<20}")
        print("-" * 70)

        for student in students:
            print(
                f"{student[0]:<5}"
                f"{student[1]:<25}"
                f"{student[2]:<15}"
                f"{student[3] or 'N/A':<20}"
            )

        print("-" * 70)

    except ValueError:
        print("Input a valid input: ")
    except Error as e:
        print("Error: ", e)
    finally:
        mycursor.close()
#e\tests