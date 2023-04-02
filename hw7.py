import sqlite3
db = sqlite3.connect('hw7.db')
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS
student(
hobby TEXT,
name TEXT NOT NULL,
lastname TEXT NOT NULL,
br DATE NOT NULL,
mark FLOAT NOT NULL DEFAULT 0.0
)''')

# c.execute('INSERT INTO student VALUES ("fly","Argen","Kydyrovsfdsfds","2004-02-05",4.5)')
# c.execute('INSERT INTO student VALUES ("cycle","Kalys","Belekov","2003-02-29",14.5)')
# c.execute('INSERT INTO student VALUES ("dkjf","kdkf","dkfjk","2000-03-09",3.3)')
# c.execute('INSERT INTO student VALUES ("playfootball","Tolon","Abdybekovdfd","2005-03-02",1)')
# c.execute('INSERT INTO student VALUES ("readbook","Мирлан","Beletbekovf","1999-03-17",5.3)')
# c.execute('INSERT INTO student VALUES ("a;skfls",";skdjf","slfjks","2004-12-15",2.5)')
# c.execute('INSERT INTO student VALUES ("lskfs","lse","kdjls","2008-22-05",8.1)')
# c.execute('INSERT INTO student VALUES ("Миh","lslf","sljkfef","2009-12-10",10.3)')
# c.execute('INSERT INTO student VALUES ("bas","ldsfk","lfdfj","2004-03-03",9.9)')
# c.execute('INSERT INTO student VALUES ("2peiuri","efijf","iweifeijfiejfj","1995-31-01",10.4)')
c.execute("SELECT lastname FROM student WHERE LENGTH(lastname) > 10")
a = c.fetchall()
print(a)
c.execute("UPDATE student SET name='genius' WHERE mark > 10")
c.execute("SELECT * FROM student WHERE name = 'genius'")
b = c.fetchall()
for i in b:
    print(i)
c.execute("DELETE FROM student WHERE rowid%2==0")



# c.execute("SELECT rowid,* FROM user") #rowid чтобы достать свои id
# item = c.fetchall() #достает всех
# for i in item:
#     print(i)
# print(c.fetchone()) #достает первую
# print(c.fetchmany(4)) #достает сколько указано
db.commit() #сохранение
db.close()