from whoosh.fields import Schema,TEXT
from whoosh.analysis import StemmingAnalyzer
from whoosh import index

schema=Schema(title=fields.TEXT(store=True),content=fields.TEXT)

def create_index(indexdir,schema):
	ix=index.create_index(indexdir,schema)
	return ix

def addDoc(ix,tit,cont):
	writer=ix.writer()
	writer.add_document(title=tit,content=cont)
	writer.commit()

reading module
	