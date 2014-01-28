def readText():
    import sys, os
    dataFile = open(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'BWT_Input.txt'),'r')
    inString = list(dataFile.read())
    inString.append('$')
    dataFile.close()
    return inString
