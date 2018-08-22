#!/usr/bin/python3

import sys

cache={1:1}

def get_cycle_length(num):
	cycle_length=cache.get(num)
	if cycle_length is None:
		cycle_length=get_cycle_length(num=num/2 if num%2==0 else 3*num+1)+1
		cache[num]=cycle_length

	return cycle_length

def main():
	for num in sys.stdin:
		if not num:
			break
		else:
			num_i,num_j=list(map(int,num.split()))
			tmp_i,tmp_j=num_i,num_j
			if num_i > num_j: #swap
				tmp_i,tmp_j=num_j,num_i

			max_cycle_length=max(list(map(get_cycle_length,range(tmp_i,tmp_j+1))))
			print(num_i,num_j,max_cycle_length,end="\n")

if __name__ == '__main__':
	main()
