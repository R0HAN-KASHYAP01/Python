import mysql.connector as mysql  # Statement 1

def sql_data():
    con1 = mysql.connect(host="localhost",user="root",password="tiger", database="School")
    
    mycoursor = con1.cursor()  # statement 2
    print("Students with marks greater than 75 are: ")
    mycoursor.execute("SELECT * FROM STUDENT WHERE MARKS > 75")  # Statement 3
    
    data = mycoursor.fetchone()  # Statement 4
    
    for i in data: 
        print (i)
    print()