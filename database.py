import sqlite3

conn = sqlite3.connect("data.db")

#creates a cursor
c = conn.cursor()

#creates a table                             # AFTER CREATION OF DATABASE, WE COMMENT THIS PROCESS OUT
#c.execute("""CREATE TABLE data
#(
#    source_email text,
#    verification_code text,
#    destination_email text,
#    time_of_post text,
#    message text,
#    input_file text  
#
#)""")

#   DATATYPES
#NULL - it doesnt exit
#INTEGER - whole nubmer
#REAL - decimel
#TEXT - text/string
#BLOB - image, mp3,...

multiple_data = [   
    ('11','12','13','14'),   # ?,?,?    TUPLE PLACEHOLDER WITH ?
    ('21','22','23','24'),   # ?,?,?
    ('31','32','33','34'),
    ('41','42','43','44'),   # ?,?,?    TUPLE PLACEHOLDER WITH ?
    ('51','52','53','54'),   # ?,?,?
    ('61','62','63','64'),   # ?,?,?
      
      ]

#c.execute ( "INSERT INTO random_data VALUES ('somebodyfells@gmail.com','forlife2004@gmail.com','current_date','blob')")

#c.executemany( "INSERT INTO random_data VALUES (?,?,?,?)", multiple_data )

# Query the Database

#c.execute("SELECT rowid, * FROM random_data")
#c.execute("SELECT rowid, * FROM random_data")
#c.execute("SELECT rowid, * FROM random_data WHERE time_of_post LIKE 'cu%' ")
#c.execute("SELECT rowid, * FROM random_data WHERE time_of_post = '33' ")


#print(c.fetchone()  )                                   #its a tuple, 0 means first item of first row 
#print(c.fetchmany(2) )                                     #2 is number of fetched rows 
#print(c.fetchall())                                       #returns as a python list

#items = c.fetchall()
#print("Email_1 " +  "\t\t Email_2" )
#print("--------  " +  "\t\t--------")
#for item in items:
#    print(item[0] + " " + item [1] + "\t" + item[2] + " " + item[3]) 

#c.execute("""UPDATE random_data SET time_of_post = "changed" WHERE rowid = 5""")
#c.execute("DELETE from random_data WHERE rowid = 4")
#c.execute("SELECT rowid, * FROM random_data WHERE time_of_post LIKE '3%' AND rowid rowid = 3 ")
#c.execute("SELECT rowid, * FROM random_data WHERE time_of_post LIKE '3%' OR rowid rowid = 3 ")
#c.execute("DROP TABLE random_data")  #deletes entire table

#show all data in datatable
def show_all():  
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM data")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()    



#adds new record to table
#def add_one(source_email,destination_email,time_of_post,blob):                                 #email_1,email_2,time,blob
def add_one(source_email,code,destination_email,time_of_post,blob):                                 #email_1,email_2,time,blob
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("INSERT INTO data VALUES (?,?,?,?,?,?)", ( 'source_email','code','destination_email','time_of_post','message','blob'))
    conn.commit()
    conn.close()



#deletes a single given row of data
def delete_one(id):
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("DELETE from data WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


#adds multiple data at a time
def add_many(list):
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.executemany("INSERT INTO data VALUES (?,?,?,?,?,?)", (list))
    conn.commit()
    conn.close()



#look up where is item
def data_lookup(data):
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("SELECT rowid,  * from data WHERE time_of_post = (?)", (data,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()



def delete_all():
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("DELETE from data")
    conn.commit()
    conn.close()

def get_last():
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("SELECT * FROM data ORDER BY rowid DESC LIMIT 1;")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

def get_code():
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("SELECT * FROM data ORDER BY rowid DESC LIMIT 1;")    
    code=c.fetchone()[1]
    return code

def delete_last_input():
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("DELETE FROM data WHERE rowid = (SELECT MAX(rowid) FROM data);")
    conn.commit()
    conn.close()

def get_recepients_email():
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("SELECT * FROM data ORDER BY rowid DESC LIMIT 1;")    
    recepients_email=c.fetchone()[2]
    return recepients_email

def get_file():
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("SELECT * FROM data ORDER BY rowid DESC LIMIT 1;")    
    file=c.fetchone()[4]
    return file

def get_last_returned():
    conn = sqlite3.connect("data.db") 
    c = conn.cursor()
    c.execute("SELECT * FROM data WHERE rowid = (SELECT MAX(rowid) FROM data);")
    zero = c.fetchone()[0]
    c.execute("SELECT * FROM data WHERE rowid = (SELECT MAX(rowid) FROM data);")
    one =  c.fetchone()[1]
    c.execute("SELECT * FROM data WHERE rowid = (SELECT MAX(rowid) FROM data);")
    two =  c.fetchone()[2]
    c.execute("SELECT * FROM data WHERE rowid = (SELECT MAX(rowid) FROM data);")
    tree=  c.fetchone()[3]
    c.execute("SELECT * FROM data WHERE rowid = (SELECT MAX(rowid) FROM data);")
    four=  c.fetchone()[4]
    conn.commit()
    conn.close()
    return zero, one, two,tree, four

#def add_one_last(file_path):
#    conn = sqlite3.connect("data.db") 
#    c = conn.cursor()
#    c.execute("INSERT INTO data VALUES (?,?,?,?,?)", (list))
#    c.fetchone()[4] = file_path
#    conn.commit()
#    conn.close()

# Commit comand
conn.commit()

# Close connection
conn.close()

