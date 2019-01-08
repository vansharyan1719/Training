import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Zaroor hoga'
    elif answerNumber == 2:
        return 'aabhi tak to lagta hai'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply mat suno bhai'
    elif answerNumber == 5:
        return 'baad mein puchna bhai'
    elif answerNumber == 6:
        return 'Concentrate karo kaam par'
    elif answerNumber == 7:
        return 'nahi hoga, aur kuch sunaun'
    elif answerNumber == 8:
        return 'umeed mat karo'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
