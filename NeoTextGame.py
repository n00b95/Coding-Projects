from sys import exit
from random import randint
import random
import sys
import time


class Scene(object):
	
	def enter(self):
		print"This scene is not yet configured"
		return Home_
		
	
class Engine(object):
	
	
	
	def __init__(self,scene_map): #Initialize the scene map
		#print "Engine __init__ has scene_map", scene_map
		self.scene_map = scene_map #Scene map is self returning the scene map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()  #The current scene is self, calling the scene map, calling the opening scene
		#print "Play's first scene", current_scene
	
		
		while True:
		
			print "\n-------"
			
			#Weapon = self.weapon
			
			next_scene_name = current_scene.enter() #The next scene is the current scene, which calls the enter function
			#print "The next scene is:", next_scene_name
			current_scene = self.scene_map.next_scene(next_scene_name) #The current scene is self, calling the scene map, calling the next scene, with the next scene name in it
			#print "The map moves onto a new scene:>", current_scene
			
class Death(Scene):
	
	def enter(self):
		pass
		
class Home_(Scene):
	def enter(self):
		name = raw_input("First, choose your name....")
		print"The alarm clock wakes you up from your nap"
		print "Here you are, waking up for another day at work"
		print "It seems as if your life is a never ending spiral of work"
		print "and lack of sleep."
		print "You have two choices %s, you can either keep dreaming" % name
		print "Or get up for work, what will you do?"
		choice = raw_input("['stay in bed?'/'work?']> ")
		
		if choice == "stay in bed":
			return 'Dream'
		elif choice == 'work':
			return 'work'
		else:
			print "Be more clear about your choices"
			return 'Home'
			
class Goto_Job(Scene):
	def enter(self):
		
		print "You slap the off button on the alarm clock and slowly"
		print "rise off your bed. \n"
		print "You do the usual routine, shower, brush, breakfast"
		print "coffee, get dressed and head out the door. \n"
		print "You rush through traffic, find a parking spot and "
		print "finally get to your office. \n"
		print "You're a head software engineer at the company AMFAC. \n"
		print "Lets get to work now Mr. Smarty pants, guess your"
		print "login password to begin working. \n"
		login_pass = 'password'
		password = raw_input("Login:________")
		login_tries = 0
		#
		#
		while password != login_pass and login_tries < 10:
			print "WRONG PASSWORD \N"
			print "TRY AGAIN! \n"
			print "Heres a hint: Whats the most common password?"
			password = raw_input("Login:_______")
			login_tries += 1
		
		if password == 'password':
			return 'computer'
		else:
			return 'boss'
			
class Computer(Scene):
	def enter(self):
		print "SYSTEM LOGIN CORRECT"
		print "Alright winner, you're finally in the system."
		print "Funny thing is, you barely ever work on any software"
		print "while youre at work, you prefer to work from home. \n"
		print "Instead you use your talented programming skills to"
		print "hack your coworkers computers and see what theyre up to."
		print "You usually tell yourself you'll stop doing this, but"
		print "old habits are always the hardest to break \n"
		print "Lets see what your fellow coworkers are up to today, shall we? \n"
		
		
		
class Annoyed_Boss(Scene):
	def enter(self):
		pass
			
class Dream_exe(Scene):
	
	def enter(self):
		print "You turn the alarm clock off and go back to a deep sleep \n"
		print "You hear the alarm clock ringing again, and open your eyes to turn it off"
		print "But you notice that youre not in your room anymore,"
		print  "everything is...futuristic."
		print  "You hop off the bed and walk around this wierd new home you awoke in."
		print  "You look at the calender at what seems to be your kitchen...."
		print "It reads: 'Year 2096' ......."
		raw_input(" Press Enter To Continue")
		return 'living_room'
		
