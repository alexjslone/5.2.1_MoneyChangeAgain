moneyList = []
coins = [1, 3, 4]
def change(money):
    for i in range(0,money+1): 
        moneyList.append(float('inf'))
    for m in range(0,money+1):
        #moneyList[m]=float('inf')
        for c in coins: 
            #moneyList[m]=float('inf')
            #I'm not sure if I need to move this up?
            if m == 0: 
                moneyList[m]=0
            elif m >= c and moneyList[m-c]+1 <= moneyList[m]:
                moneyList[m]= 1 + moneyList[m-c]
                #print(moneyList[m])
                #this should give you the min value for each
    return moneyList[money]



    
#money = 34
#print(change(money))


if __name__ == '__main__':
    m = int(input())
    print(change(m))
