# methods.py
# Contains the sorting functions for the various boarding methods

def backToFront(manifest, rows):
    sorted = []
    for row in range(1, rows+1):
        for passenger in manifest:
            if passenger.gr == row:
                sorted.insert(0, passenger)
    return sorted

def frontToBack(manifest, rows):
    sorted = backToFront(manifest, rows)
    sorted.reverse()
    return sorted

def perfectSteffen():
    return
