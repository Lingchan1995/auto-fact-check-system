import os
import search.Search as sh
from whoosh.analysis import StemmingAnalyzer

print("enter the root file address")
address=raw_input
files=os.listdir(address)
print("enter the index dir name")
dir_name=raw_input

schema=Schema(title=fields.TEXT(store=True),content=fields.TEXT(analyser=StemmingAnalyzer()))
index_addr=os.path.join(address,dir_name)
ix=sh.create_index(index_addr,schema)

for file in files:
	if(os.path.splitext(file)[1] == '.txt'):
		with open(file_address) as f
		line = f.readline()
		while line:
			info=line.split(" ")
			key=info[0]+info[1]
			sh.addDoc(ix,key,info[2])


			
			
			