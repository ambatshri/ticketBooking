from dbconnection import DBConnection

class Movie(object):

   def printMovieList(self):
      dbConn = DBConnection()
      cur = dbConn.connection()
      print("#########################\n#\tMovies \t\t#\n#########################")
      query = "SELECT * FROM movies"
      for row in cur.execute(query):
         print("["+str(row[0])+"]","\t",row[1])
      cur.close()
   
   def printMovieDays(self,movie_id):
      dbConn = DBConnection()
      cur = dbConn.connection()
      query = "SELECT id,day FROM movie_days where movie_id = ?"
      for row in cur.execute(query,movie_id):
         print("["+str(row[0])+"]","\t",row[1])
      cur.close()

   def printMovieTimes(self,day_id):
      dbConn = DBConnection()
      cur = dbConn.connection()
      query = "SELECT id,time FROM movie_timings where day_id = ?"
      for row in cur.execute(query,day_id):
         print("["+str(row[0])+"]","\t",row[1])
      cur.close()

   def getMovieTitle(self,id):
      dbConn = DBConnection()
      conn = dbConn.connection()
      cur = conn.cursor()
      query = "SELECT title from movies where id = ?"
      cur.execute(query,id)
      row = cur.fetchone()
      if row:
         return row[0]
      else:
         return False

   def getMovieDay(self,id,movieID):
      dbConn = DBConnection()
      conn = dbConn.connection()
      cur = conn.cursor()
      query = "SELECT day from movie_days where id = {0} AND movie_id = {1}".format(id,movieID)
      cur.execute(query)
      row = cur.fetchone()
      if row:
         return row[0]
      else:
         return False
   
   def getMovieTime(self,id,dayID):
      dbConn = DBConnection()
      conn = dbConn.connection()
      cur = conn.cursor()
      query = "SELECT time from movie_timings where id = {0} and day_id = {1}".format(id,dayID)
      cur.execute(query)
      row = cur.fetchone()
      if row:
         return row[0]
      else:
         return False

   def acceptMovie(self):
      while True:
         try:
            movieID = input("Select Movie: ")
            title = self.getMovieTitle(movieID)
            if title == False:
               raise ValueError("Incorrect Movie, Please select movie again.")
         except ValueError as err:
               print(err)
               continue
         else:
            return (movieID,title)
   
   def acceptMovieDay(self,movieID):
      while True:
         try:
            dayID = input("Select Day: ")
            day = self.getMovieDay(dayID,movieID)
            if day == False:
               raise ValueError("Incorrect Day, Please select day again.")
         except ValueError as err:
               print(err)
               continue
         else:
            return (dayID,day)
   
   def acceptMovieTime(self,dayID):
      while True:
         try:
            timeID = input("Select Time: ")
            time = self.getMovieTime(timeID,dayID)
            if time == False:
               raise ValueError("Incorrect Time, Please select time again.")
         except ValueError as err:
               print(err)
               continue
         else:
            return (timeID,time)
   