import mysql.connector
from mysql.connector import Error

def get_db():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='default',
                                             user='root',
                                             password='12345678')
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:

        print("Error while connecting to MySQL", e)

# if __name__ == "__main__":
#     get_db()