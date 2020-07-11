import mysql.connector as sql
import pandas as pd
from sqlalchemy import create_engine


mydb = sql.connect(host = 'localhost', user = 'root', password = 'neomercazole')
mycursor = mydb.cursor()

engine = create_engine('mysql+mysqlconnector://root:neomercazole@localhost', echo=False)

class Table():

	def __init__(self, schema, tbl, cond = None):

		self.tbl = schema.strip() + '.' + tbl.strip()

		if cond is None: self.qry = 'select * from %s;' %(self.tbl)
		else: self.qry = 'select * from %s where %s;' %(self.tbl,cond)

		self.data = pd.read_sql ( self.qry , engine)

		self.cols = self.data.columns
		self.row_count = len(self.data.index)

		self.keys = get_data('select column_name, column_key from information_schema.columns \
							where table_schema = "%s" \
							and table_name = "%s" \
							and column_key is not null \
							and ltrim(rtrim(column_key)) != "" ' %(schema,tbl))

		self.user_connection = get_data ('select current_user();')[0][0].split('@')[0]


	def savetocsv(self):
		with open( self.tbl+'.csv', 'w' ) as f:
			for i in self.data.to_csv(index = False).split('\n')[:-1]:
				f.write( (',').join(i.split(',')) )

	def refreshDB(self):
		s,nm = self.tbl.split('.')
		self.data.to_sql( name=nm, con=engine, schema=s, if_exists='replace', index=False)

	def createqry(self):
		pri_key = [ i[0] for i in self.keys if i[1]=='PRI' ][0]
		non_key_cols = list(self.data.columns)
		non_key_cols.remove(pri_key)

		qry_ins = []
		qry_upd = []

		self.data2 = pd.read_csv(self.tbl+'.csv')

		new_key_vals = list (set( self.data2[pri_key] ) - set( self.data[pri_key] ) )
		for i in new_key_vals:
			fltr = (self.data2[pri_key] == i)
			values = []
			for val in self.cols:
				values.append( self.data2[fltr][val].values[0] )
			qry_ins.append( 'insert into %s values(%s)' %(self.tbl, ','.join(values)))
		print( qry_ins )

def get_data(qry):
	out = []
	x = engine.execute(qry)
	for row in x:
		out.append( [i for i in row] )
	return out

def add_data ():
	while(True):
		roll = int(input('Please Enter Roll_Num : '))
		nm = input('Please Enter Name : ').capitalize()
		contact = input('Please Enter Contact Num : ')
		email = input('Please Enter Email : ')
		qry = 'insert into stud_main values(%s, "%s", "%s", "%s")' %(roll,nm,contact,email)

		mycursor.execute( qry )

		if str(input('Wanna Quit? (y/n) : ')).upper().strip() == 'Y':
			mydb.commit()
			break



# t1 = Table('information_schema','columns','table_name = "stud_main" and table_schema = "atul"')
t1 = Table('atul','stud_main')
#t1.createqry()
#t1.savetocsv()
# filt = (t1.data['Roll_Num'] == 1207129)
# print( t1.data[filt]['IsActive','Email'].values)
# filt = (t1.data['Email'] == 'gupta.atul193@gmail.com')
# filt = t1.data['Email'].str.contains('kiit')
# t1.data['Email'].apply(lambda x:x.replace('kiit','infy'))
t1.data['newcol'] = 'Nan'
t1.data = t1.data.append({'Roll_Num':12121212}, ignore_index = True)
print(t1.data)
flt = (t1.data['Fullname'].str.upper() == 'ATUL GUPTA')
t1.data = t1.data.drop(index=t1.data[flt].index)
print(t1.data)
