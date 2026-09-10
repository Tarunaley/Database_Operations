import psycopg
conn = psycopg.connect("postgresql://neondb_owner:npg_wuIB2bQi1pkz@ep-falling-tree-a5xezzz6-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
cur = conn.cursor()

def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)
    conn.commit()
def insert_data(id, name, age):
    cur.execute(
        "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)",
        (id, name, age)
    )
    print("Student inserted successfully!")
    conn.commit()

def delete_student(id):
    cur.execute(
        "DELETE FROM students WHERE id = %s",
        (id,)
    )
    print("Student deleted successfully!")
    conn.commit()

while(True):
    print("====Student Management System=====")
    print("option 1:Create Database")
    print("option 2:Insert Data")
    print("option 3:Delete a student row")
    print("option 4:Exit")
    choice=int(input("Enter Your Choice:"))
    if(choice==1):
        create_table()
    elif(choice==2):
        id=int(input("enter student id:"))
        name=input("enter student name:")
        age=int(input("enter student age:"))
        insert_data(id,name,age)
    elif(choice==3):
        id=int(input("Enter student Id that to be deleted:"))
        delete_student(id)
    elif(choice==4):
        break
    else:
        print("Invalid choice!")

