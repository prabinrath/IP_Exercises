import numpy
#a,b,c only
inputString = raw_input("Enter data: ")
charDict = {"a":1,"b":2,"c":3}

count = 4
check = False
i=0
while i <len(inputString):
    for j in range(i+1,len(inputString)+1):
        check = False
        if inputString[i:j] not in charDict:
            charDict[inputString[i:j]] = count
            count = count +1 
            #print(inputString[i:j-1],charDict[inputString[i:j-1]])
            check = True
            i = j-1
            break
    if check == False:
        #print(inputString[i:len(inputString)],charDict[inputString[i:len(inputString)]])
        break

print('Result Dict: ',charDict)