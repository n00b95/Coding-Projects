from random import randint

print "Its time to play: \n"

print """   _   _   _   _   _     _   _   _   _     _   _   _   _   _   _  
  / \ / \ / \ / \ / \   / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ 
 ( g ( u ( e ( s ( s ) ( t ( h ( i ( s ) ( n ( u ( m ( b ( e ( r )
  \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \n"""
  
print "Keep in mind that you only have 6 tries to win! \n"

print "Goodluck! \n"
  
number = randint(1,10)

guess = int(raw_input("Guess an number from 1 to 10!"))

while guess != number:
	
	guesses = 0
	
	while guesses < 6:
	
		if guess > number:
			print "Too High!"
			guesses +=1
			guess = int(raw_input("Guess an number from 1 to 10!"))
		
		elif guess < number:
			print "Too low!"
			guesses +=1
			guess = int(raw_input("Guess an number from 1 to 10!"))
			
		elif guess == number:
			print "WINNER!"
			exit(0)
		
	if guesses == 6:
		print """ _____ _____ _____ _____    _____ _____ _____ _____ 
|   __|  _  |     |   __|  |     |  |  |   __| __  |
|  |  |     | | | |   __|  |  |  |  |  |   __|    -|
|_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|"""
		exit(0)
