# Import the sqlite3 module
import sqlite3
from tabulate import tabulate

# Setup a connection with our database file
try:
    connection = sqlite3.connect('file:movies.db?mode=rw', uri=True)
    c = connection.cursor()
except sqlite3.OperationalError:
    connection = sqlite3.connect('movies.db')
    c = connection.cursor()
    statement = """CREATE TABLE movies (
	mov_name VARCHAR(20) PRIMARY KEY,
	actor VARCHAR(20),
	actress VARCHAR(30),
	year INTEGER(4),
	director DATE
);"""
    # Execute a statement
    c.execute(statement)

    # Insertion
    c.execute("""INSERT INTO movies VALUES ("Oblivion","Tom Cruise","Olga Kurylenko",2013,"Joseph Kosinski");""")
    c.execute("""INSERT INTO movies VALUES ("Unknown","Liam Neeson","Diane Kruger",2011,"Jaume Collet-Serra");""")
    c.execute("""INSERT INTO movies VALUES ("The Commutor","Liam Neeson","Vera Farmiga",2018,"Jaume Collet-Serra");""")
    c.execute("""INSERT INTO movies VALUES ("Taken","Liam Neeson", "Maggie Grace",2010,"Olivae Megaton");""")
    c.execute("""INSERT INTO movies VALUES ("Green Lantern","Ryan Reynolds","Blake Lively",2011,"Martin Campbell");""")
    c.execute("""INSERT INTO movies VALUES ("The Blind Side","Tim McGraw","Sandra Bullock",2010,"JohnLee Hancock");""")
    c.execute(
        """INSERT INTO movies VALUES ("Prince of Persia","Jake Gyllenhaal", "Gemma Arterton",2010,"Mike Newell");""")
    c.execute("""INSERT INTO movies VALUES ("Source Code","Jake Gyllenhaal", "Vera Farmiga",2011,"Duncan Jones");""")
    c.execute("""INSERT INTO movies VALUES ("Salt"," Liev Schreiber","Angelina Jolie",2010,"Phillip Noyce");""")
    c.execute("""INSERT INTO movies VALUES ("Kinght and Day","Tom Cruise", "Cameron Diaz",2010,"James Mangold");""")
    c.execute("""INSERT INTO movies VALUES ("Edge of Tommorow","Tom Cruise","Emily Blunt",2014,"Doug Liman");""")
    c.execute("""INSERT INTO movies VALUES ("Transcendence","Johnny Depp","Rebecca Hall",2014,"Wally Pfister");""")
    c.execute("""INSERT INTO movies VALUES ("Jason Bourne","Matt Damon", "Julia Stiles",2016,"Paul GreenGrass");""")
    c.execute(
        """INSERT INTO movies VALUES ("The Good Shepherd","Matt Damon", "Angelina Jolie",2006,"Robert DE Niro");""")
    c.execute("""INSERT INTO movies VALUES ("Gravity","George Cloonry","Sandra Bullock",2013,"Alfonso Cuaron");""")
    c.execute("""INSERT INTO movies VALUES ("Speed","Keanu Reeves","Sandra Bullock",1994,"Jan De Bont");""")
    c.execute("""INSERT INTO movies VALUES ("DeadPool","Ryan Reynolds","Morena Baccarin",2016,"Tim Miller");""")
    c.execute("""INSERT INTO movies VALUES ("Free Guy","Ryan Reynolds","Jodie Comer",2021,"Shawn Levy");""")
    connection.commit()

flag = True
while (flag == True):
    print('Menu:\n1)Show All\n2)Select Movies by Actor\n3)Select Movies by Actress\nPress any key to Exit')
    ch = int(input())

    if ch == 1:
        result = c.execute("""SELECT * FROM movies""")
        result = result.fetchall()
        print(tabulate(result, headers=["Movie", "Actor", "Actress", "Year", "Director"]))

    elif ch == 2:
        print("Enter Actor name")
        actor = (input(),)
        result = c.execute("""SELECT mov_name,year,director
              FROM movies
              WHERE actor = ?""", actor)
        result = result.fetchall()
        print(tabulate(result, headers=["Movie", "Year", "Director"]))

    elif ch == 3:
        print("Enter Actress name")
        actress = (input(),)
        result = c.execute("""SELECT mov_name,year,director
              FROM movies
              WHERE actress = ?""", actress)
        result = result.fetchall()
        print(tabulate(result, headers=["Movie", "Year", "Director"]))

    else:
        flag = False
# Save + close the database, never skip this
# or nothing will be saved!
connection.commit()
connection.close()