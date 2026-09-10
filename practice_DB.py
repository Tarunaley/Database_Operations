import psycopg
conn = psycopg.connect("postgresql://neondb_owner:npg_wuIB2bQi1pkz@ep-falling-tree-a5xezzz6-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
cur = conn.cursor()

list1=input("Enter Id Name Age").split()
list2=input("Enter Id Name Age").split()
list3=input("Enter Id Name Age").split()
cur.execute("""(
create table if not exists student_data(
id int primary key,
name text,
age int
)
)""")
list_all=[list1[0],list2[0],list3[0]]

def valid_id(id):
    return isinstance(id, int) and id > 0 and list_all.count(id)==1


def valid_name(name):
    return isinstance(name, str) and len(name) > 0 and name.isalpha()


def valid_age(age):
    if isinstance(age, (int, float)):
        return age > 0 and age == int(age)

    return False


def insert_data(id,name,age):
    if(valid_id(id) and valid_name(name) and valid_age(age)): 
        validated_name=""
        name_arr=name.split()
        for char in name_arr:
            if(char.isdigit()):
                 validated_name+=char
         cur.execute(
             "INSERT INTO student_data (id, name, age) VALUES (%s, %s, %s)",
            (id, name, age)
        )
insert_data(list1[0],list1[1],list1[2])
       


    