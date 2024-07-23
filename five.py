# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
class Train:
    def __init__(self, status, fare) -> None:
        self.status = status
        self.fare = fare
    def bookTicket(self, num):
        if self.status >= num:
            self.status-=num
        else:
            print('Seats Full')
    def getStatus(self):
        return self.status
    def getFare(self):
        return self.fare
    
Rajdhani = Train(20, 1500)

Rajdhani.bookTicket(21)
print(Rajdhani.getStatus())