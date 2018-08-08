#!/usr/bin/python3
#configure algorithm
def algorithm(n):
	count=0;
	while n!=1:
		if n%2!=0: #n is odd
			n=3*n+1
			count+=1
		else: #n is even
			n=n/2
			count+=1
	else:
		count+=1
		return count

def cycle_length(i,j):
	count=0
	maxNum=0
	if i>j: #if i is larger than j then swap them
		#print(i,j)
		i,j=j,i
	for num in range(i,j+1):
		#print(num)
		count=algorithm(num) #get count for every num
		if count > maxNum:
			maxNum=count
	return maxNum
	#print(i,j,maxNum)

#cycle_length(900,1000)
def main():
	while True:
		try:
			num=input()
			num_i,num_j=map(int,num.split())
			print(num_i,num_j,cycle_length(num_i,num_j),end="\n")
		except:
			break

if __name__ == '__main__':
	main()
