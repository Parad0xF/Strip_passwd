def readTheFile(fileName):
    myLines = []
    with open(fileName) as file_in:
        while file_in:
            line = file_in.readline().replace("Collection", " ").lstrip()
            myLines.append(line)
            if line == "":
                break
    secList = []
    substr = ":"
    for line in myLines:
        index = 0
        index = line.find(substr, index)
        if index == -1:
            break
        secList.append(line[index + 1:].strip('\n'))
    myLines.clear()

    return secList


def writeListOnFile(theList):
    MyFile = open(input("Output file name: "), 'w')
    for data in theList:
        MyFile.write(data)
        MyFile.write('\n')
    MyFile.close()


if __name__ == "__main__":
    theList = readTheFile(input("Input file name: "))
    writeListOnFile(theList)
