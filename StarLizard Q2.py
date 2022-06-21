name = ['ball', 'bat', 'glove', 'glove', 'glove']
price = [2, 3, 1, 1, 1]
weight = [1, 1, 1, 1, 1]

def numDuplicates(name,price,weight):
    productArray=[]
    duplicates=0
    for i in range(0,len(name)):
        productArray.append([name[i],price[i],weight[i]])
    while len(productArray)>0:
        check=productArray[0]
        for i in range(1,len(productArray)):
            if productArray[i]==check:
                duplicates+=1
                productArray[i]=0
        print(productArray)
        try:
            productArray.remove(0)
        except:
            print("no Zero")
        if len(productArray)!=0:
            productArray.pop(0)


    return(duplicates)

print(numDuplicates(name,price,weight))