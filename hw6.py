import sqlite3
from sqlite3 import Error


def create(d):
    cre = False
    try:
        cre = sqlite3.connect(d)
    except Error as e:
        print(e)
    return cre


def ct(cre, sql):
    try:
        cursor = cre.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)



def del1(deleted):
    try:
        sql_del =  sqlite3.connect('hw.db')
        cursor = sql_del.cursor()

        sql__del = """DELETE from man where rowid>1"""
        cursor.execute(sql__del)
        sql_del.commit()
    except Error as e:
        print(e)



def rd(cre):
    try:
        sql='SELECT * FROM man'
        cursor = cre.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()

        for i in rows:
            print(i)
    except Error as e:
        print(e)




def cm(cre, man_):
    sql = '''INSERT INTO man (name,age,hobby,b_date,is_married)
    VALUES (?,?,?,?,?)
    '''
    try:
        cursor=cre.cursor()
        cursor.execute(sql,man_)
        cre.commit()
    except Error as e:
        print(e)
#
#
db = r'hw.db'
#
sql_create_table = '''
CREATE TABLE man(
name TEXT NOT NULL,
age INTEGER,
hobby TEXT,
b_date DATE NOT NULL ,
is_married BOOLEAN
);
'''

created = create(db)
if created is not None:
    # ct(created, sql_create_table)
    # cm(created,('Tolon',18,'playfootball','2005-03-02',False))
    del1(created)
    rd(created)
    print('все работает')