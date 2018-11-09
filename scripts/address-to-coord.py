#!/usr/bin/env python3

import requests
import pandas
import csv

dict = {}
error = 0

def main():
    with open('london-bikes.csv') as f:
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
                endLat, endLong = computeCoords(ele[5])
                startLat, startLong = computeCoords(ele[8])

                ele.append(endLat)
                ele.append(endLong)

                ele.append(startLat)
                ele.append(startLong)

                writer.writerow(ele)

    print("Completed with ", error, " errors")

def computeCoords(address):
    # First check if we've computed this location before
    if address in dict:
        print("Value stored!")
        return dict[address]
    else:
        print("Requesting Value!")
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+ address  + '&key=AIzaSyCswxrLBhiTq9PPW_8l6nMU2b0fwf9Z5oA')
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





main()


# "https://maps.googleapis.com/maps/api/geocode/json?address="+ADDRESS+"&key=AIzaSyCswxrLBhiTq9PPW_8l6nMU2b0fwf9Z5oA"