class Living_Room(Scene):
	def enter(self):
		print "You're confused, how could time have passed by so quickly?...\n"
		print "You sit on your futuristic couch and try to take it all in \n"
		print "You turn the Tv on and your heart drops yet again. \n"
		print "['ROBOTS REBEL, ALL CITIZENS PREPARE'] seems to be todays headline."
		print "As you sink into your couch and try to take all of this in at once \n"
		print "You hear a knock on your door. Company!, how nice....."
		print "You look through your remote control, which has a small touchscreen \n"
		print "that allows you to look through the camera of your door and notice \n"
		print "something off about your visitor....his....hers..its eyes are blazing red! \n"
		print "Now here's where the fun part begins, whats your next move? \n"
		print "Will you let the robot in? Or try and find cover like a reasonable"
		print "person would?"
		decision = raw_input(" ['let robot in' ]/[ 'find cover'] " )
		if decision == 'let robot in':
			return 'robot_door_death'
			#
		elif decision == 'find cover':
			return 'robot_escape'
		
class Robot_Escape(Scene):
	
	def enter(self):
		print "You have only 2 rooms you could escape to!\n"
		print "Choose either the bedroom or the garage! Quick!"
		print "He's...She's...It's getting closer!\n"
		#
		run_away = raw_input(" 'bedroom' / 'garage' ")
		if run_away == 'bedroom':
			return 'bedroom_death'
		elif run_away == 'garage':
			return 'garage'
		else:
			print "Choose quickly! It's closing in on you!"
			return 'robot_escape'
			
class Garage_Room(Scene):
	def enter(self):
		print "You quickly dash to the Garage room, just barely avoiding the"
		print "Robot's claw! You lock the door behind you but you know that"
		print "it wont hold up for long. You're gonna have to man up"
		print "and fight it!"
		print "You scramble around your garage looking for some tools. \n"
		print "You see 3 items laid out on the work table, a futuristic"
		print "wrench, a...light saber?, and a hammer"
		
		return 'Choose_Weapons'
		
class Choose_Weapons(Scene):
	def enter(self):
		choose = int(raw_input("1: Wrench/ 2: Light saber/ 3: Hammer"))
		if choose == 1:
			print "The robot finally breaks through the door! You quickly"
			print "grab the wrench, FIRMLY grasp it and take a quick swing at the robot!"
			return 'wrench_fight'	
			
		elif choose == 2:
			return 'saber_fight'
			
			
##########(WEAPONS CLASS/FIGHT)#################			
			
class Wrench_Fight(Scene):
	def enter(self):
		
		hit = 4 #This is the number you need to get to attack the robot
		#
		swing_wrench = randint(1,7) #This will make a random digit 
		#
		swings = 0 #This is the amount of swings you've taken
		
		attack = int(raw_input("Press 1 to swing!")) #
		
		if attack == 1:
			while swing_wrench != hit and swings < 10:
				print "miss!"
				swings += 1
				swing_wrench = randint(1,7)
				#
				attack = int(raw_input("Press 1 to swing again!"))
			if swing_wrench == hit:
				print "You got him!"
				
class Light_Saber_Fight(Scene):
	def enter(self):
	
		print "A wise choice, what kind of idiot would choose"
		print "regular tools to fight a robot?! \n"
		print "The robot breaks through the garage entrance door and"
		print "reaches for you with its metallic claw! Quick!"
		print "swing this saber of light at it!" 
		
		hit = 2 #This is the number you need to get to attack the robot
		#
		swing_saber = randint(1,5) #This will make a random digit 
		#
		swings = 0 #This is the amount of swings you've taken
		
		attack = int(raw_input("Press 1 to swing!")) #
		
		if attack == 1:
			while swing_saber != hit and swings < 10:
				print "miss! Keep swinging that light stick!"
				swings += 1
				swing_saber = randint(1,7)
				#
				attack = int(raw_input("[Press 1 to swing again!]"))
			if swing_saber == hit:
				print "You got him!"
				
				bomb_scene = turn_off(self.enter())
				
		
	def turn_off(self):
		return bomb_scene

		print "You slice the robots head off with this stick of"
		print "light.....this saber of light....oh right, its"
		print " ' light saber '. Anyways, great, the robot is dead! \n"
		print "Its even making the sound of defeat! It keeps making"
		print "this 'BZZZ BZZZ BZZZ' sound from its chest! \n"
		print "No...wait...that cant be right!....you"
		print "open up its chest and see that its initiated"
		print "its ' [SELF DESTRUCTION] ' sequence! Theres only"
		print "one way to deactivate it and thats by guessing the"
		print "code! Quick! Get to typing and guess the 3 digit"
		print "password!"
		
		bomb_code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		
		guess = raw_input("[Keypad]>")
		
		tries = 0
		
		while guess != bomb_code and tries < 10:
			print "BZZZZZ! 'TRY AGAIN' "
			tries += 1
			guess = raw_input("[Keypad>]")
			
		if guess == bomb_code:
			print "[SELF DESTRUCT DISACTIVATED]"	

        	 
