import random

def keygen(segments, seglength, dashenabled):
    keylist = []
    key = ""
    outloop = 0
    inloop = 0
    while outloop != segments:
        while inloop != seglength:
            valid = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            randomchar = random.choice(valid)
            keylist.append(randomchar)
            inloop += 1

        if outloop == segments - 1:
            outloop += 1
            inloop = 0
        else:
            if dashenabled:
                keylist.append("-")
                outloop += 1
                inloop = 0
            else:
                outloop += 1
                inloop = 0
    # convert list to var
    loops = 0
    while loops != len(keylist):
        key = key + keylist[loops]
        loops += 1
    return key