#!/usr/bin/env python3

import sys
import os
import select

def runCCWC():
    inputArray = sys.argv
    lengthArray = len(inputArray)
    if(lengthArray > 3):
        print("Too Many Arguments")
    elif(lengthArray == 3):
        filename = str(inputArray[2])
        file = open(filename, 'r')
        fileData = file.read()
        case = inputArray[1]
        if(case =='-c'):
            print(str(countBytes(filename)) + " " + filename)
        if(case =='-l'):
            print(str(countLines(fileData)) + " " + filename)
        if(case =='-w'):
            print(str(countWords(fileData)) + " " + filename)
        if(case =='-m'):
            print(str(countCharacters(fileData)) + " " + filename)
    else:
        print(inputArray)
        filename = str(inputArray[1])
        file = open(filename, 'r')
        fileData = file.read()
        print(str(countLines(fileData)) + " " + str(countWords(fileData)) + " " + str(countBytes(filename)) + " " + filename)

def runCCWC2(data, arg):
    if not arg:
        print(str(countLines(data)) + " " + str(countWords(data)) + " " + str(countBytes2(data)))
    else:
        if(arg =='-c'):
            print(str(countBytes2(data)))
        if(arg =='-l'):
            print(str(countLines(data)))
        if(arg =='-w'):
            print(str(countWords(data)))
        if(arg =='-m'):
            print(str(countCharacters(data)))
    return

def countBytes(filename):
    return os.stat(filename).st_size

def countBytes2(string):
    return len(string.encode('utf-8'))

def countLines(fileData):
    count = 0
    for c in fileData:
        if c == '\n':
            count+=1
    return count

def countWords(fileData):
    return len(fileData.split())

def countCharacters(fileData):
    count = 0
    for c in fileData:
        count+=1
    return count

if __name__ == '__main__':
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        inputArray = sys.argv
        data = ''
        for l in sys.stdin:
            data += l
        if(len(inputArray) > 1):
            runCCWC2(data, inputArray[1])
        else:
            runCCWC2(data, '')
    else:
        runCCWC()