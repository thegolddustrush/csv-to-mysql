import sys

DELIM="\t"
TABLE="table_to_parse"
USE_AI=False #assume autoincrement is last
SKIP_FIRST_LINE=False
INTTYPE="int"
STRTYPE="str"
SKIP="skip"
mappings=[]

def ProcessMappingFile(mappingFile):
	global mappings
	try:
		f=open(mappingFile)
		for l in f.readlines():
			mappings.append(l.strip())
	except IOError:
		print "Trouble processing "+ mappingFile

def ProcessCSV( csv ):
	try:
		f = open(csv,'r')
		i=1
		for l in f.readlines():
			if i!=1 or not SKIP_FIRST_LINE:
				ProcessRow(l,i)
			i+=1
	except IOError:
		print "Trouble processing ", csv 

def ProcessRow(row,num):
	elems = row.split(DELIM)
	to_print = "INSERT INTO "+ TABLE+ " VALUES ("
	if USE_AI:
		to_print += str(num) + ","
	for i in range(0,len(elems),1):
		elems[i]=elems[i].strip()
		if i < len(mappings):
			if mappings[i] == INTTYPE:
				to_print += elems[i] 
				if i < len(elems)-1:
					to_print += ","
			elif mappings[i] == STRTYPE:
				to_print += "'"+elems[i]+"'"
				if i < len(elems)-1:
					to_print += ","
			elif mappings[i] == SKIP:
				continue
	
	to_print += ");"
	print to_print


def main(*args):

	if  len(args) != 3:
		print args[0], " csv_file mapping_file"
	
	
	else:
		ProcessMappingFile(args[2])
		ProcessCSV(args[1])
if __name__ == "__main__":
	main(*sys.argv)