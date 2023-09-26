
import sqlite3

conn = sqlite3.connect('files.db')

#Creating a table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_computerFiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('files.db')

#This block is inserting the file names into the database
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_computerFiles(file_name) VALUES (?)", \
                ('information.docx',))
    cur.execute("INSERT INTO tbl_computerFiles(file_name) VALUES (?)", \
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_computerFiles(file_name) VALUES (?)", \
                ('myImage.png',))
    cur.execute("INSERT INTO tbl_computerFiles(file_name) VALUES (?)", \
                ('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_computerFiles(file_name) VALUES (?)", \
                ('World.txt',))
    cur.execute("INSERT INTO tbl_computerFiles(file_name) VALUES (?)", \
                ('data.pdf',))
    cur.execute("INSERT INTO tbl_computerFiles(file_name) VALUES (?)", \
                ('myPhoto.jpg',))
    conn.commit()
conn.close()

#This is looping through the tuple to find the file names that
#end with the file extension .txt
conn = sqlite3.connect('files.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_computerFiles (file_name) VALUES (?)", (x,))
            print(x)
