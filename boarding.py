# boarding.py
# Simulerar ombordsstigningen av ett flypglan
# baserat på olika sätt att ordna passagerarna.

import methods, random, time, copy, math

# Settings
animationEnabled = True
animationSpeed = 0.6 # 0 to 1, 0 is inf time, 1 is 0 time

rows = 10
loopsPerMethod = 1

methodList = [
              #"random",
              #"BTF",
              #"FTB",
              #"WMA",
              "WMA_BTF",
              "WMA_BTF_ALT",
              "perfectSteffen"
             ]



passengers = []
animationSpeed = -math.log(animationSpeed, 10)

print("-- Boarding Methods --")

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

# Populating list
print("Populating passenger list...")
unsortedPassengerList = []
for row in range(1, rows+1):
    seats = [-3, 3, -2, 2, -1, 1] # from -3 to 3 except for 0
    for seat in seats:
        unsortedPassengerList.insert(0, Passenger('default', row, seat))




for currentMethod in methodList:
    print("\nNow running method: " + currentMethod)

    totalLoops = 0

    for i in range(loopsPerMethod):
        passengers = copy.deepcopy(unsortedPassengerList)

        random.shuffle(passengers) # Randomly shuffles list before sorting via method
        passengers = getattr(methods, currentMethod)(passengers)

        passengers[0].r = 1
        passengers[0].state = 'bag'

        loops = 0
        enterIndex = 1

        boardingComplete = False
        while not boardingComplete: # Loops if boarding is not complete
            boardingComplete = True
            # ...great


            # Calculates appropriate move calls
            seats = [-3, 3, -2, 2, -1, 1, 0]
            for row in reversed(range(1, rows+1)):
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
            ###

            # Lets a new passenger enter
            if enterIndex < (rows * 6):
                boardingComplete = False
                if not checkState(1, 0):
                    passengers[enterIndex].r = 1
                    if passengers[enterIndex].gr == 1:
                        passengers[enterIndex].state = 'bag'
                    enterIndex += 1
            ###

            if boardingComplete:
                break

            loops += 1

            # Renders animation
            if animationEnabled:
                for row in range(1, rows+1):
                    seatString = ""

                    seats = [-3, -2, -1, 0, 1, 2 , 3]
                    for seat in seats:
                        seatState = checkState(row, seat)

                        if seatState == 'bag':
                            seatString += "B"
                        elif seatState:
                            seatString += "x"
                        else:
                            seatString += "_"

                    print(seatString)
                print("#######")
                time.sleep(animationSpeed)
            ###
        print(str(i+1) + " - Loops: " + str(loops))
        totalLoops += loops
    ###

    average = totalLoops / loopsPerMethod
    print(currentMethod + " average: " + str(average))
