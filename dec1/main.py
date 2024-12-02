import math
fh = open('input.txt')
left = list()
right = list()
for line in fh:
    numbers = line.split()
    left.append(int(numbers[0]))
    ##print('Left number is ', left)
    right.append(int(numbers[1]))
    ##print('Right number is ', right)
    ##input("Press Enter to continue")
left.sort()
right.sort()
totaldiff = 0
count = 0
for line in left:
    #print(count)
    diff = math.dist([left[count]], [right[count]])
    #print(diff)
    count=count+1
    totaldiff = totaldiff+diff
print("The total difference is: ", totaldiff)
## the above code is for Day 1 Part 1 and works





## This part is not working yet
match = 0
leftsimscore = 0
for lline in left:
    match = 0
    print("LEFT LOOP START - pre-nested line from left is: ", lline, ". Press enter to continue:")
    #input()
    for rline in right:
        #print("The current rline is: ", rline, "and left line is: ", line, ". Press enter to continue: ")
        #input()
        if rline != lline: continue
        leftsimscore = leftsimscore + lline
        match = match + 1
        print("MATCH - Line: ", lline, "Count: ", match, "rline: ", rline, "Left sim score: ", leftsimscore)
        #input()
    print("LEFT LOOP END - Left sim score is now ", leftsimscore)
    #input()
print("Final left sim score is: ", leftsimscore, ". Press enter to continue:")
input()


match = 0
rightsimscore = 0
for rline in right:
    match = 0
    print("RIGHT LOOP START - pre-nested line from right is: ", rline, ". Press enter to continue:")
    #input()
    for lline in left:
        #print("The current rline is: ", rline, "and left line is: ", line, ". Press enter to continue: ")
        #input()
        if lline != rline: continue
        rightsimscore = rightsimscore + rline
        match = match + 1
        print("MATCH - Line: ", rline, "Count: ", match, "lline: ", lline, "Right sim score: ", rightsimscore)
        #input()
    print("RIGHT LOOP END - Right sim score is now ", rightsimscore)
    #input()
print("Final right sim score is: ", rightsimscore, ". Total sim score is ", (rightsimscore + leftsimscore))
input()




'''
leftsimscore = 0
for line in left:
    sim = 0
    print("LEFT LOOP START - the current sim number is: ", sim, "pre-nested line from left is: ", line, "press enter to continue")
    #input()
    for rline in right:
        #print("the current rline is: ", rline, "and left line is: ", line, "press enter to continue, ")
        #input()
        if rline != line: continue
        sim = sim + 1
        #print("sim number is now: ", sim)
        #input()
    leftsimscore = leftsimscore + (line * sim)
    print("LEFT LOOP END - total sim for this loop was, ", sim, "and line was, ", line, "and left sim score is now ", leftsimscore)
    #input()
print("Left sim score is: ", leftsimscore, "press enter to continue")
input()
'''
'''
rightsimscore = 0
for rline in right:
    sim = 0
    print("RIGHT LOOP START - the current sim number is: ", sim, "pre-nested line from right is: ", line, "press enter to continue")
    #input()
    for lline in left:
        #print("the current rline is: ", rline, "and left line is: ", line, "press enter to continue, ")
        #input()
        if lline != rline: continue
        sim = sim + 1
        print("sim number is now: ", sim, "and left line is: ", lline, "press enter to continue:")
        input()
    rightsimscore = rightsimscore + (rline * sim)
    print("RIGHT LOOP END - total sim for this loop was, ", sim, "and right line was, ", rline, "and right sim score is now ", rightsimscore)
    #input()
print("Left sim score is: ", leftsimscore, "right sim score is: ", rightsimscore, "total is: ", leftsimscore+rightsimscore)
'''