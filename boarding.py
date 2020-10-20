# boarding.py
# Simulerar ombordsstigningen av ett flypglan
# baserat på olika sätt att ordna passagerarna.

import methods

passengers = []

class Passenger:
    def __init__(self, type, row, seat):
        self.t = type
        self.gr = row # Goal Row (Assigned Row)
        self.gs = seat # Goal Seat (Assigned Seat)
        self.r = 0 # Current Row
        self.s = 0 # Current Seat
        self.state = 'none'

    def move(self):
        if self.state == 'bag':
            self.state = 'none'

        # Passenger is going forward
        elif self.r < self.gr: # Forward
            if not checkState(self.r + 1, 0):
                self.r += 1
                if self.r == self.gr:
                    self.state = 'bag'

        # Passenger is going left
        elif self.gs < self.s:
            self.s -= 1

        # Passenger is going right
        else:
            self.s += 1


def checkState(row, seat):
    for passenger in passengers: # Want 2nd to be active list
        if passenger.r == row and passenger.s == seat:
            return passenger.state
    return

rows = 30
seats = [-3, 3, -2, 2, -1, 1] # from -3 to 3 bar 0

# Populating list
for row in range(1, rows+1):
    for seat in seats:
        passengers.insert(0, Passenger('default', row, seat))

seats = [-3, 3, -2, 2, -1, 1, 0]

# One move cycle
def moveTick():

    # List "active". Starts out identical to passengers.
    # When an action is taken on a passenger, they are removed from the active list.
    # They do not need to be checked again that tick.

    boardingComplete = True

    for row in reversed(range(1, loops+2)): # Changing rows to loops, hm
        # For each row in reverse order, 30 -> 29 -> 28 etc.
        for seat in seats:
            #print("Row: " + str(row) + " Seat: " + str(seat))
            # For each seat in that row, check if there is a passenger there.
            for passenger in passengers:
                #print("Found a passenger")
                #print("Checking passenger, row " + str(passenger.r) + " seat " + str(passenger.s) + "... goal row " + str(passenger.gr) + " goal seat " + str(passenger.gs))
                if (passenger.r == row) and (passenger.s == seat):
                    #print("Matched.")
                    if not (passenger.r == passenger.gr and passenger.s == passenger.gs):
                        boardingComplete = False # This cycle, a passenger has moved. Boarding is not complete.
                        passenger.move()
                        #active.remove(passenger)
                        #print("Moved. New position, row " + str(passenger.r) + " seat " + str(passenger.s))
                    else:
                        passenger.state = 'seated'
                        #active.remove(passenger)
                #else:
                #    print("Did not match.")
    return boardingComplete # Returns the state of the boarding process.

#methods = ["backToFront", "frontToBack"]

passengers = methods.frontToBack(passengers)
passengers[0].move()
# First in sorted manifest moves

loops = 0

while not moveTick():
    print("Loop " + str(loops))
    if loops < 180:
        passengers[loops].r = 1
    loops += 1

print("FINISHED! Loops: " + str(loops))
