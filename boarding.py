# boarding.py
# Simulerar ombordsstigningen av ett flypglan
# baserat på olika sätt att ordna passagerarna.

import methods

passengers = []

class Passenger(type, row, seat):
    def __init__(self):
        self.t = type
        self.gr = row # Goal Row
        self.gs = seat # Goal Seat
        self.r = 0 # Current Row
        self.s = 0 # Current Seat
        self.state = 'none'

    def move(self):
        if self.state == 'bag':
            self.state = 'none'

        # Passenger is going forward
        elif self.r < self.gr: # Forward
            if not checkState(self.r + 1, 0):
                if (self.r := self.r + 1) == self.gr:
                    self.state = 'bag'

        # Passenger is going left
        elif self.gs > self.s:
            self.s -= 1

        # Passenger is going right
        else:
            self.s += 1


def checkState(row, seat):
    for passenger in active:
        if passenger.r == row and passenger.s == seat:
            return passenger.state
    return

rows = 30
seats = [-3, 3, -2, 2, -1, 1] # from -3 to 3 bar 0

# Populating list
for row in range(1, rows+1):
    for seat in seats:
        passengers.insert(Passenger('default', row, seat))

# One move cycle
def moveTick():
    active = passengers
    # List "active". Starts out identical to passengers.
    # When an action is taken on a passenger, they are removed from the active list.
    # They do not need to be checked again that tick.

    boardingComplete = True

    for row in reversed(range(1, rows+1)):
        # For each row in reverse order, 30 -> 29 -> 28 etc.
        for seat in seats:
            # For each seat in that row, check if there is a passenger there.
            for passenger in active:
                if (passenger.r == row) and (passenger.s == seat):
                    active.remove(passenger)
                    if not (passenger.r == passenger.gr and passenger.s == passenger.gs):
                        boardingComplete = False # This cycle, a passenger has moved. Boarding is not complete.
                        passenger.move()
                    else:
                        passenger.state = 'seated'
    return boardingComplete # Returns the state of the boarding process.

#methods = ["backToFront", "frontToBack"]

loops = 0
for method in methods: # Not correct
    while moveTick():
        loops += 1

        if checkState(0, 0):
            if method == "backToFront":
                for passenger in active:

            elif method == "frontToBack":
                print()

        continue

    print(method + " - " + loops)
