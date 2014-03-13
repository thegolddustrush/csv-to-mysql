Simple python script to convert a csv file to mysql

How to run:

python csv_to_mysql.py table_to_parse.csv mapping.txt

csv files can use different delimiters. You can open the script and specify what delimiter to use by changing the DELIM variable. 

Variables in csv_to_mysql.py:

- DELIM : csv field delimiiter
- TABLE : table the generated insert statements will be for
- USE_AI : whether to include autoincrement field in beginning 
- SKIP_FIRST_LINE : whether to skip the first line 
- INTTYPE : what the mapping file will use for int types
- STRTYPE : what the mapping file will use for string types
- SKIP : what the mapping file will use to skip a column in the csv

The mapping file:

Each line in the file denotes whether to skip a field or what type of field it is.


skip
int
str

The above 3 lines means that the first field will be skipped, the second treated as an int and the last is a string. You can change the words used in the mapping file by setting the SKIP, INT, and STR variables in the python script.



Warning:
Definitely needs some work to expand its functionality since it doesn't include field names in the generated insert statements.


It assumes the fields you choose via the mapping file match what's in your table.

