class Train:
    def __init__(slf, name, fare, seats):
        slf.name = name
        slf.fare = fare
        slf.seats = seats

    def getStatus(slf):
        print (f"The name of train is {slf.name}")
        print (f"The number of available seats are {slf.seats}")

    def getFareInfo(slf):
        print (f"The price of ticket is Rs. {slf.fare}")

    def bookTicket(slf):
        if (slf.seats>0):
            print (f"Your seat is booked. Your seat no. is: {slf.seats}. Have a safe journey :) ")
            slf.seats = slf.seats - 1 
        else:
            print ("Sorry, This train is full! Kindly try for other trains.")

# this part has to be improve (with the help of sets or lists may be)
    def ticketcancel(slf):
        c = input("Do you want to cancel the ticket (yes or no) ? ")
        if c == 'no':
            pass
        elif c == 'yes':
            print (f"Your ticket has been cancelled.")
            slf.seats = slf.seats + 1
        else:
            print ("You entered the wrong command :)")


intercity = Train("Pindi Express", 100, 500)
intercity.getStatus()
intercity.getFareInfo()
intercity.bookTicket()
intercity.getStatus()
intercity.ticketcancel()
intercity.getStatu()