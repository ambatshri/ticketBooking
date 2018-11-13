from dbconnection import DBConnection


def install():

   dbConn = DBConnection()
   conn = dbConn.connection()
   cur = conn.cursor()



   #creating movie table

   cur.execute('''CREATE TABLE IF NOT EXISTS movies(ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT NOT NULL)''')

   cur.execute("INSERT INTO movies(TITLE) \
            VALUES ('Die Hard 4.0')")

   cur.execute("INSERT INTO movies(TITLE) \
            VALUES ('John Wick')")

   cur.execute("INSERT INTO movies(TITLE) \
            VALUES ('John Wick 2')")                  

   cur.execute('''CREATE TABLE IF NOT EXISTS movie_days(ID INTEGER PRIMARY KEY AUTOINCREMENT, movie_id INTEGER NOT NULL, day TEXT)''')

   cur.execute("INSERT INTO movie_days(movie_id,day) \
            VALUES (1,'TUE')")
   cur.execute("INSERT INTO movie_days(movie_id,day) \
            VALUES (1,'WED')")
   cur.execute("INSERT INTO movie_days(movie_id,day) \
            VALUES (1,'FRI')")
   cur.execute("INSERT INTO movie_days(movie_id,day) \
            VALUES (2,'MON')")
   cur.execute("INSERT INTO movie_days(movie_id,day) \
            VALUES (2,'WED')")
   cur.execute("INSERT INTO movie_days(movie_id,day) \
            VALUES (2,'THUR')")
   cur.execute("INSERT INTO movie_days(movie_id,day) \
            VALUES (2,'FRI')")
   cur.execute("INSERT INTO movie_days(movie_id,day) \
            VALUES (3,'FRI')")

   cur.execute('''CREATE TABLE IF NOT EXISTS movie_timings(ID INTEGER PRIMARY KEY AUTOINCREMENT, day_id INTEGER NOT NULL, time TEXT)''')
   cur.execute('''CREATE TABLE IF NOT EXISTS movie_booking ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `time_id` INTEGER NOT NULL, `row` INTEGER NOT NULL, `col` INTEGER NOT NULL, `username` TEXT NOT NULL )''')
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (1,'09:00')")
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (1,'11:30')")
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (2,'14:00')")         
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (2,'20:00')")
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (3,'22:00')")
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (3,'22:00')")
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (4,'22:00')")
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (4,'22:00')")
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (5,'22:00')")
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (6,'22:00')")                           
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (7,'22:00')")
   cur.execute("INSERT INTO movie_timings(day_id,time) \
            VALUES (8,'22:00')")     
   conn.commit()
   conn.close()

install()