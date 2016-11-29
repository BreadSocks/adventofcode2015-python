import json

counter = 0

def findnumbersinjson(jsonlist):
    global counter
    for jsonelement in jsonlist:
        if isinstance(jsonelement, list):
            findnumbersinjson(jsonelement)
        elif isinstance(jsonelement, dict):
            findnumbersinjson(dict(jsonelement).values())
        elif isinstance(jsonelement, int):
            print "Found number"
            counter += int(jsonelement)

jsonstring = open("input.txt").read()
jsonarray = json.loads(jsonstring)
print jsonarray
findnumbersinjson(jsonarray)

print "Finished", counter
