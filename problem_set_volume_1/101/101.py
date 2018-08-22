#!/usr/bin/python3

"""
move a onto b:歸位a上block 歸位b上block 把a放到b上
move a over b:歸位a上block 把a放到b上
pile a onto b:歸位b上block 把a和a上面的所有block放到b上
pile a over b:把a和a上面的所有block放到b上

總共2個動作:歸位x上block 把x和x上所有block放到x'上(如果x上面沒有別的block就會做出"把a放到b上")
"""

blockList=[]

def _initialBlock(blockNum):
	for i in range(len(blockList[blockNum])):
		#putBackNum=blockList[blockNum][-1]
		blockList[blockList[blockNum][-1]].append(blockList[blockNum][-1])
		del blockList[blockNum][-1]


def _pileBlock(blockNum1, blockNum2):
	blockList[blockNum2].extend(blockList[blockNum1])
	del blockList[blockNum1][-1] #delete last element in two dimension list

def _moveBlock(blockNum1, blockNum2):
	blockList[blockNum2].extend(blockList[blockNum1])

def _makeList(blockNum):
	for i in range(blockNum):
		blockList.append([]) #making two dimension array by append [] to the list
		blockList[i].append(i)
	#return blockList

num=int(input())
_makeList(num)
#print(blockList)

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






