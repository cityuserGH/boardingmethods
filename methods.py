# methods.py
# Contains the sorting functions for the various boarding methods

def random(manifest):
    return manifest

def BTF(manifest):
    return sorted(manifest, key = lambda p: -p.gr)

def FTB(manifest):
    return sorted(manifest, key = lambda p: p.gr)

def WMA(manifest):
    return sorted(manifest, key = lambda p: -abs(p.gs))

def WMA_BTF(manifest): # Window Middle Aisle, Back To Front (3 or -3, 2 or -2, 1 or -1)
    return sorted(manifest, key = lambda p: (-abs(p.gs), -p.gr))

def WMA_BTF_ALT(manifest): # Window Middle Aisle, Back To Front, Alternating sides. (3, -3, 2, -2, 1, -1)
    return sorted(manifest, key = lambda p: (-abs(p.gs + 0.25) + 0.25, -p.gr))
    # -abs(x + 0.25) + 0.25 gives
        #-abs(x) behaviour for x > -0.25
        #-abs(x + 0.5) behaviour for x < -0.25

def perfectSteffen():
    return
