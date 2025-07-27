# import mysql.connector
# from tkinter import messagebox

# #B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q ,R
# def  Save_Data_MySql(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R):
#     # Function implementation here

#     try:
#         mydb = mysql.connector.connect(host='localhost',user ='root',password="992922")
#         mycursor=mydb.cursor()
#         print("Connection stablished!")

#     except:
#         messagebox.showerror("Connection","Database connection not stablished!!")

#     # try:
#     #     print(B)
#     #     print(C)
#     #     print(D)
#     #     print(E)
#     #     print(F)
#     #     print(G)
#     #     print(H)
#     #     print(I)
#     #     print(J)
#     #     print(k)
#     #     print(L)
#     #     print(M)
#     #     print(N)
#     #     print(O)
#     #     print(P)
#     #     print(Q)
#     #     print(R)

#     try:
#         command="create databse Heart_Data"
#         mycursor.execute(command)

#         command="use Heart_Data"
#         mycursor.execute(command)

#         command="create table data(user int auto_increment key not null,Name varchar(50),Date varchar(100),DOB varchar(100),age varchar(100),sex varchar(100),Cp varchar(100),trestbps varchar(100),chol varchar(100),fbs varchar(100),restecg varchar(100),thalach varchar(100),exang varchar(100),oldpeak varchar(100),slope varchar(100),ca varchar(100),thal varchar(100),result varchar(100))"
#         mycursor.execute(command)

#         command="insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q ,R))
#         mydb.commit()
#         mydb.close()
#         messagebox.showinfo("Register","New user added sucessfully!!!")

 
#     except:
#         mycursor.execute("use Heart_Data")
#         mydb=mysql.connector.connect(host="localhost",user='root',password='992922',database='Heart_Data')
#         mycursor=mydb.cursor()

#         command = "insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         mycursor.execute  (command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q ,R))
#         mydb.commit()
#         mydb.close()
#         messagebox.showinfo("Register","New user added sucessfully!!!")

     


# Save_Data_MySql('mr unknown',"08/08/2023","1979","44","1","1","233","233","1","1","233","1","233.0","0","2","1","0")

import mysql.connector  # No unnecessary spaces
from mysql.connector import Error
from tkinter import messagebox

def Save_Data_MySql(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R):
    try:
        # Establish Connection
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password="San@5555"
        )
        if mydb.is_connected():
            print("Database connection established!")
            mycursor = mydb.cursor()
        
        # Create Database If Not Exists
        mycursor.execute("CREATE DATABASE IF NOT EXISTS Heart_Data")
        mycursor.execute("USE Heart_Data")

        # Create Table If Not Exists
        command = """
        CREATE TABLE IF NOT EXISTS data (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(50),
            Date VARCHAR(100),
            DOB VARCHAR(100),
            age VARCHAR(100),
            sex VARCHAR(100),
            Cp VARCHAR(100),
            trestbps VARCHAR(100),
            chol VARCHAR(100),
            fbs VARCHAR(100),
            restecg VARCHAR(100),
            thalach VARCHAR(100),
            exang VARCHAR(100),
            oldpeak VARCHAR(100),
            slope VARCHAR(100),
            ca VARCHAR(100),
            thal VARCHAR(100),
            result VARCHAR(100)
        )
        """
        mycursor.execute(command)

        # Insert Data
        insert_command = """
        INSERT INTO data (Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, result)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        mycursor.execute(insert_command, (B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R))
        mydb.commit()
        
        # Close Connection
        mycursor.close()
        mydb.close()

        messagebox.showinfo("Register", "New user added successfully!")

    except Error as e:
        messagebox.showerror("info", "there is mistake in the above code!!")

# Call the function
Save_Data_MySql('mr unknown', "08/08/2023", "1979", "44", "1", "1", "233", "233", "1", "1", "233", "1", "233.0", "0", "2", "1", "0")

