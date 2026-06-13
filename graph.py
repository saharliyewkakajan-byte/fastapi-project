import os

import psycopg2

def get_connection():
    return psycopg2.connect(os.environ["DATABASE_URL"])
conn = get_connection()

cur = conn.cursor()

# # Studentalr barada
# cur.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     age INTEGER NOT NULL,
#     grade VARCHAR(10)
#     );
#             """)



# def Add_student():
    
#     name = input("Name: ")
#     age = int(input("Age: "))
#     grade = input("Grade: ")

#     cur.execute(
#         "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)",
#         (name, age, grade)
#     )
#     print("Students are added successfully!")
#     conn.commit()





# def Show_students():
#     cur.execute("SELECT * FROM students ORDER BY id")
#     rows = cur.fetchall()
    
#     print("Students:")
#     for row in rows:
#         if row[3] == "True":
#             row = list(row)
#             row[3] = "Active"
#         else:
#             row = list(row)
#             row[3] = "Deleted"
#         print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
#     conn.commit()




# def Update_student():
#     cur.execute(
#         "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = 3",
#         ("Ayna", 19, "False")
#     )
#     print("Student is updated successfully!")
#     conn.commit()




# def Delete_student():
#     cur.execute("DELETE FROM students WHERE id = 1")
#     conn.commit()




# def Menu():
#     while True:
#         print("\nMenu:")
#         print("1. Add Student")
#         print("2. Show Students")
#         print("3. Update Student")
#         print("4. Delete Student")
#         print("5. Exit")

#         choice = input("Choice >>> ")

#         if choice == "1":
#             Add_student()
#         elif choice == "2":
#             Show_students()
#         elif choice == "3":
#             Update_student()
#         elif choice == "4":
#             Delete_student()
#         elif choice == "5":
#             break
#         else:
#             print("Tapylmady!")











# ====================== TABLE ======================
# Hasabatlar barada
cur.execute("""
CREATE TABLE IF NOT EXISTS hereketler (
    id SERIAL PRIMARY KEY,
    Sebap VARCHAR(100) NOT NULL,
    Cykdayjy INTEGER NOT NULL,
    Senesi TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    );
            """)

# cur.execute("""
# CREATE TABLE IF NOT EXISTS girdeyjy (
#     id SERIAL PRIMARY KEY,
#     Girdeyjy INTEGER NOT NULL,
#     Senesi TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
#     );
#             """)

# cur.execute("""
# CREATE TABLE IF NOT EXISTS categories (
#     id SERIAL PRIMARY KEY,
#     Name VARCHAR(100) NOT NULL
#     );
#             """)

# ====================== FUNCTIONS ======================
def Add_hereket():
    cur.execute("SELECT * FROM categories")
    rows = cur.fetchall()

    for i, category in enumerate(rows, start=1):
        print(f"{i}. {category[1]}")

    sebap = input("Kategoriya sayla (1-7): ")

    categories = {
        "1": "Taksi",
        "2": "CSGO",
        "3": "Okuwda",
        "4": "Kursda",
        "5": "Market sowda",
        "6": "Koshi shashlyk"
    }

    if sebap in categories:
        sebap = categories[sebap]
    elif sebap == "7":
        sebap = input("Sebap yaz: ")

        cur.execute(
            "INSERT INTO categories (Name) VALUES (%s)",
            (sebap,)
        )
        conn.commit()
        print("Added successfully!")
    else:
        print("Yalnys saylaw!")
        return

    print("Saylanan kategoriya:", sebap)
# Çykdaýjy
    cykdayjy = int(input("Çykdaýjy näçe? : "))
    ans = input("Toçno şony sowdiňmy? (Hawa/Ýok): ")
    if ans == "Hawa":
        print("Okay! 🤝")

        cur.execute(
            "INSERT INTO hereketler (Sebap, Cykdayjy) VALUES (%s, %s)",
            (sebap, cykdayjy)
        )
        print("Sebap is added successfully!👍")
        conn.commit()
    else:
        print("Try again! ❌")


# Girdeýjy goşmak
def Add_income():
    income = int(input("Girdeýjy näçe? : "))
    
    cur.execute(
        "INSERT INTO girdeyjy (Girdeyjy) VALUES (%s)",
        (income,)
    )
    print("Girdeýjy is added successfully!")


# Girdeýjy gormek
def Show_income():
    cur.execute("SELECT * FROM girdeyjy ORDER BY id")
    rows = cur.fetchall()

    print("Girdeyjy:")
    for row in rows:
        print(f"ID: {row[0]}, Girdeyjy: {row[1]}, Senesi: {row[2]}")
    conn.commit()


def Show_hereket():
    cur.execute("SELECT * FROM hereketler ORDER BY id")
    rows = cur.fetchall()

    print("Hereketler:")
    for row in rows:
        print(f"ID: {row[0]}, Sebap: {row[1]}, Çykdaýjy: {row[2]}, Senesi: {row[3]}")

def Summ_hereket():
    cur.execute("SELECT SUM(Cykdayjy) FROM hereketler")
    cykdayjy_sum = cur.fetchall()[0][0]
    print(f"Total Çykdaýjy: {cykdayjy_sum}")
    conn.commit()

# ====================== MENU ======================
def Menu_hereket():
    while True:
        print("\nMenu:")
        print("1. Add Hereket")
        print("2. Add Income")
        print("3. Show Income")
        print("4. Show Hereketler")
        print("5. Summary Hereketler")
        print("6. Exit")

        choice = int(input("Choice >>> "))

        if choice == 1:
            Add_hereket()
        elif choice == 2:
            Add_income()
        elif choice == 3:
            Show_income()
        elif choice == 4:
            Show_hereket()
        elif choice == 5:
            Summ_hereket()
        elif choice == 6:
            break
        else:
            print("Tapylmady! 👎")











# # Isler barada
# cur.execute("""
# CREATE TABLE IF NOT EXISTS isler (
#     id SERIAL PRIMARY KEY,
#     title TEXT NOT NULL,
#     status TEXT DEFAULT 'todo',
#     Senesi TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
#     );
#         """)


# def Add_isler():
#     etmeli_zatlar = input("Etmeli zatlary ýazyň: ")

#     cur.execute(
#         "INSERT INTO isler (title) VALUES (%s)",
#         (etmeli_zatlar,)

#     )
#     print("Isler are added successfully!")
#     conn.commit()


# def Show_isler():
#     cur.execute("SELECT * FROM isler ORDER BY id")
#     rows = cur.fetchall()
#     for row in rows:
#         print(f"ID: {row[0]}, Title: {row[1]}, \nStatus: {row[2]}, \nSenesi: {row[3]} \n")
#     conn.commit()




# def Update_isler():
#     answer = input("Isler tamamlandymy? (True/False): ")
#     sany = int(input("Naçinji (ID) tamamlandy? : "))
#     cur.execute(
#         "UPDATE isler SET status = %s WHERE id = %s",
#         (answer, sany)
#     )
#     print("Isler is updated successfully!")
#     conn.commit()


# def Menu_isler():
#     while True:
#         print("\nMenu:")
#         print("1. Add isler")
#         print("2. Show isler")
#         print("3. Update isler")
#         print("4. Exit")
#         chooise = int(input("Choice >>> "))
#         if chooise == 1:
#             Add_isler()
#         elif chooise == 2:
#             Show_isler()
#         elif chooise == 3:
#             Update_isler()
#         elif chooise == 4:
#             break
#         else:
#             print("Tapylmady!")
# Menu_hereket()
# Close the cursor and connection
cur.close()
conn.close()
if __name__ == "__main__":
    Menu_hereket()