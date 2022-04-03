# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:39:57 2021

@author: souga
"""

# Python program for weighted job scheduling using Dynamic
# Programming and Binary Search

# Class to represent a job
class Job:
	def __init__(self, start, finish, profit):
		self.start = start
		self.finish = finish
		self.profit = profit


# A Binary Search based function to find the latest job
# (before current job) that doesn't conflict with current
# job. "index" is index of the current job. This function
# returns -1 if all jobs before index conflict with it.
# The array jobs[] is sorted in increasing order of finish
# time.
def binarySearch(job, start_index):

	# Initialize 'lo' and 'hi' for Binary Search
	lo = 0
	hi = start_index - 1

	# Perform binary Search iteratively
	while lo <= hi:
		mid = (lo + hi) // 2
		if job[mid].finish <= job[start_index].start:
			if job[mid + 1].finish <= job[start_index].start:
				lo = mid + 1
			else:
				return mid
		else:
			hi = mid - 1
	return -1

# The main function that returns the maximum possible
# profit from given array of jobs
def schedule(job,k):
    
	
	# Sort jobs according to finish time
    job = sorted(job, key = lambda j: j.finish)

	# Create an array to store solutions of subproblems. table[i]
	# stores the profit for jobs till arr[i] (including arr[i])
    n = len(job)
    table = [0 for _ in range(n)]
    count = [1 for i in range(n)]

    table[0] = job[0].profit
    
	# Fill entries in table[] using recursive property
    
    for i in range (1,n):
        currentprofit = job[i].profit
        tempcount = count[i]
        li = binarySearch(job, i)
        if (li != -1):
            currentprofit += table[li]
            tempcount += count[li]
            
        table[i] = currentprofit;
        count[i] = tempcount;
        
    temp = 0;
    for i in range (0,n):
        if k == count[i]:
            if temp == 0:
                temp = table[i]
            elif table[i] > temp:
                temp = table[i]
    
    #print(count)
    #print(table)
    return temp;
            
    #print(count)
    #return table

# Driver code to test above function
def main ():
    job = [Job(1, 3, 50), Job(3, 5, 20),
	Job(6, 19, 100), Job(2, 100, 200)]
    
    job2 = [Job(1, 3, 5), Job(2, 5, 6),Job(4, 6, 5), Job(6, 7, 4), Job(5, 8, 11), Job(7, 9, 2)]
    
    job3 = [Job(0, 2, 50), Job(0, 3, 90), Job(0, 4, 140), Job(1, 4, 120), Job(2, 5, 100), Job(3, 6, 60), Job(3, 8, 150), 
            Job(4, 9, 130), Job(5, 10, 160), Job(5, 11, 180), Job(6, 11, 100), Job(8, 11, 90), Job(9, 11, 40), Job(10, 11, 30)]
    k = 3
    print("Optimal profit is"),
    print(schedule(job3,k))
    
if __name__ == "__main__":
    main()
