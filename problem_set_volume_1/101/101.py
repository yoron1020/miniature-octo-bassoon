#!/usr/bin/python3

"""
move a onto b:歸位a上block 歸位b上block 把a放到b上
move a over b:歸位a上block 把a放到b上
pile a onto b:歸位b上block 把a和a上面的所有block放到b上
pile a over b:把a和a上面的所有block放到b上

總共2個動作:歸位x上block 把x和x上所有block放到x'上(如果x上面沒有別的block就會做出"把a放到b上")
"""

#宣告一個空的一維陣列
blockList=[]


#在一維陣列的索引裡面再加上一個一維陣列就可以製作出一個二維陣列
def _makeList(blockNum):
	for i in range(blockNum):	#假設blockNum是10，就要做出最大10x10的陣列，因為還加上值擴充，所以目前是10x1的二維陣列
		blockList.append([])	#在每個一維陣列的索引再加上一格一維陣列
		blockList[i].append(i)	#[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]

#在blockList裡尋找blockNum的位置
def _findPosition(blockNum):
	for i in range(len(blockList)):
		for j in range(len(blockList[i])):
			if blockNum==blockList[i][j]:
				return i,j	

#歸位
#要先找到blokNum1和blockNum2在二維陣列的位置
def _initialBlock(blockNum): 
	i=_findPosition(blockNum)[0]
	j=_findPosition(blockNum)[i]
	if len(blockList[i])!=j+1:					#如果blockNum是最後一個就不要做，因為沒得刪
	for in range(len(blockList[i])-j-1):		#假設blockNum=7，[[0],[1],[2],[3],[4],[5,6,7,8,9]]，位置在(i=5,j=2)，要把7之後(8和9)放回去，for執行次數(len=5)-(j=2)-1=2步
		#putBackNum=blockList[blockNum][-1]		#第5個一維陣列的最後一個
		blockList[blockList[blockNum][-1]].append(blockList[blockNum][-1])	#把第5個一維陣列的最後一個值加到該值代表的一維陣列的最後面
		del blockList[blockNum][-1]	#因為已經把值加到該去的地方了，所以把第5個索引的值移除

#有錯的function XDDDD
"""
def _pileBlock(blockNum1, blockNum2):
		blockList[blockNum2].extend(blockList[blockNum1])
	del blockList[blockNum1][-1] ]#delete last element in two dimension list

def _moveBlock(blockNum1, blockNum2):
	blockList[blockNum2].extend(blockList[blockNum1])
"""

#移動block
#要先找到blockNum1和blockNum2在二維陣列的位置，
#def moveBlock(blockNum1, blockNum2):
		

#輸入block數量，然後產生一個二維陣列
num=int(input())
_makeList(num)


#test new function
"""
i=_findPosition(2)[0]
j=_findPosition(2)[1]
print(i)
print(j)
"""
"""
for i in range(len(blockList)):
	for j in range(len(blockList[i])):
		print(blockList[i][j].index(blockList[i][j]))
"""

while True:
	command=input()
	if command=="quit":
		print(blockList)
		break
	else:
		move_pile,a,onto_over,b=map(str,command.split())
		#print(move_pile,a,onto_over,b)
		if move_pile=="move":
			if onto_over=="onto":
				_initialBlock(int(a))
				_initialBlock(int(b))
				_moveBlock(int(a), int(b))
				print(blockList)
			if onto_over=="over":
				_initialBlock(int(a))
				_moveBlock(int(a), int(b))
				print(blockList)
		
		if move_pile=="pile":
			if onto_over=="onto":
				_initialBlock(int(b))
				_pileBlock(int(a), int(b))
				print(blockList)
			if onto_over=="over":
				_pileBlock(int(a), int(b))
				print(blockList)






