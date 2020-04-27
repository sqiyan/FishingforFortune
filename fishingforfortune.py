import numpy as np
import random
import time
from libdw import sm

#Defining the class Rod, which encompasses functions that all rods/fish catching equipment have
class Rod:

	#n represents the number of fish caught a time by the type of rod, default value is 1
	n = 1

	#defines an attribute .chance, which is the probability of catching each type of fish, specific  to each rod
	def __init__(self):
		self.chance = [1]*self.stat1 + [2]*self.stat2 + [3]*self.stat3 + [4]*self.stat4

	#main function called to start fishing in the game, which also calls upon another function catch_fish
	def startfishing(self):
		n = self.n
		timer = random.randint(3,5)
		print("\n\tFishing... Patience is key.")
		time.sleep(timer)
		print("\t!!!!!")
		start = time.time()
		fishnames, fishlengths = self.catch_fish()
		input("\tQuick! Press ENTER to catch the fish!\n")
		end = time.time()
		duration = round(end-start,1)

		#function checks for the time it takes for player to react to the fishing prompt
		#if player takes longer than 1.5 seconds to enter an input, the fish is not caught
		if duration <= 1.5:
			for i in range(n):
				print("\n\tWoah! You caught a {}! It's {}cm long.".format(fishnames[i],fishlengths[i]))
				user.fishlist += "\n\t" + fishnames[i] + "  -  " + str(fishlengths[i]) + "cm"
				user.fishcount.append(fishlengths[i])
				

				user.fishdict[fishnames[i]] += 1

				if fishlengths[i] > user.largest:
					user.largest = fishlengths[i]
					user.fishdict["Largest Fish You Ever Caught"] = str(user.largest) + " cm"

		else:
			print("\n\tAww, it escaped.\n")

	# def catch_fish(self, self.n=1):
	def catch_fish(self):
		n = self.n
		probability = self.chance
		fishnames = []
		fishlengths = []

		#this function randomly chooses one type of fish to be caught out of the four.
		#the length of the type of fish caught is also randomly generated, with a specific range for each type.
		for i in range(n):
			fish = random.choice(probability)

			if fish == 1:
				fishname = "Guppy"
				fishlength = random.randint(3,6)

			elif fish == 2:
				fishname = "Saba Fish"
				fishlength = random.randint(10,60)

			elif fish == 3:
				fishname = "King Salmon"
				fishlength = random.randint(80,170)

			elif fish == 4:
				fishname = "Giant Magikarp??"
				fishlength = random.randint(200,450)

			fishnames.append(fishname)
			fishlengths.append(fishlength)

			#the steps below add on to the player's fishing history/statistics for every fish he catches
			# user.fishdict[fishname] += 1

			# if fishlength > user.largest:
			# 	user.largest = fishlength
			# 	user.fishdict["Largest Fish You Ever Caught"] = str(user.largest) + " cm"

		return fishnames, fishlengths

#CLASS INHERITANCE of Rod in different types of rods within the game

#Defining stat1, stat2, stat3 and stat4 for each type of rod allows for customisation
#of fishing probability for each rod, with the probability being higher for 'better quality'
#or more expensive fish as the upgrade becomes higher
class OldRod(Rod):
	"""
	STARTER ROD
	probability of getting 1: 50%, 
	probability of getting 2: 30%, 
	probability of getting 3: 15%, 
	probability of getting 4: 5%
	"""
	stat1 = 50
	stat2 = 30
	stat3 = 15
	stat4 = 5

class NewerRod(Rod):
	"""
	probability of getting 1: 20%, 
	probability of getting 2: 40%, 
	probability of getting 3: 30%, 
	probability of getting 4: 10%
	"""
	stat1 = 20
	stat2 = 40
	stat3 = 30
	stat4 = 10

class SuperRod5000(Rod):
	"""
	OP ROD
	probability of getting 1: 10%
	probability of getting 2: 15%
	probability of getting 3: 30%
	probability of getting 4: 45%
	"""
	stat1 = 10
	stat2 = 15
	stat3 = 30
	stat4 = 45

