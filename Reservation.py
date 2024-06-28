from time import sleep as s
import random

class Railway:
    seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    coach = "S1"
    fare = random.randint(200,1000)
    print("\n***** WELCOME TO INDIAN RAILWAYS *****\n")

    def __init__(self, name, trainName, fromStation, toStation, dateOfJourney):
        self.name = name
        self.trainName = trainName
        self.fromStation = fromStation
        self.toStation = toStation
        self.dateOfJourney = dateOfJourney

        while True:
            print("\n---------------------------")
            print("\nSelect Option... \
            \n1 . Check Status\
            \n2 . Book Ticket\
            \n3 . Cancel Ticket")
            n = int(input(">"))

            if n == 1:
                self.getStatus()
                print("\n---------------------------")
                print("(for Return press 1, for Exit press 0)")
                m=int(input(">"))
                if m==0:
                    break
                else:
                    continue

            elif n == 2:
                self.bookTicket()
                print("\n---------------------------")
                print("(for Return press 1, for Exit press 0)")
                m=int(input(">"))
                if m==0:
                    break
                else:
                    continue

            elif n == 3:
                a=int(input("Enter Your Ticket Number : "))
                self.cancelTicket(a)
                print("\n---------------------------")
                print("(for Return press 1, for Exit press 0)")
                m=int(input(">"))
                if m==0:
                    break
                else:
                    continue

    @classmethod
    def fillInfo(cls, string):
        return cls(*string.split("  "))

    @staticmethod
    def wait():
        a = "\nPlease_Wait...\n"
        for i in a:
            s(0.1)
            print(i, end="", flush=True)
        s(1)

    def getStatus(self):
        print("\n---------------------------")
        s(1)
        print("TRAIN STATUS...")
        print(f"Name of Train -  {self.trainName}")
        print(f"No. of Seats Available -  {len(self.seats)} on date {self.dateOfJourney}")
        print(
            f"Fare from {self.fromStation} to {self.toStation} - {self.fare}/- Rs.")

    def bookTicket(self):
        print("\n---------------------------")

        if len(self.seats) <= 0:
            print("Sorry, Seats are Not Available...")
        else:
            print("TICKET BOOKING")
            s(1)
            print("Verify Your Details...\n")
            print(f"Name of Passenger - {self.name}")
            print(f"Name of Train     -  {self.trainName}")
            print(
                f"Reservation - From {self.fromStation} to {self.toStation}")
            print(f"Date of Journey - {self.dateOfJourney}")
            print(f"Fare - {self.fare}/- Rs.")
            print("\n---------------------------")
            s(1)
            print("Make Payment... \n(press 1 to make Payment, else press 0)")
            n = int(input(">>>"))
            if n == 1:
                upi = input("Enter UPI ID : ")
                pin = int(input("Enter UPI PIN : "))
                self.wait()
                print("\n---------------------------")
                print("TICKET BOOKED SUCCESSFULLY...")
                print(f"\nName of Passenger - {self.name}")
                print(f"Name of Train       -  {self.trainName}")
                print(
                    f"Reservation From {self.fromStation} to {self.toStation}")
                print(f"Date of Journey - {self.dateOfJourney}")
                print(f"Fare - {self.fare}/- Rs.")
                print(
                    f"Status - CONFIRMED | Coach - {self.coach} | Seat - {self.seats[-1]} |")
                Railway.seats.pop()
            else:
                print("Transaction Cancelled...")

    def cancelTicket(self, ticketNumber):
        Railway.seats.append(ticketNumber)
        print("\n---------------------------")
        print("TICKET CANCELATION")
        s(1)
        print("Verify Your Details...\n")
        print(f"Name of Passenger - {self.name}")
        print(f"Name of Train     - {self.trainName}")
        print(
            f"Reservation         - From {self.fromStation} to {self.toStation}")
        print(
            f"Coach - {self.coach} | Seat - {self.seats[-1]} |")
        print(f"Date of Journey - {self.dateOfJourney}")
        print(f"Amount Paid - {self.fare}/- Rs.")
        print("\n---------------------------")
        print("Do You Want to Cancel...\n(press 1 to Cancel, else press 0)")
        n = int(input(">>>"))
        if n == 1:
            self.wait()
            print("\n---------------------------")
            print("TICKET CANCELLED SUCCESSFULLY...")
            print(f"\nAMOUNT REFUNDED - {self.fare}-60(Cancelation Charges) \
                    \nTotal - {self.fare-60}/- Rs. Refunded...")

        else:
            print("Ticket Not Cancelled...")


name                    = (input("Your Name              : ").upper())
trainName            = (input("Train Name / Number    : ").upper())
reservationFrom   = (input("Reservation From       : ").upper())
reservationUpto    = (input("Reservation Upto       : ").upper())
dateOfJourney      = (input("Date of Journey        : ").upper())

Name = Railway(name, trainName, reservationFrom,
               reservationUpto,dateOfJourney)
