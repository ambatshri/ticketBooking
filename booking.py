import string
from dbconnection import DBConnection
from movie import Movie

class Booking(object):
   
   def getBookedSeatNos(self,time_id):
      dbConn = DBConnection()
      conn = dbConn.connection()
      cur = conn.cursor()
      seat_no = list()
      query = "SELECT row,col from movie_booking where time_id = ?"
      for row in cur.execute(query,time_id):
         seat_no.append(row)
      return seat_no
      
   def generateSeatingArrangement(self,seat_no_list):
      rows = 11
      cols = 16
      Matrix = [["x" if (y,x) in seat_no_list else "-" for x in range(cols)] for y in range(rows) ] 
      count = 0
      for row in Matrix:
         row[0] = str(count)
         count += 1
      columnkeys = list(string.ascii_uppercase[:cols-1])      
      Matrix[0] = ['*'] + columnkeys
      print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in Matrix]))

   def checkSeatAvailability(self,seatNo,time):
      seatNo = list(seatNo.split(','))
      seatNo[0] = int(seatNo[0])
      seatNo[1] = ord(seatNo[1].lower()) - 96
      seat = tuple(seatNo)      
      booked = self.getBookedSeatNos(time)
      if seat in booked:
         return True
      else:
         return False


   def acceptSeatNumber(self,message,time):
      rows = list(range(1,11))
      cols = list(string.ascii_uppercase[:15])
      while True:
         try:
            userInput = input(message)
            userInputList = list(userInput.split(','))
            userInputList[0] = int(userInputList[0])
            if userInputList[0] not in rows:
               raise ValueError("Invalid Row: "+str(userInputList[0]))
            if userInputList[1] not in cols:
               raise ValueError("Invalid Column: "+userInputList[1])
            userInputList[1] = ord(userInputList[1].lower()) - 96
            if self.checkSeatAvailability(userInput,time):
               raise ValueError("Seat Not Available")
         except ValueError as err:
            print(err)
            continue
         else:
            return tuple(userInputList)

   def bookTicket(self,time_id,seatnos,name):
      dbConn = DBConnection()
      conn = dbConn.connection()
      cur = conn.cursor()
      for seat in seatnos:
         (row,col) = seat
         query = "INSERT INTO movie_booking(time_id,row,col,username) values({0},{1},{2},'{3}')".format(time_id,row,col,str(name))
         if cur.execute(query):
            conn.commit()
         else:
            return False
      return True

   def run(self):
      book = Movie()
      book.printMovieList()
      (movieID,title) = book.acceptMovie()
      book.printMovieDays(movieID)
      (dayID, day) = book.acceptMovieDay(movieID)
      book.printMovieTimes(dayID)
      (timeID, time) = book.acceptMovieTime(dayID)
      booked_seats = self.getBookedSeatNos(timeID)
      self.generateSeatingArrangement(booked_seats)
      no_of_seats = int(input("Enter no of seats: "))
      seat_nos = list()
      for count in range(no_of_seats):
         seat = self.acceptSeatNumber("Select your seat no. (ex. 1,E): ",timeID)
         seat_nos.append(seat)
      username = input("Enter your name: ")
      tick = "Ticket's " if no_of_seats > 1 else "Ticket"
      if self.bookTicket(timeID,seat_nos,username):
         print(str(no_of_seats) + " "+ tick +" Successfully Booked for "+ title +" on "+ day +" at " +time+" by "+username)