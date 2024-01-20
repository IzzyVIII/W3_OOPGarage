# Team Mozzy (Mo and Liz)
# Project OOP Parking Garage

# Here are some guidelines on constructing your Garage. Your Garage does not need to do exactly this.
# BUT! It should be robust enough for the user to interact with as if they were entering and leaving a parking garage. 
# - take_ticket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parking_spaces available by 1
# - pay_for_parking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "current_ticket" dictionary key "paid" to True
# -leave_garage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parking_spaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# Some example attributes:
# - tickets -> list
# - parking_spaces -> list
# - current_ticket -> dictionary

from time import sleep

class Parking_garage():
    
    print("\n")
    print("Welcome to Mozzy Garage, where your car will be in great hands! ")

    def __init__(self):
        self.ticket_available = 20
        self.parking_available = 20
        self.current_ticket = {}

    def take_ticket(self):
        
        if self.ticket_available == 0 and self.parking_available == 0:
            print("Sorry! No parking available.")
            return

        else:
            print("Thank you! Please take a Mozzy Ticket!")
            self.current_ticket[self.ticket_available] = ""
            print(f"Your ticket number is: {self.ticket_available}")
            self.ticket_available -= 1
            self.parking_available -= 1
            print("Enjoy your Mozzy stay!")
           
            
    def pay_ticket(self):

        ticket_number = int(input("Please input your ticket number: "))
        time = input("Plese enter how long was your stay? Enter '1' for less than 1 hour, '2' for less than 6 hours, or '3' for anything more than 6 hours: ")
        if time == '1':
            self.current_ticket[ticket_number] = 25
        elif time == '2':
            self.current_ticket[ticket_number] = 50
        else:
            self.current_ticket[ticket_number] = 75
    
        print("Your ticket price is:")
        sleep(2)
        print("....calculating....")
        sleep(2)
        print(f"${self.current_ticket[ticket_number]}! ")
        while True:
            paying = int(input(f"Please input dollar amount of {self.current_ticket[ticket_number]}:  $"))
        
            if paying != self.current_ticket[ticket_number]:
                print("Please enter the correct amount given.")
                continue
            else: 
                print("Thank you for paying an arm and leg!  You now have 15 mins to leave :D ")
                self.current_ticket[ticket_number] = True
                break


    def leave_garage(self):
       
        parking_paid = int(input("Please enter your Mozzy Ticket number... pretty please! "))
       
        for key, value in self.current_ticket.items():
            if key == parking_paid:
                if value != True:
                    print("You didnt pay your ticket yet")
                    self.run()
                else:
                    print("Thank you for using Mozzy Garage!  Please come back again!")
                    self.ticket_available += 1
                    self.parking_available += 1
                    # didnt put a self.run() here because we didnt want to keep them here forever 
                    # ex: Hotel California where you can check out anytime you like, but you can never leave.....


    def run(self):
    
        while True:
            choice = input("What would you like to do?  Park / Pay ticket / Leave: ").lower()
            if choice == "park":
                park.take_ticket()
            elif choice == "pay ticket":
                park.pay_ticket()
            elif choice == "leave":
                park.leave_garage()
                break


park = Parking_garage()
park.run()
