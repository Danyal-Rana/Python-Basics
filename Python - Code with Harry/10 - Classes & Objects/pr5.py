class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print (f"The name of train is {self.name}")
        print (f"The number of available seats are {self.seats}")

    def getFareInfo(self):
        print (f"The price of ticket is Rs. {self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print (f"Your seat is booked. Your seat no. is: {self.seats}. Have a safe journey :) ")
            self.seats = self.seats - 1 
        else:
            print ("Sorry, This train is full! Kindly try for other trains.")

# this part has to be improve (with the help of sets or lists may be)
    def ticketcancel(self):
        c = input("Do you want to cancel the ticket (yes or no) ? ")
        if c == 'no':
            pass
        elif c == 'yes':
            print (f"Your ticket has been cancelled.")
            self.seats = self.seats + 1
        else:
            print ("You entered the wrong command :)")


intercity = Train("Pindi Express", 100, 500)
intercity.getStatus()
intercity.getFareInfo()
intercity.bookTicket()
intercity.getStatus()
intercity.ticketcancel()
intercity.getStatus()