import os
import sys
from search import Search as sh
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema,TEXT

address=input("enter the root file address: ")
files=os.listdir(address)
dir_name=input("enter the index dir name: ")

schema=Schema(title=TEXT(stored=True),content=TEXT(analyzer=StemmingAnalyzer()))
index_addr=os.path.join(address,dir_name)
ix=sh.create_index(index_addr,schema)

for file in files:
	if(os.path.splitext(file)[1] == '.txt'):
		file_address=os.path.join(address,file)
		with open(file_address) as f:
			line = f.readline()
			while line:
				info=line.split(" ")
				key=info[0]+info[1]
				sh.addDoc(ix,key,info[2])
				line = f.readline()

			
			
			