#This is a special type of rod, the Fishing Net
#the player does not own this rod, instead, it is a single-use purchasable tool/add-on in the game
#here, n has been defined as 5 as the fishing net can catch 5 fishes for each time the user uses it
#the fishing net is also a rod since it uses the same functions catch_fish and start_fishing
class FishingNet(Rod):
	"""
	catches 5 fish in a row, 1 time usage, probability is buffed
	probability of getting 1: 20%
	probability of getting 2: 20%
	probability of getting 3: 30%
	probability of getting 4: 30%
	"""
	stat1 = 20
	stat2 = 20
	stat3 = 30
	stat4 = 30 
	n = 5

#Object instantiation for the rods used in the game
#this allows the rod's functions to be callable within the state machine and by the Player object

oldrod = OldRod()
newerrod = NewerRod()
superrod = SuperRod5000()
fishingnet = FishingNet()

#Defining the Player class - this class creates an object called the Player, which encompasses
#common attributes used and accessed by the user in the game
class Player:
	name = "John"

	#This is the fish dictionary, it keeps track of total no. of each type of fish caught
	#by the player throughout the entire game, as well as the longest fish ever caught
	fishdict = {
	"Guppy" : 0,
	"Saba Fish" : 0,
	"King Salmon" : 0,
	"Giant Magikarp??" : 0,
	"Largest Fish You Ever Caught" : ""
	}
	
	#rod list is a list of the rods that can be owned/used by the user/player
	rodlist = [oldrod, newerrod, superrod]

	#net = "OFF" and netcount = 0 defines the default state whereby the player does not own any nets at the start of the game
	#therefore the player is not allowed to use any nets
	net = "OFF"
	netcount = 0

	#an arbitrary value set to start storing the largest length of fish caught
	largest = 1


	#When player starts the game, he has no fishes, $0 and starts with the starter rod, Old Rod.
	def __init__(self):
		self.fishcount = []
		self.fishlist = ""
		self.coins = 0
		self.rod = self.rodlist[0]

	#A function that is called when user wants to check how much money he has
	def get_coins(self):
		print("\n\tWow, you have ${} right now.\n".format(self.coins))
		return self.coins

	#The function called when user wants to check how many fishes he has currently
	def my_fishes(self):
		if self.fishlist == "":
			print("\n\tYou don't have any fishes right now.\n")
		else:
			print(self.fishlist)

	#Function called when user wants to sell the fishes he has on him currently
	def sell_fishes(self):

		#catches the scenario where the user has no fish to sell, returns him back to previous action
		if self.fishcount == []:
			print("\n\tHey, who are you trying to kid? You haven't fished anything to sell!\n")
			return
		total_lengths = sum(self.fishcount)
		#profit = total length of fishes he has caught (in cm) x Market rate for fishes ($0.50 per cm)
		profit = total_lengths * 0.50
		self.coins += profit
		#fishcount and fishlist is reset everytime he makes a sale
		self.fishcount = []
		self.fishlist = ""
		print("""
		
	What a sale! You've earned ${}!
	You now have ${} in total.
	Keep working hard :)

		""".format(profit,self.coins))

	#Function called when user wants to purchase some single-use fishing nets to use in game
	def buy_nets(self):
		print("""
	So you want to buy some fishing nets? Sure!
	Let me explain how to use them again:

	Each fishing net catches you five fishes at one time, and can only be used once, with:
	probability of getting Guppy: {0}%, 
	probability of getting Saba Fish: {1}%, 
	probability of getting Norweigian Salmon: {2}%, 
	probability of getting Giant Magikarp??: {3}%

	After purchasing fishing nets, the option to enter 'N' will appear when you are FISHING.
	Enter 'N' each time to use the fishing net(s) you have purchased.
	Once all fishing nets purchased have been used up, you will no longer be given the option 'N'.

	Price of 1 fishing net: $20

	How many would you like to buy? 
	Enter "None" if you'd like to cancel your purchase.
	""".format(fishingnet.stat1,fishingnet.stat2,fishingnet.stat3,fishingnet.stat4))
		ans = input(">>>")
		#This allows for the user to go back to his previous action if he changes his mind
		#and doesn't want to buy a net anymore
		if ans == "None":
			return

		#this catches the error whereby the string input by the user is not an integer and cannot be converted to integer type,
		#hence preventing an error that crashes the game
		try:
			int(ans)
		except:
			print("\n\tThat's an invalid number! Please try again :)\n")
			self.buy_nets()
		else:
			#checks amount of money user has
			balance = self.coins
			ans = int(ans)
			#check if his amount of money is sufficient
			if balance >= ans*20:
				self.net = "ON"
				self.coins = self.coins - ans*20
				self.netcount += ans
				print("""

	Thank you for your payment!
	You have purchased {0} fishing nets.
	Your current coin balance is: ${1}.

					""".format(int(ans),self.coins))

			#else, the transaction does not go through and user is sent back to previous action
			else:
				print("""

	Oh no! You don't have enough money.
	Your current coin balance is: ${}.
	Please purchase lesser nets OR come back when you have more :)

					""".format(self.coins))

		return

	#Function called when player would like to upgrade his current fishing rod
	def upgrade_rod(self):
		"""
		PRICELIST:

		NEWER ROD: requires $100
		SUPER ROD 5000: requires $1000
		"""
		namelist = ["Newer Rod","SUPER ROD 5000"]
		pricelist = [100,1000]
		index = self.rodlist.index(self.rod)

		#Catches the scenario where the player has upgraded to the best rod and it cannot be upgraded further
		if index == 2:
			print("\n\tSorry! You've reached your maximum upgrade :)\n")
			return 

		balance = self.coins
		print("""

	Yay! Time to upgrade your rod!

	Your next available rod is: {0}!

	probability of getting Guppy: {1}%, 
	probability of getting Saba Fish: {2}%, 
	probability of getting Norweigian Salmon: {3}%, 
	probability of getting Giant Magikarp??: {4}%

	COST: ${5}

	Your previous rod (Old Rod)'s specifications:

	probability of getting Guppy: {6}%, 
	probability of getting Saba Fish: {7}%, 
	probability of getting Norweigian Salmon: {8}%, 
	probability of getting Giant Magikarp??: {9}%

	Would you like to upgrade? Y/N
		""".format(namelist[index],self.rodlist[index+1].stat1,self.rodlist[index+1].stat2,self.rodlist[index+1].stat3,self.rodlist[index+1].stat4,pricelist[index],self.rodlist[index].stat1,self.rodlist[index].stat2,self.rodlist[index].stat3,self.rodlist[index].stat4))
		#Player decides whether or not to upgrade
		key = input(">>>")
		if key == "Y":

			#checks if player has enough money to upgrade his rod
			if balance >= pricelist[index]:
				self.rod = self.rodlist[index+1]
				self.coins = self.coins - pricelist[index]
				print("""

	Thank you for your payment!
	Your rod has been upgraded to {0}.
	Your current coin balance is: ${1}.

					""".format(namelist[index],self.coins))

			#message that he receives if he does not have enough money
			else:
				print("""

	Oh no! You don't have enough money.
	Your current coin balance is: ${}.
	Please come back when you have more :)

					""".format(self.coins))

		elif key == "N":
			return

		#function is called again if player does not answer with the right input
		else:
			print("\n\tThat's not the right answer, try again!\n")
			self.upgrade_rod()

		return


