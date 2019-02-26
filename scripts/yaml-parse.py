#!/usr/bin/env python

import yaml

def filterOut(element):
    # Commuter Rail
    if "Commuter" not in element['lines']:
        notCommuter = True
    else:
        notCommuter = False

    # AND together all the fields.
    return notCommuter

def parse():
    with open("mbta.yaml", 'r') as stream:
        try:
            y = yaml.load(stream)
        except yaml.YAMLError as exc:
            print("no")
            print(exc)

    output = []

    for idx in range(0, len(y)):
        for item in y[idx]['stations']:
            try:
                element = {
                "title": item['title'],
                "lines": item['lines'],
                "latitude": item['latitude'],
                "longitude": item['longitude']
                }
                if (filterOut(element)):
                    output.append(element)
            except:
                pass

    return output

def cleanLines(output):
    cleanedOutput = []
    lineCodes = ["Green Line (all), (B"]

    for item in output:
        for code in lineCodes:
            if code in item["lines"]:
                if (uniqueName(cleanedOutput, item["title"])):
                    cleanedOutput.append(item)


    return cleanedOutput

###
def uniqueName(arr, name):
    for ele in arr:
        if ele["title"] == name:
            return False
    return True
###

def main():
    output = parse()
    output = cleanLines(output)

    for ele in output:
        print(ele,",")

# Run
main()
