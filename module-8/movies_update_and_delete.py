import mysql.connector
from mysql.connector import errorcode
from db_config import secrets

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "port": secrets["PORT"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window.
    cursor.execute("""
        SELECT 
            film_name AS Name, 
            film_director AS Director, 
            genre_name AS Genre, 
            studio_name AS 'Studio Name' 
        FROM film 
        INNER JOIN genre ON film.genre_id = genre.genre_id 
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]
        ))

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print(f"Connected to MySQL on {secrets['HOST']}:{secrets['PORT']} as {secrets['USER']}")

   
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    input("\n\nPress Enter to exit...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\nMySQL connection closed.")
