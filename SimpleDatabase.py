import sys, shelve

def store_person(db):
	"""
	Query user for data and store it in the shelf object
	"""
	
	pid = raw_input('Enter a unique ID number: ') #Here we store the personal id number
	person = {} #Here is the dictionary where we keep the person's information
	person['name'] = raw_input('Enter name: ')
	person['age'] = raw_input('Enter age: ')
	person['phone'] = raw_input('Enter phone number: ')
	person['gender'] = raw_input('Enter gender: ')
	
	db[pid] = person#db = database,the database with the key 'pid' is dictionary its stored in,which is person


def store_debts(db):
	debtid = raw_input('Enter a unique ID number: ')
	debtCollection = {}
	debtCollection['object'] = raw_input('Describe the object: ')
	debtCollection['money'] = raw_input('Describe the amount($): ')
	
	
	db[debtid] = debtCollection
	
def lookup_debt(db):
	debtid = raw_input('Enter ID number: ')
	debtfield = raw_input('What would you like to know? (object,money) ')
	debtfield = debtfield.strip().lower()
	
	print debtfield.capitalize() + ':', db[debtid][debtfield]

	
	
	
	print db[debtid],[debtfield]
	
def lookup_person(db):
	"""
	Query user for ID and desired field, and fetch the corresponding data from
	the shelf object
	"""
	
	pid = raw_input('Enter ID number: ')
	field = raw_input('What would you like to know? (name,age,phone,gender) ')
	field = field.strip().lower() #This allows the user to be as sloppy and 
								  #allows them to use either uppercase or lowercase letters
	
	print field.capitalize() + ':', db[pid][field]
	
	print "Here is the database: \n", db
		
	print db[pid],[field]
		
def print_help():
	 print 'The available commands are: '
	 print 'store : Stores information about a person'
	 print 'lookup : Looks up a person from ID number'
	 print 'quit: Saves changes and exit'
	 print '? : Prints this message'
	 
def enter_command():
	cmd = raw_input('Enter command (? for help): ')
	cmd = cmd.strip().lower()
	return cmd
	
def main():
	database = shelve.open('C:\\database.dat')
	try:
		cmd = enter_command()
		
		if cmd == 'store':
			decision = raw_input('store(person/debt)?: ')
			if decision == 'person':
				store_person(database)
			elif decision == 'debt':
				store_debts(database)
				
		elif cmd == 'lookup':
			decision = raw_input('Are you looking for (person,debts)?: ')
			
			if decision == 'person':
				lookup_person(database)
			
			elif decision == 'object':
				lookup_debt(database)
		
		elif cmd == '?':
			print_help()
			print "\n"
			return enter_command()
			
		elif cmd == 'quit':
			return
			
	finally:
		database.close()
		
		
		
if __name__ == '__main__': main()
