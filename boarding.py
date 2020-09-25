# boarding.py
# Simulerar ombordsstigningen av ett flypglan
# baserat på olika sätt att ordna passagerarna.

passengers = []

# [ [ [],[] ], [ [],[] ], [ [],[] ] ]
# [ [goalRow, goalSeat], [posRow, posSeat] ]

class Passenger(type, row, seat):
    def __init__(self, row, seat):
        self.t = type
        self.r = row
        self.s = seat
        self.pr = 0
        self.ps = 0
        self.state = 'none'

    def move():
        if self.pr < self.r:
            if checkState(self.r + 1, 0):
                print()
        else:
            if self.s > self.ps:
                if not checkState(self.r, self.s - 1):
                    print()
                # left
            else:
                return 2
                # right


# populating list

def checkState(row, seat):
    for passenger in passengers:
        if passenger.r == row and passenger.s == seat:
            return passenger.state
    return

rows = 30
seats = [-3, -2, -1, 1, 2, 3] # from -3 to 3 bar 0

for row in range(1, rows+1):
    for seat in seats:
        # Setting goalRow to row
        passengers[i][0][0] = row

        # Setting goalSeat to a seat in seats
        passengers[i][0][1] = seat

        # Setting posRow to 0
        passengers[i][1][0] = 0

        # Setting posSeat to 0
        passengers[i][1][1] = 0

def moveTick():
    active = passengers
    # List "active". Starts out identical to passengers.
    # When an action is taken on a passenger, they are removed from the active list.
    # Thus, they do not need to be checked again that tick.

    for row in reversed(range(1, rows+1)):
        # For each row in reverse order, 30 -> 29 -> 28 etc.
        for seat in seats:
            # For each seat in that row, check if there is a passenger there.
            for passenger in active:
                if (passenger[1][0] == row) and (passenger[1][1] == seat):
                    active.remove(passenger)
                    # Update position values in passengers
                    # I.e. move logic
                    if passengers[1][0] == passengers[0][0]:
                        # If in aisle, bag.
                        print()
                    elif passengers[1][0] < passengers[0][0]:
                        # Move forward 1 step if next is clear
                        occupied = False
                        for other in passengers:
                            if (other[1][0] == (passenger[1][0] + 1)) and (other[1][1] == 0):
                                occupied = True
                        if occupied == False:
                            passengers[1][0] += 1
