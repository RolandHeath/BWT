def transform(inString, suffixes):
    outString=[0]*len(inString)
    for i in xrange(len(inString)):
        outString[i]=inString[suffixes[i]-1]
    return outString
