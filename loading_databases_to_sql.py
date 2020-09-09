import sqlite3
import csv

def airlinetable_connect():
    """Loading Airlines.csv to SQLite"""
    connection = sqlite3.connect('Openflights.db')
    cursor = connection.cursor()

    csv_file = open('airlines.csv', encoding = "utf8")
    rows = csv.reader(csv_file)
    cursor.executemany("INSERT INTO airlines VALUES(?,?,?,?,?,?,?,?)", rows)

    cursor.execute("SELECT * FROM airlines")
    print(cursor.fetchall())
    connection.commit()
    connection.close()

def routetable_connect():
    """Loading Routes.csv to SQLite"""
    connection = sqlite3.connect('Openflights.db')
    cursor = connection.cursor()
    csv_file = open('routes.csv', encoding = "utf8")
    rows = csv.reader(csv_file)
    cursor.executemany("INSERT INTO routes VALUES(?,?,?,?,?,?,?,?,?)", rows)

    cursor.execute("SELECT * FROM routes")
    print(cursor.fetchall())
    connection.commit()
    connection.close()

def airporttable_connect():
    """Loading Airports.csv to SQLite"""
    connection = sqlite3.connect('Openflights.db')
    cursor = connection.cursor()
    
    csv_file = open('airports.csv', encoding = "utf8")
    rows = csv.reader(csv_file)
    cursor.executemany("INSERT INTO airports VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)

    cursor.execute("SELECT * FROM airports")
    print(cursor.fetchall())
    connection.commit()
    connection.close()

airlinetable_connect()
routetable_connect()
airporttable_connect()


