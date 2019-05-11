import os
import sys

print("enter the root file address")
address=sys.argv[0]
files=os.listdir(address)

dict={}
for file in files:
	if(os.path.splitext(file)[1] == '.txt'):
		file_address=os.path.join(address,file)
		with open(file_address) as f
		line = f.readline()
		while line:
			info=line.split(" ")
			key=info[0]+info[1]
			dict[key]=file
