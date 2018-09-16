#!/usr/bin/python3

"""
這題要把箱子盡可能的裝起來。
假設這排數字是箱子體積，如果要把小箱子們裝進大箱子，代表體積小的才能放進體積大的
4 1 2 9 16 25
箱子順序不能調換的情況下，最多可以塞5個箱子：1 2 9 16 25
這五個箱子的順序就像是所有箱子序列的子序列；最多可以塞的箱子數相當於最長的子序列
整體來說跟LIS一樣
但是題目給的輸入是邊長而且不一定是三維，所以不能以體積的概念做。
輸入可能是：
5 2 3
4 3 5
5 6 9
7 8 3
9 1 1
箱子大小和方向不一致，所以可以先把箱子轉成同方向，如果A箱三邊都小於B箱三邊，代表A可以塞到B裡

步驟：
1.箱子的邊排序
因為題目是要盡可能的塞箱子，所以可以把箱子按大小排序，達到最大塞箱數!
2.箱子大小排序
3.套用LIS解法
"""

import sys

#存箱子用的list(暫時用不到)
#_boxList=[]

#存箱子cahce的list
_boxCache=[]

#暫存箱子的list，為了排序
_tmpList=[] 

#這個dictionary是用來存一開始輸入時箱子的位置，因為排序過後位置會不一樣，但是輸出是要原本位置
cache={}

#createCache這個function是要把每個箱子的初始位置記錄下來，以空間爭取時間
#傳進function的有_box和他的index
def createCache(box,index):
    if cache.get(box) is None:
        cache[box]=index

#執行LIS
def lis(boxList):
    #lengthList是要用來儲存所有箱子的LIS長度
    lengthList=[]

    #測試lengthList是否建立成功
    #print("測試lengthList是否建立成功",lengthList)

    #得到傳進來的箱子序列長度，就是看有幾個箱子拉
    length=len(boxList)

    #根據LIS演算法，每個箱子預設的LIS長度都是1
    for i in range(length):
        lengthList.append(1)

    #測試lengthList是否全部初始化成1
    #print("測試lengthList是否全部初始化成1",lengthList)

    #計算每個箱子的LIS長度
    for i in range(length):
        j=i+1

        for j in range(length):
            #比較boxList[i][k]是否小於boxList[j][k]，如果小於則設成1，否則0
            cmp=0
                
            #因為傳進來的箱子資料全都是維度邊長，所以比較的時候要所有邊長都比較，所以需要多一個迴圈
            for k in range(len(boxList[i])):
                if boxList[i][k]<boxList[j][k]:
                    cmp=1
                elif boxList[i][k]==boxList[j][k]:
                    continue
                else:
                    cmp=0
                    break
                
            #如果boxList[i]的每個index都小於boxList[j]
            if cmp==1:
                if lengthList[j]<lengthList[i]+1:
                    lengthList[j]=lengthList[i]+1

    #找出LIS序列
    lisList=[]  #用來儲存Lis序列
    lisLength=max(lengthList)   #lisLength是儲存最長LIS
    for i in range(len(lengthList)-1,-1,-1):    #這段FOR LOOP是用來找LIS序列，從整段lengthList反向搜尋 range(start/起點,stop/終點,[step/差距])
        if lengthList[i]==lisLength:
            lisList.append(i)
            lisLength=lisLength-1

    #因為當初是反過來找LIS，之後要根據lisList去找相對應的箱子，所以在這邊要再反轉一次，也就是說一開始得到的lisList是4321，為了之後方便搜尋箱子，要做成1234
    lisList.reverse()
    
    #測試lengthList是否執行成功
    print("測試lengthList是否執行成功",lengthList)

    #找最長LIS
    print("找最長LIS",max(lengthList))
    print(max(lengthList))

    #找最長LIS的序列
    print("找最長LIS的序列",lisList)

    #根據找到的最佳LIS找箱子位置
    for i in range(len(lisList)):
        loopLen=len(lisList)
        if i!=loopLen-1:
            print(_boxCache[lisList[i]],end=' ')
        else:
            print(_boxCache[lisList[i]])

    print()
for _input in sys.stdin:

    #第一行會輸入的是箱子數量和維度
    #[箱子數量，維度]
    _boxSequence_dimension=list(map(int,_input.split()))
    if len(_boxSequence_dimension)!=2:
        continue

    #根據箱子數量和維度限制接下來的輸入，順便做箱子的邊長排序，當輸入到了最大箱子數時，排序同一個維度的所有箱子
    for _num in sys.stdin:
        _box=list(map(int, _num.split()))

        #檢查機制，確定要符合維度
        if len(_box) != _boxSequence_dimension[1]:
            continue
        else:
            #箱子維度排序
            _box.sort()

            #排好維度的箱子裝進站存箱序列，之後要來個所有箱子的排序
            _tmpList.append(_box)

            #因為dictionary不能接受list當作key，所以這裡會把box從list轉成tuple再存進tmpList
            createCache(tuple(_box),_tmpList.index(_box))

            #檢查機制，怕超出箱子數量
            _boxSequence_dimension[0]=_boxSequence_dimension[0]-1
            if _boxSequence_dimension[0]==0:    #如果是最後一個箱子的話...

                #暫存箱序列大排序!!!!
                print("BEFORE : ",_tmpList)
                _tmpList.sort()
                print("AFTER : ",_tmpList)

                #為了根據LIS序列抓箱子位置的方便，建立好cache之後就建立一個cache list
                for i in range(len(tuple(_tmpList))):
                    tmp=cache.get(tuple(_tmpList[i]))+1
                    _boxCache.append(tmp)
                print("_boxCache",_boxCache)

                #事後覺得沒有把所有箱子序列裝進大箱子序列的必要，所以在這邊註解掉
                #_boxList.extend(_tmpList)
                

                #排好的暫存箱進行LIS作業
                lis(_tmpList)
                
                #清空暫存箱序列和cache，準備下一波箱子序列輸入
                del _tmpList[:]
                del _boxCache[:]
                cache.clear()
                break

#print(_boxList)

"""
for i in range(len(_boxList)):
    print(_boxList[i],cache[tuple(_boxList[i])]+1)
"""
