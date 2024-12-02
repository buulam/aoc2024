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
count = 0
leftsimscore = 0
for line in left:
    sim = 0
    for rline in right:
        if rline != left: continue
        sim = sim+1
        leftsimscore = leftsimscore + (left * sim)
print("Left sim score is: ", leftsimscore)
count = 0
rightsimscore = 0
for line in right:
    sim = 0
    count=count+1
    for lline in left:
        if lline != right[count-1]: continue
        sim = sim+1
        rightsimscore = rightsimscore + (right[count-1] * sim)
print("Right sim score is: ", rightsimscore)
print("Total sim score is: ", leftsimscore+rightsimscore)