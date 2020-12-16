

OptimizerValues = {}

def isPerfectNum(num, OptimizerPD = False):
    listDiv = [1]
    div = 2
    opNum = num
    while (opNum != 1):
        if OptimizerPD and opNum in OptimizerValues:
          
            listDiv = listDiv +  [x*y for x in OptimizerValues[opNum] for y in listDiv ]
          
            # listDiv.append(num)
            break
        if opNum%div == 0:
            listDiv =  listDiv + [div*x for x in listDiv]
            opNum = opNum / div
        else:
            div+=1
    # print(listDiv)
    
    if OptimizerPD:
        OptimizerValues[num] = listDiv.copy()
    if num != 1:
        listDiv.remove(num)
    listDiv = set(listDiv)
    return listDiv, (sum(listDiv) == num)


#The optimizer, uses PD to calculate faster, in the end of the output files pfnumberoutputNormal.txt and 
#pfnumberoutputOptimizer.txt has a time comparison
def __main__():
    print("perfect numbers 1-10000")
    for x in range(1,10001):
        # print(x)
        r1, r2 = isPerfectNum(x, OptimizerPD=True)
        # print(r1,r2)
        if r2:
            print(x)

__main__()