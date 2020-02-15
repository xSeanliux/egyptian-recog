import glob
import random 

def get():
	allpics = glob.glob("./data/images/*")
	sz = len(allpics) * 9 // 10
	i = 0
	random.shuffle(allpics)
	print(allpics)
	for d in allpics:
		i = i + 1
		if(i == sz):
			print("--------------------") #dividing line
		print(d)

get()