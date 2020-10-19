def backToFront(manifest):
    sorted = []
    for i in range(30):
        for passenger in manifest:
            if passenger.r == i:
                sorted.insert(0, passenger)

    sorted.reverse()
    return sorted

def frontToBack(manifest):
    return

def perfectSteffen(manifest):

    return
