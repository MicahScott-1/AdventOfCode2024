#!/usr/bin/env python3

# read file splitlines on whitespace
# check all inc or all dec
# check non inc or dec more than 3

# Define variables
totalSafe = 0
inputList = []

# Define functions

def populateLists(inputFileName):
    with open(inputFileName, "r") as file:
        for line in file:
            inputList.append(int(line.split()))

populateLists('inputFile.txt')
print()
# Do operations