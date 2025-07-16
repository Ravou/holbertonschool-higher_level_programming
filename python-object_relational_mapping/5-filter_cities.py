#!/usr/bin/python3
"""
Script to list all cities of a state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def connectBDD(user, password, db_name):
    """
    Function to connect to the MySQL database
    """
    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    return connect


if __name__ == "__main__":
    # Get the arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = connectBDD(mysql_user, mysql_password, mysql_db)

    # Create a cursor to execute the query
    cursor = db.cursor()

    # SQL query to fetch cities from the specified state
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the query
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    cities = cursor.fetchall()

    # Create a list of city names
    city_names = [city[0] for city in cities]

    # Print the city names separated by commas
    print(", ".join(city_names))

    # Close cursor and database connection
    cursor.close()
    db.close()
