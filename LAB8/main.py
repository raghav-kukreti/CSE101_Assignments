import random
import warnings
warnings.filterwarnings("ignore")

# rand_arr=[]
rand_arr = [5,4,3,2,1]
# for _ in range(100):
	# rand_arr.append(random.uniform(0.0,1.0))

ctr_swap=0
ctr_comp=0
def insertion(arr):
	for index in range(1,len(arr)):
		 currentvalue = arr[index]
		 position = index
		 while position>0 and arr[position-1]>currentvalue:
				 arr[position]=arr[position-1]
				 position = position-1
				 global ctr_comp
				 ctr_comp += 1
		 arr[position]=currentvalue
		 global ctr_swap
		 ctr_swap+=1

sel_swap=0
sel_comp=0
def selection(A):
	for i in range(len(A)):		 
		min_idx = i
		for j in range(i+1, len(A)):
				if A[min_idx] > A[j]:
						min_idx = j			
				global sel_comp
				sel_comp+=1									 
		A[i], A[min_idx] = A[min_idx], A[i]
		global sel_swap
		sel_swap+=1

merge_comp=0
merge_swap=0
def mergeSort(alist):
	if len(alist)>1:
			mid = len(alist)//2
			lefthalf = alist[:mid]
			righthalf = alist[mid:]
			mergeSort(lefthalf)
			mergeSort(righthalf)
			i=0
			j=0
			k=0
			while i < len(lefthalf) and j < len(righthalf):
					if lefthalf[i] < righthalf[j]:
							alist[k]=lefthalf[i]
							global merge_comp
							merge_comp =merge_comp+1
							i=i+1
					else:
							alist[k]=righthalf[j]
							j=j+1
					k=k+1
			while i < len(lefthalf):
					alist[k]=lefthalf[i]
					i=i+1
					k=k+1
			while j < len(righthalf):
					alist[k]=righthalf[j]
					j=j+1
					k=k+1

insertion(rand_arr)
selection(rand_arr)
mergeSort(rand_arr)
# print(rand_arr)
# comp=0
# comp_2=0
# comp_3=0
# for i in range(20):
# 	for _ in range(10):
# 		rand_arr.append(random.uniform(0.0,1.0))
# 	selection(rand_arr)
# 	insertion(rand_arr)
# 	mergeSort(rand_arr)
# 	global sel_comp
# 	global ctr_swap
# 	global merge_comp

# 	comp+=sel_comp
# 	comp_2+=ctr_swap
# 	comp_3+=merge_comp
# 	sel_comp=0
# 	ctr_comp=0
# 	merge_comp=0

# print(comp/10000)
# print(comp_2/100)
# print(comp_3/100)
print("Insertion Compare: " + str(ctr_comp))
print("Selection Swap = " + str(ctr_swap) + " Selection Compare: " + str(sel_comp))
print("Merge Compare: " + str(merge_comp))
# print(sel_swap, sel_comp)
# print(merge_comp, merge_swap)
