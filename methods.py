# methods.py
# Contains the sorting functions for the various boarding methods

def frontToBack(manifest):
    sorted = []
    for i in range(30):
        for passenger in manifest:
            if passenger.r == i:
                sorted.insert(0, passenger)
    return sorted

def backToFront(manifest):
    sorted = frontToBack(manifest)
    sorted.reverse()
    return sorted

def perfectSteffen(manifest):
    return
