import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  #password="pynative@#29",
                                  host="3.17.78.180",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from pg_stat_wal_receiver"
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    records = cursor.fetchall()



    print("Print each row and it's columns values")
    for row in records:
        print("pid = ", row[0], )
        print("status = ", row[1])
        print("sender_host  = ", row[2], "\n")

        if row[1] == "streaming":
            print("Good shit")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