#Defines a class for the state machine which controls the different states of the game
class FishingGame(sm.SM):

	start_state = "INIT"

	#instructions that player will receive upon running the python game file
	introduction = """

	In a quiet old town away from the city, 30 year old John lives in a little run-down shack by the sea
	letting the days go by, wasted in his poverty. The economy isn't doing too good these days, and John 
	remains unemployed and unmotivated. 

	He is a simple man with a simple wish: to move out of his run-down little house
	and have a proper home.

	Just when it all seemed hopeless for John, one day, he found an old fishing rod washed
	up on shore. 

	Maybe there was hope for him afterall.


	OBJECTIVE:
	You are John. Well, John is you. And all you have to do, is fish for your fortune.
	Catch fish -> Sell fish -> Earn money -> REPEAT
	Earn more money till you have enough buy a house :)

	
	HOW TO PLAY:

	FISHING
	In order to fish, press F to cast your rod into the sea to lure some fishes. 
	The following message will appear:

	"Fishing... Patience is key."

	It takes about 3-5 seconds for fishes to take the bait.
	When a fish has been hooked, an alert will be displayed:

	"!!!!!
	Quick! Press ENTER to catch the fish!"

	Respond quickly to catch the fish! Otherwise, it'll escape :(

	INVENTORY
	You can access the inventory after you have fished, through the command 'I' 
	and vice versa, through the command 'fish'.

	This is the important place where you can sell your fishes, upgrade your rod,
	and also buy some special fishing nets! 

	Remember, the market rate for fishes is: 
	$0.50 per cm of fish :)

	So the bigger (longer) the fish, the better!

	At the inventory, you can also do several other things, but I'll explain them to you later,
	I'm pretty sure you'd forget by then, haha (I mean, I would too)

	And that's all you need to know for now!

	Enter 'S' to start the game, and 'Q' to quit.
	"""

	#instructions received by player to learn how to navigate the inventory
	inv_instructions = """
	Welcome to your INVENTORY! 
	- Enter 'check' to see what fishes you have
	- Enter 'stats' to see your fishing record
	- Enter 'wallet' to check how much money you have
	- Enter 'sell' to sell the fishes you have, remember, market rate is $0.50 per cm!
	- Enter 'upgrade' to upgrade your fishing rod
	- Enter 'buy' to purchase fishing nets
	- Enter 'fish' to start fishing again!
	"""

	#message received by player upon completion of the game
	#he also receives his game statistics at the end of the game
	credits = """

	******** WAIT A MINUTE ********

	Oh my goodness! You've already earned $10,000! That's enough (in an ideal world) for John to move out from his 
	old shack into a proper home! With the excess money, and his newly acquired knowledge on fishing,
	John can now run his very own business as a fishing tycoon!

	"Give a man a fish, and you feed him for a day. 
	Teach a man to fish, and you feed him for a lifetime."

	Thank you for helping John in his story of self-growth and perseverance :)

	******** CONGRATULATIONS ********

	You have completed the game. Kudos to you! 
	"""

	#checks current state and input received from user to determine which functions to be called (which actions to carry out)
	def get_next_values(self,state,inp):

		#to start the game
		if inp == "S" and state == "INIT":
			output = "\n\tHey there, John! Welcome to your first step towards a little more fortune. \n\tAre you ready to start fishing? Enter 'F' to cast your fishing rod!\n"
			next_state = "FISH"

		#to quit the game when it has already been started
		elif inp == "Q" and (state == "FISH" or state == "INVENTORY"):
			next_state = state
			#this is a prompt in case the player accidentally tried to quit the game
			#allowing him to return to the previous state and continue playing where he left off
			print("""
	Aw, leaving already? But John hasn't fulfilled dream yet :(
	Enter 'Q' again if you'd really like to quit, 
	else enter ANY KEY if you'd like to continue playing.
	Remember, your game data is lost once you quit!
			""")
			ans = input(">>>")
			if ans == "Q":
				output = """
	Alright then, see you! 
	Thanks for helping John out :) 
				"""
				next_state = "QUIT"
			else: 
				output = """
	Yay, you stayed!
	Please enter what you'd like to do next :)
				"""

		#This is the state where the player is fishing by the sea
		elif state == "FISH":

			next_state = state
			
			#checks for whether the user has any fishing nets in his inventory
			if user.net == "ON":

				#if he does, he is allowed to use the command 'N' to use his net when fishing
				output = "\tEnter 'F' to FISH again OR 'N' to use your FISHING NET \n\tOR Enter 'I' to check your INVENTORY!\n"
		
			#if he does not have any nets, user.net = "OFF" and he is only allowed to use 'F' and 'I' commands
			else:
				output = "\tEnter 'F' to FISH again OR Enter 'I' to check your INVENTORY!\n"

			#Calls the function for the rod currently used by the user to start fishing
			if inp == "F":
				user.rod.startfishing()
