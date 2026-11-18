def findCharacterMissed (sampleText, userText):
    mistakes = []
    i = 0
    j = 0
    while i< len(sampleText) and j < len(userText):
        #Correct text at the same place
        if sampleText[i] == userText[j]:
            i += 1 
            j += 1 
        #An extra character
        elif (j+1)<len(userText) and sampleText[i] == userText[j+1]:
            mistakes.append(userText[j])
            j+=1 
        #Missing character
        elif (i+1)< len(sampleText) and sampleText[i+1] == userText[j]:
            mistakes.append (sampleText[i])
            i+= 1 
        #Incorrect character at the same place:
        else: 
            mistakes.append(userText[j])
            i +=1 
            j +=1 
            
    #Missing character at the end
    while i <len(sampleText):
        mistakes.append(sampleText[i])
        i += 1 
    #Extra character at the end
    while j < len(userText):
        mistakes.append ( userText [j])
        j+=1 
        
    return mistakes


def calCharacterMissed(sampleText, userText):
    mistakes = findCharacterMissed(sampleText, userText)
    return len(mistakes)

def calcAccuracy (sampleText, userText):
    totalChars = len(sampleText)
    missedChars = calcCharsMissed(sampleText, userText)
    accuracy = (totalChars - missedChars)/totalChars
    return accuracy
