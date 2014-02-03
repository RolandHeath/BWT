# This suffix array construction method is an early attempt at reconstructing the SA-IS method 
# described by Nong, Zhang and Chan (2009)
# It is not tested on any large datasets, but *should* behave similarly

#Input string S is an input string terminated by a $ character. This can be generated with readText.py
def suffixArray(S):                         #Where n is the length of the input, a is the size of its alphabet
    from bisect import insort
    from copy import copy
    t = [True]*len(S)                       #Type array, True is S-type, false is L-type: O(1) time, O(n) space eventually
    LMS = []                                #Keeps track of LMS suffix positions O(1) time, O(n) space eventually
    SA = [-1]*len(S)                        #The list which will become the suffix array, O(n) time and space at most.
    buckets = [('$',0)]                     #An array to keep track of the bucket keys, heads, and tails. O(1) time, O(a) space eventually
    for i in reversed(xrange(len(S)-1)):    #Traverse right-to-left, skips the sentinel: O(n) time, O(1) space
        flag = True                         #Keeps track of when to add a new item, instead of incrementing the current one, O(1) time and space
        for item in xrange(len(buckets)):   #Find the bucket of this item, O(a) time, O(1) space
            if buckets[item][0]==S[i]:      #If there is a bucket for the current character, increment its count O(1) time and space
                buckets[item] = (buckets[item][0],buckets[item][1]+1)
                flag=False                  #Don't add a new bucket
        if flag:                            #If adding a new bucket
            insort(buckets,(S[i],0))        #Add it in sorted order, O(log(a)) time, O(1) space
        if S[i] < S[i+1]:                   #If S-type
            t[i] = True                     #Mark as S-type O(1) time and space
        else:
            if S[i] > S[i+1]:               #If L-type
                t[i] = False                #Mark as L-type O(1) time and space
                if t[i+1] is True:          #If the last index is S-type
                    LMS.append(i+1)         #Then mark it as LMS O(1) time and space
            else:                           #If same as last
                t[i] = t[i+1]               #Take the last type O(1) time and space
                
    for i in xrange(len(buckets)-1):        #Organize and reformat the bucket array, O(a) time, O(1) space, two passes
         buckets[i+1] = (buckets[i+1][0],buckets[i][1]+buckets[i+1][1]+1)
    for i in reversed(xrange(len(buckets)-1)):
         buckets[i+1] = (buckets[i+1][0],buckets[i][1]+1,buckets[i+1][1])
    buckets[0] = (buckets[0][0],0,0)        #Reformat the sentinel bucket to match the others
    b=copy(buckets)                         #Copy the bucket array so that we don't lose information in the next loop O(a) time and space *Adjust code to remove this, inefficient*
    for i in reversed(LMS):                 #Traverse the LMS string right-to-left O(n) time worst case (but in that case, we're done), O(1) space
        for item in xrange(len(b)):         #Find the bucket for the current LMS character O(a) time, O(1) space
            if b[item][0]==S[i]:            #If we're in the right bucket
                SA[b[item][2]]=i            #Set SA at the head of the right bucket to the index of the LMS character, then move the head left.
                b[item] = (b[item][0],b[item][1],max(b[item][2]-1,b[item][1]))
    del b                                   #Delete the wasteful copy of the bucket array. *Remember this when you remove the bucket copying*
    for i in xrange(len(SA)):               #Iterate left-to-right through suffix array, uses the start of bucket as the intial head, O(n) time, O(1) space
        if SA[i] > 0:                       #If the current point is initialized and non-zero (i.e. not going to write a -1 somewhere)
            char=S[SA[i]-1]                 #Get the character to the left of this suffix (The next character in the LMS substring) O(1) time and space
            for b in range(len(buckets)):   #Find the bucket it belongs to, O(a) time, O(1) space
                 if buckets[b][0]==char:    #If we're at the right bucket
                    if t[SA[i]-1]==False:   #And at an L-type character (Not at the end of the LMS substring), add the suffix and move the head right by 1
                        SA[buckets[b][1]]=SA[i]-1
                    buckets[b]=(buckets[b][0],buckets[b][1]+1,buckets[b][2])
    for i in reversed(xrange(len(SA))):     #Iterate right-to-left through suffix array, uses the end of bucket as the intial head, O(n) time, O(1) space
        if SA[i] > 0:                       #If the current point is initialized and non-zero (i.e. not going to write a -1 somewhere)
            char=S[SA[i]-1]                 #Get the character to the left of this suffix O(1) time and space
            for b in range(len(buckets)):   #Find the bucket it belongs to, O(a) time, O(1) space
                 if buckets[b][0]==char:    #If we're at the right bucket
                    if t[SA[i]-1]==True:    #And at an S-type character (An end of the LMS substring), add the suffix and move the head left by 1
                        SA[buckets[b][2]]=SA[i]-1
                        buckets[b]=(buckets[b][0],buckets[b][1],buckets[b][2]-1)
    print S
    print SA
    return SA
