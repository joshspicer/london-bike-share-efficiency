#!/usr/bin/env python3

import requests
import pandas
import csv

dict = {}
error = 0
outOfBoundCount = 0
valueStored = 0
computedValue = 0
totalEntries = 0

def main():
    with open('../london/bikes/london-bikes-original.csv') as f:
        with open('output.csv', 'w+') as ff:
            reader = csv.reader(f, delimiter=',')
            # reader = pandas.read_csv(f)
            writer = csv.writer(ff)


            itercars = iter(reader)
            header = next(reader)
            header.append("EndLatitude")
            header.append("EndLongitude")
            header.append("StartLatitude")
            header.append("StartLongitude")
            writer.writerow(header)
            for ele in reader:
                global totalEntries
                totalEntries += 0
                endLat, endLong = computeCoords(ele[5])
                startLat, startLong = computeCoords(ele[8])

                startInBounds = withinBounds(startLat, startLong)
                endInBounds = withinBounds(endLat, endLong)

                if not startInBounds or not endInBounds:
                    global outOfBoundCount
                    outOfBoundCount += 1
                    print("Coordinates out of bounds")
                    continue

                if startLat == -1 or endLat == -1:
                    continue

                ele.append(endLat)
                ele.append(endLong)

                ele.append(startLat)
                ele.append(startLong)

                writer.writerow(ele)

    print("Completed with ", error, " errors (probably couldn't find location).")
    print("There were ", outOfBoundCount, " entries with at least one location out of bounds.")
    print("There were ", computedValue, " unique coordinates computed.")

def withinBounds(lat, long):
    latitudeLower = 49
    latitudeUpper = 53
    longitudeLower = -3
    longitudeUpper = 3

    if lat >= latitudeLower and lat <= latitudeUpper and long >= longitudeLower and long <= longitudeUpper:
        return True
    else:
        return False


def computeCoords(address):
    # First check if we've computed this location before
    if address in dict:
        print("Value stored!")
        global valueStored
        valueStored += 1
        return dict[address]
    else:
        print("Requesting Value!")
        global computedValue
        computedValue += 1
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+ address  + '&key=<YOUR-KEY>')
        try:
            result = r.json()['results'][0]['geometry']['location']
            dict[address] = (result['lat'],result['lng'])
            return dict[address]
        except:
            print("Error! (Probably no result found)")
            increaseError()
            return -1, -1  # Error

def increaseError():
    global error
    error = error + 1


# Completed with  2237  errors

# Third run STATS:
# Completed with  2205  errors (probably couldn't find location).
# There were  15413  entries with at least one location out of bounds.
# There were  2980  unique coordinates computed.




main()


# "https://maps.googleapis.com/maps/api/geocode/json?address="+ADDRESS+"&key=<YOUR-TOKEN>"
