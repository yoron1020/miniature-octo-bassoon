#!/usr/bin/python3

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


"""_makeList(10)
#print(_makeList(25))
_pileBlock(9,1)
print(blockList)
_pileBlock(4,1)
print(blockList)
_pileBlock(6,1)
print(blockList)

_initialBlock(1)
print(blockList)
"""

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






