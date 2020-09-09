import sqlite3

"""This file shows the data types, fields that each table will be creating on SQLite"""

try:
    sql_connection = sqlite3.connect('Openflights.db')
    
    """Creating Airport table"""
    sql_create_airport_table = '''CREATE TABLE Airports (
                        AirportID INTEGER PRIMARY KEY,
                        name TEXT, city TEXT,
                        country TEXT, IATA TEXT,
                        ICAO TEXT, Latitude REAL,
                        Longitude REAL, Altitude REAL,
                        Timezone REAL, DST TEXT,
                        Timezone_database_time_zone TEXT,
                        Type TEXT, Source TEXT);'''
    
    """Creating Airline table"""
    sql_create_airline_table = '''CREATE TABLE Airlines (
                                AirlineID INTEGER PRIMARY KEY,
                                name TEXT, alias TEXT,
                                IATA TEXT, ICAO TEXT,
                                Callsign TEXT, country TEXT,
                                active TEXT)'''

    """Creating Routes table"""
    sql_create_routes_table = '''CREATE TABLE Routes (
                                Airline TEXT, AirlineID INTEGER,
                                SourceAirport TEXT,
                                SourceAirportID INTEGER,
                                DestinationAirport TEXT,
                                DestinationAirportID INTEGER,
                                Codeshare TEXT, Stops INTEGER,
                                Equipment TEXT,
                                FOREIGN KEY (AirlineID) REFERENCES Airlines (AirlineID),
                                FOREIGN KEY (SourceAirportID) REFERENCES Airports (AirportID),
                                FOREIGN KEY (DestinationAirportID) REFERENCES Airports (AirportID),
                                FOREIGN KEY (SourceAirport) REFERENCES Airports (IATA),
                                FOREIGN KEY (DestinationAirport) REFERENCES Airports (IATA),
                                FOREIGN KEY (Airline) REFERENCES Airlines(IATA)
                                )'''
    

    cursor = sql_connection.cursor()
    print("Successfully connected to SQLite")
    cursor.execute(sql_create_airport_table)
    cursor.execute(sql_create_airline_table)
    cursor.execute(sql_create_routes_table)
    sql_connection.commit()
    print("SQLite tables created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating table", error)
finally:
    if(sql_connection):
        sql_connection.close()
        print("sqlite connection is closed")
