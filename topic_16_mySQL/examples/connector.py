import mysql.connector
from mysql.connector import errorcode

try:
    my_db = mysql.connector.connect(user='admin', password='password',
                                    host='127.0.0.1',
                                    database='database')

    print(my_db)

    my_cursor = my_db.cursor()

    my_cursor.execute("SELECT * FROM Salaries LIMIT 10")

    my_result = my_cursor.fetchall()

    for x in my_result:
        print(x)

    print('*' * 200)

    my_cursor.execute("SELECT JobTitle, COUNT(*) AS Num FROM database.Salaries "
                      "WHERE JobTitle LIKE '%police%' GROUP BY JobTitle ORDER BY Num DESC")

    my_result = my_cursor.fetchall()

    for x in my_result:
        print(x)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    my_db.close()
