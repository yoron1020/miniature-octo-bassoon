#!/usr/bin/python3
"""
這題的目標是要把瓶子分類
輸入:123456789
123一組456一組789一組
數字順序分別是三個顏色G B C
要把同個顏色的瓶子放到同一組，要找最小步數
所以可能是147 258 369這樣的放置方式
但是要直接計算移動的瓶子數量太久了，所以直接用反過來的方式計算
"用總瓶數-不動的瓶子"
最後的顏色分類有可能是GBC GCB BGC BCG CGB CBG共六種組合

策略:
    把不動的瓶子設成1，要移動的瓶子設成0，那最終的六種組合轉換成1/0就會變成
        012345678
        BGCBGCBGC
    BGC:100010001->048
    BCG:100001010->057
    GBC:010100001->138
    GCB:010001100->156
    CBG:001100010->237
    CGB:001010100->246
    輸入123456789

    然後根據濃縮的index，全部減掉不動的，找最小值!
    ex:GBC那組，1+...+9 - 1+5+9

    萬一有不用移動的個數有多個一樣的話，GBC組合要經過排序輸出，避免多餘運算，在建colorBin時就先排好順序
"""

import sys

#numList:六組的不動瓶子座標
#staticBottleNumList:把numList計算結果append進numList
numList=[[0,5,7],[0,4,8],[2,3,7],[2,4,6],[1,3,8],[1,5,6]]
colorBin=['BCG','BGC','CBG','CGB','GBC','GCB']
staticBottleNumList=[]


#test numList
"""
for i in range(len(numList)):
    for j in range(len(numList[i])):
        print(numList[i][j],end=" ")
"""

def _count(bottle):
    for i in range(len(numList)):
        countAns=0
        for j in range(len(numList[i])):
            countAns+=bottle[numList[i][j]]
        staticBottleNumList.append(countAns)


#while True:
for num in sys.stdin:
    if not num:
        break
    else:
        #num=input() #num:1 2 3 4 5 6 7 8 9
        bottle=list(map(int,num.split()))   #bottle:[1,2,3,4,5,6,7,8,9]
        if len(bottle) != 0:
            _count(bottle)
            sumBottle=sum(bottle)   #計算總共幾個瓶子
            maxStaticBottleNumList=max(staticBottleNumList) #瓶子不移動的最大值
            #print("staticBottleNumList",staticBottleNumList)
            #print("colorBin",colorBin)
            #print("sumBottle",sumBottle)
            print(colorBin[staticBottleNumList.index(maxStaticBottleNumList)],sumBottle-maxStaticBottleNumList)
            del staticBottleNumList[:]
            del bottle[:]
