import sys
import os

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
        filename = str(inputArray[1])
        file = open(filename, 'r')
        fileData = file.read()
        print(str(countLines(fileData)) + " " + str(countWords(fileData)) + " " + str(countBytes(filename)) + " " + filename)

def countBytes(filename):
    return os.stat(filename).st_size

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
    runCCWC()