class Hammer_Fight(Scene):
	def enter(self):
		print "You grab the tiny 4 inch hammer and thrust it at the robot \n"
		print "The robot looks at you with its red eyes, its not amused"
		print "at your poor choice of weaponry, infact its a little"
		print "offended you'd use such a wimpy tool against it!\n"
		print "It grabs you by the throat with its robot claw, closes you"
		print "in on its face and says 'Do you know whats the worst part"
		print " ? ' You try to shake your head 'no', but the claw is too"
		print "tight on your neck. The robot drops you from its claw,"
		print "closes you in to the corner of the wall and says \n"
		print " 'You still have to go to work. ' "
		return 'ending_2'
		
class Bedroom_Death(Scene):
	
	def enter(self):
		print "You dash to your bedroom in your underwear and lock the door behind you!\n"
		print "You hear the robot smash through the front door and start roaming your home\n"
		print "Its standing right outside your bedroom door, you can hear it... \n"
		print " ' maybe if i stay quiet enough ' you tell yourself, trying to"
		print "find some comfort in the situation, but ALAS you release"
		print "a loud, nasty, uncontrollable fart. A fart powerful"
		print "enough to set off the robot's heat sensors to locate you!"
		print "He smashes through the door, It grabs you from under the bed"
		print "and looks you in the eyes with its blazing red 'eyes' "
		print "and says........ \n"
		print "BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP"
		text ="GoodMorning City of Newyork! Im your host with the most......"
		for char in text: #for characters in text
			sys.stdout.write(char) #used for the output of print and 
			#						expression statements and for the prompts of input() 
			#						and raw_input().
			time.sleep(0.03)
			
		return 'back_to_reality'
		
class Reality(Scene):
	
	def enter(self):
		print "You forgot to hit the off button on the alarm, you only"
		print "hit snooze. Luckily the alarm went off before the robot decided to"
		print "decapitate you all because of a nasty fart. \n"
		print "You look to your left to check the time, its only been 8 minutes"
		print "since the last alarm went off."
		print "Now this is where the real nightmare begins.......\n"
		print "You have to go to work."
		return 'ending_2'
		
class Ending_2(Scene):
	def enter(self):
		print "Thanks for playing \n"
		print """ __   _   _____   _____  
|  \ | | | ____| /  _  \ 
|   \| | | |__   | | | | 
| |\   | |  __|  | | | | 
| | \  | | |___  | |_| | 
|_|  \_| |_____| \_____/ """

		exit(1) #Exits out with no errors
		
class EscapePod(Scene):

	def enter(self):
		pass
		
		
		
class Map(object):

	scenes = {'Home': Home_(),
			'computer' :Computer(),
			'boss' : Annoyed_Boss(), 
			'work' : Goto_Job(),
			'Dream': Dream_exe(),
			'living_room': Living_Room(),
			'robot_escape': Robot_Escape(),
			'garage': Garage_Room(),
			'bedroom_death': Bedroom_Death(),
			'back_to_reality':Reality(),
			'ending_2': Ending_2(),
			'Choose_Weapons' : Choose_Weapons(),
			'wrench_fight' : Wrench_Fight(),
			'saber_fight' :Light_Saber_Fight()
			 }
		
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self,next_scene_name):
		return Map.scenes.get(scenes)
	
	def opening_scene(self):
		return self.next_scene(self.start_scene) #Returns the opening scene
	
		
a_map = Map('Home')
a_game = Engine(a_map)
a_game.play()
