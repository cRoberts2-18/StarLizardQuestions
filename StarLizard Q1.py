def function(outfits,money):
    possibleCombinations=[]
    maxLen=0
    for i in range(0,len(outfits)):
        MoneySpent=0
        tempArray=[]
        for j in range(0,len(outfits)-i):
            MoneySpent+=outfits[i+j]
            if MoneySpent<=money:
                tempArray.append(outfits[i+j])
        possibleCombinations.append(tempArray)

    for i in range(0,len(possibleCombinations)):
        if maxLen<len(possibleCombinations[i]):
            maxLen=len(possibleCombinations[i])
    

    return(maxLen)

outfits=[2, 2, 1, 4, 1]
money=5

print(function(outfits,money))