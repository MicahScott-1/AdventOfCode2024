#! /usr/bin/env python

# Define the lists and var
list1 = []
list2 = []
listOfDistances = []

# Function Definitions
def populateLists(inputFileName):
    with open(inputFileName, "r") as file:
        for line in file:
            list1.append(line[0:5])
            list2.append(line[8:13])

def orderList(list):
    list.sort()

def findDifference(item1, item2):
    if item1 > item2:
        return item1 - item2
    if item2 > item1:
        return item2 - item1
    else: #they must be equal
        return 0

def displayTotalDistance(list):
    totalDistance = 0
    for item in list:
        totalDistance += item
    print("The total distance is: " + str(totalDistance))

# Populate lists
populateLists("inputFile.txt")

# Doing the calculations 
orderList(list1)
orderList(list2)
print("Ordered lists:")
print(str(list1) + "\n" + str(list2))

if len(list1) == len(list2):
    for x in range(0,len(list1)):
        listOfDistances.append(findDifference(list1[x],list2[x]))
    displayTotalDistance(listOfDistances)
else:
    print("There is an error related to the lengths of\nthe lists that I do not know how to handle.")
    input("ENTER to quit...")
    quit()
