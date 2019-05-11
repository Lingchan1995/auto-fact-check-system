import os
from whoosh.fields import Schema,TEXT
from whoosh import index 

class Search(object):

	@staticmethod
	def create_index(indexdir,schema):
		if not os.path.exists(indexdir):
			os.mkdir(indexdir) 
		ix=index.create_in(indexdir,schema)
		return ix

	@staticmethod
	def addDoc(ix,tit,cont):
		writer=ix.writer()
		writer.add_document(title=tit,content=cont)
		writer.commit()