# 				if user.net == "ON":
# 					output = """
# Enter 'F' to FISH again OR 'N' to use your FISHING NET 
# OR Enter 'I' to check your INVENTORY!
# 					"""
# 				else:
# 					output = "Enter 'F' to FISH again OR Enter 'I' to check your INVENTORY!"

			#Calls the function for the fishing net to be used by the user
			if inp == "N":
				if user.net == "ON":
					fishingnet.startfishing()

					#after each use of the fishing net, the player uses up 1 net in his inventory
					user.netcount -= 1

					#if he runs out of nets to use, he is given a message and can no longer use command 'N'
					if user.netcount == 0: 
						user.net = "OFF"
						output = "\tYou've used up all your fishing nets!\n\tEnter 'F' to FISH again OR Enter 'I' to check your INVENTORY!\n"
			
			#Allows user to transit from state FISHING to state INVENTORY to access his inventory
			#the inventory instructions are reiterated to him each time he transits to inventory state
			elif inp == "I":
				next_state = "INVENTORY"
				output = self.inv_instructions

		#the state where the user performs actions in the inventory
		elif state == "INVENTORY":

			#default output that is given to user once he performs an action
			output = "\n\tWhat would you like to do next? Enter 'help' if you need the commands again!\n"
			next_state = state

			#calls the function to check for the number of fishes he has
			if inp == "check":
				user.my_fishes()

			#calls the function to check his fishing dictionary class attribute which updates everytime he fishes
			elif inp == "stats":
				print("""
	John's Fishing Record!
					""")
				for i in user.fishdict:
					print("\t{0} : {1}".format(i,user.fishdict[i]))

			#calls the function to check the amount of money the user has
			elif inp == "wallet":
				user.get_coins()

			#calls the function to allow the user to sell the fishes he has at hand
			elif inp == "sell":
				user.sell_fishes()

			#calls the function to upgrade the user's rod
			elif inp == "upgrade":
				user.upgrade_rod()

			#calls the function to allow the user to buy nets to add to his inventory to be used at FISHING state
			elif inp == "buy":
				user.buy_nets()

			#reiterates the commands that can be used in the inventory to the user
			elif inp == 'help':
				output = self.inv_instructions

			#allows user to transit from state INVENTORY to state FISHING
			elif inp == "fish":
				next_state = "FISH"
				#allows the message seen by the user when going to fish to alternate between 3 different messages
				words = ["\n\tLet's get to fishing!", "\n\tYou can't get rich without doing anything! Let's fish!", "\n\tIt's fishing time!"]
				print(random.choice(words))
				print("\t...")
				time.sleep(1)

				#checks if the user has any nets, gives him the appropriate instructions
				if user.net == "ON":
					output = "\tYou're now FISHING. Enter 'F' to cast your rod or 'N' to use your fishing net!\n"
				else:
					output = "\tYou're now FISHING. Enter 'F' to cast your rod!\n"

			#catches invalid commands/inputs given to the state machine in the inventory state
			else:
				output = "\n\tHey, that's not a command! Try again please :)\n"

		#if game is quit before it is even started
		elif inp == "Q" and state == "INIT":
			output = "\n\tOkay then, bye!\n"
			next_state = "QUIT"

		#catches invalid commands/inputs given to the state machine in the any other case
		else:
			next_state = state
			output = "\n\tHey, that's not a command! Try again please :)\n"

		return next_state, output

	#checks if the user has completed the game --> reached the end goal of $10,000
	def done(self,state):
		if state != "INIT":
			money = user.coins
			if money >= 10000:
				return True
			return False
		else:
			return False

	def run(self):
		self.start()
		print(self.introduction)
		while(True):

			if self.done(self.state) == False:
				inp = input(">>>")
				output = self.step(inp)
				print(output)

				if self.state == "QUIT":
					break

			#if self.done(self.state) == True, game has been completed, roll credits for player		
			else:
				print(self.credits)
				print("""
	Your Statistics!
					""")
				for i in user.fishdict:
					print("\t{0} : {1}".format(i,user.fishdict[i]))
				break


		print("""
	------------ GAME TERMINATED ------------\n\n\tFishing for Fortune\n\tCopyright 2020 Seah Qi Yan\n""")

user = Player()
game = FishingGame()
game.run()












			


















