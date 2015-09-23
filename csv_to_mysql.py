import sys

DELIM=","
TABLE="osp$award_custom_data "
USE_AI=False #assume autoincrement is last
SKIP_FIRST_LINE=True
INTTYPE="int"
STRTYPE="str"
SKIP="skip"
USE_UPDATE=1
UPDATE_FIRST_IS_KEY=1
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
                if not USE_UPDATE:
                    ProcessRow(l,i)
                else:
                    ProcessRowForUpdate(l,i)
            i+=1
    except IOError:
        print "Trouble processing ", csv 

def ProcessRowForUpdate(row,num):
    elems = row.split(DELIM)
    
    if len(elems) != 4 :
        return
    
    to_print = "UPDATE "+ TABLE+ " SET "
    for i in range(0,len(elems),1):
        elems[i] = elems[i].strip()    
    to_print += " update_timestamp='21-SEP-2015' , update_user='username' , column_value = '" + elems[3] + "' WHERE mit_award_number = '" + elems[0] +"' and sequence_number = " + elems[1] + " and column_name = '" + elems[2] + "' ;"
    
    print to_print

        
        
def ProcessRow(row,num):

    elems = row.split(DELIM)
    to_print = "INSERT INTO "+ TABLE+ " VALUES ("
    for i in range(0,len(elems),1):
        elems[i]=elems[i].strip()
        if i < len(mappings):
            if mappings[i] == INTTYPE:
                if not elems[i]:
                    to_print += "0"
                else:
                    to_print += elems[i] 
                if i < len(elems)-1:
                    to_print += ","
            elif mappings[i] == STRTYPE:
                to_print += "'"+elems[i]+"'"
                if i < len(elems)-1:
                    to_print += ","
            elif mappings[i] == SKIP:
                continue
    if USE_AI:
        to_print += ","+str(num)
    to_print += ");"
    print to_print

# for vendors
def RowToObjectVendor(csv):
    try :
        f = open(csv,'r')
        for l in f.readlines():
            elems = l.split(DELIM)
            print "_VendorCatalogItems.Add(new VendorCatalogItem(){"
            for i in range(0,len(elems),1):
                elems[i] = elems[i].strip()
            
            print "VendorId = ", elems[1] , ","
            print "CatalogId = \""+ elems[2] + "\","
            print "SpeciesId = ", elems[3] , ","
            print "VendorStrainDesc = \"" + elems[4]+ "\","
            print "Strain = \"" +elems[5]+  "\","
            print "SubStrain = \"" + elems[6]+ "\" });"
            
    except IOError:
        print "Trouble processing file "

# for antibiotics
def RowToObjectAntibiotics(csv):
    
    try :
        f = open(csv,'r')
        for l in f.readlines():
            elems = l.split(DELIM)
            print "_Antibiotics.Add(new AntibioticItem(){"
            for i in range(0,len(elems),1):
                elems[i] = elems[i].strip()
            
            print "DrugShort = \""+ elems[2] + "\","
            print "SpeciesId = ", elems[3] , ","
            print "DrugDescription = \"" + elems[4]+ "\","
            print "Dose = \"" +elems[6]+  "\","
            print "Units = \"" + elems[7]+ "\","
            print "Route = \"" + elems[8]+ "\","
            print "CS = \"" + elems[9]+ "\","
            print "Volatile = \"" + elems[10]+ "\","
            print "Comment = \"" + elems[11]+ "\","
            print "Source = \"" + elems[12]+ "\"});"
    except IOError, e:
        print "Trouble processing file ", e

def RowToObject_euthanasia_species(csv):
    
    try :
        f = open(csv,'r')
        for l in f.readlines():
            elems = l.split(DELIM)
            print "DispositionSpeciesItems.Add(new DispositionSpeciesItem(){"
            for i in range(0,len(elems),1):
                elems[i] = elems[i].strip()
            
            print "Species = \""+ elems[0] + "\","
            print "DispositionId = "+ elems[2] + "});"
    except IOError, e:
        print "Trouble processing file ", e
def RowToObject_euthanasia_method(csv):
    
    try :
        f = open(csv,'r')
        for l in f.readlines():
            elems = l.split(DELIM)
            print "DispositionItems.Add(new DispositionItem(){"
            for i in range(0,len(elems),1):
                elems[i] = elems[i].strip()
            
            print "Method = \""+ elems[1] + "\","
            print "DispositionId = "+ elems[3] + ","
            print "IsEuthanasia = \""+ elems[4] + "\"});"
    except IOError, e:
        print "Trouble processing file ", e

def RowToObject(csv):
    
    try :
        f = open(csv,'r')
        for l in f.readlines():
            elems = l.split(DELIM)
            print "_EuthanasiaDrugItems.Add(new EuthanasiaDrugItem(){"
            for i in range(0,len(elems),1):
                elems[i] = elems[i].strip()
            
            
            print "DrugShort = \""+ elems[1] + "\","
            print "DrugDescription = \"" + elems[2]+ "\","
            print "SpeciesId = ", elems[3] , ","
            print "Dose = \"" +elems[5]+  "\","
            print "Units = \"" + elems[6]+ "\","
            print "Route = \"" + elems[8]+ "\","
            print "CS = \"" + elems[9]+ "\","
            print "Volatile = \"" + elems[10]+ "\","
            print "Comment = \"" + elems[11]+ "\","
            print "Source = \"" + elems[12]+ "\"});"
    except IOError, e:
        print "Trouble processing file ", e

def main(*args):

    if len(args) == 2:
        RowToObject(args[1])
    elif len(args) != 3:
        print args[0], " csv_file mapping_file"
    
    
    else:
        ProcessMappingFile(args[2])
        ProcessCSV(args[1])
if __name__ == "__main__":
    main(*sys.argv)