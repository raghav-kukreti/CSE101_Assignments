from main import selection
import random
rand_arr=[]
# rand_arr = [5,42,311,2,1,1]
for _ in range(10):
	rand_arr.append(random.uniform(0.0,1.0))
	
for _ in range(100):
	selection(rand_arr)
	print(sel_swap, sel_comp)

print(rand_arr)