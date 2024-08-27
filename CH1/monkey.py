#GOAL: measure match to “methinks it is like a weasel”

#generate string strlen param long
import random
def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz " #0 to 26 cuz of space
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res

#scoring function
def score(goal, teststr):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststr[i]:
            numSame = numSame+1
    return numSame/len(goal)

def main():
    goalstr = "methinks it is like a weasel"
    newstring = generateOne(28)
    best = 0 #track best score
    newscore = score(goalstr, newstring)

    while newscore < 1:
        if newscore > best:
            best = newscore
            print(newscore, newstring)
        newstring = generateOne(28)
        newscore = score(goalstr, newstring)



main()
