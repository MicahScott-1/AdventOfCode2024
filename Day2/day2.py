#!/usr/bin/env python3

# read file splitlines on whitespace
# check all inc or all dec
# check non inc or dec more than 3

# Define variables
totalSafe = 0
inputString = ""
inputList = []

# Define functions
def readFile(inputFileName):
    with open(inputFileName, "r") as file:
        return file.read()

def createList(stringInput):
    global inputList
    for line in stringInput.splitlines():
        inputList.append(line.split())

def reportAscending(input):
    if sorted(input) == input:
        print("list asc")
        return True
    else:
        return False
    
def reportDescending(input):
    if sorted(input, reverse=True) == input:
        print("list desc")
        return True
    else:
        return False

def reportSafeLevels(input):
    asc = reportAscending(input)
    desc = reportDescending(input)
    #input=input.split(",")
    print(str(asc) + " "+str(desc))
    if asc:
        for i in range(0,len(input)-1):
            if i == 0:
                if int(input[i+1]) - int(input[i]) <= 3:
                    pass #is ok
                else:
                    print("asc list not safe")
                    break
            else:
                if int(input[i+1]) - int(input[i]) <=3:
                    return True
    if desc:
        for i in range(0, len(input)-1):
            if int(input[i]) - int(input[i+1]) <= 3:
                return True
            else:
                print("desc list not safe")
                break
                
                    
#probably not using?
def countSafe(input):
    global totalSafe
    for x in range(0,len(input)):
        print(input[x])
        if reportSafeLevels(input[x]) == True:
            totalSafe += 1

# Do operations
inputString = readFile("inputFile.txt")
createList(inputString) #creates inputList
countSafe(inputList)
print(totalSafe)

