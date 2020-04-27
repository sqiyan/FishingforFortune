# Fishing for Fortune
---
Text-based fishing simulation game using Python for 10.009 Digital World Final Exam Programming Assignment 2020 :)

### Backstory
---
In a quiet old town away from the city, 30 year old John lives in a little run-down shack by the sea letting the days go by, wasted in his poverty. The economy isn't doing too good these days, and John remains unemployed and unmotivated. 

He is a simple man with a simple wish: to move out of his run-down little house and have a proper home.

Just when it all seemed hopeless for John, one day, he found an old fishing rod washed up on shore. 
 
Maybe there was hope for him afterall.

### Game Objective
---
You are John. Well, John is you. And all you have to do, is fish for your fortune.

Catch fish -> Sell fish -> Earn money -> REPEAT

Earn more money till you have enough buy a house :)

## How to Play
---

### FISHING Mode
---
When player enters the FISHING mode, they will receive the following prompt:
```
#at the start of the game
Are you ready to start fishing? Enter 'F' to cast your fishing rod!

#after initial fishing
You're now FISHING. Enter 'F' to cast your rod!
```
In order to fish, enter `F` to cast your rod into the sea to lure some fishes. 
The following message will appear:

	Fishing... Patience is key.

It takes about 3-5 seconds for fishes to take the bait.
When a fish has been hooked, an alert will be displayed:

	!!!!!
	Quick! Press ENTER to catch the fish!

Respond quickly by hitting `ENTER` to catch the fish! Otherwise, it'll escape :(

After fishing, player is given an option to fish again or to go to their inventory

	Enter 'F' to FISH again OR Enter 'I' to check your INVENTORY!

In later stages of the game, where the player is able to purchase and owns fishing nets, the player receives a different prompt instead:

```
You're now FISHING. Enter 'F' to cast your rod or 'N' to use your fishing net!

#and

Enter 'F' to FISH again OR 'N' to use your FISHING NET
Enter 'I' to check your INVENTORY!
```

### INVENTORY Mode
---
Whenever player enters his inventory, he receives the following instructions:
```
Welcome to your INVENTORY! 
- Enter 'check' to see what fishes you have
- Enter 'stats' to see your fishing record
- Enter 'wallet' to check how much money you have
- Enter 'sell' to sell the fishes you have, remember, market rate is $0.50 per cm!
- Enter 'upgrade' to upgrade your fishing rod
- Enter 'buy' to purchase fishing nets
- Enter 'fish' to start fishing again!
```
Entering the specified input will allow the player to carry out the respective actions within the game

#### 'check'
This action returns the player a list of all the fish he has caught on hand
```
Saba Fish  -  27cm
Guppy  -  4cm
Guppy  -  3cm
King Salmon  -  138cm

What would you like to do next? Enter 'help' if you need the commands again!
```
#### 'stats'
This action returns the player's complete list of fishes ever caught since starting the game
```
John's Fishing Record!
					
Guppy : 0
Saba Fish : 1
King Salmon : 0
Giant Magikarp?? : 0
Largest Fish You Ever Caught : 27 cm

What would you like to do next? Enter 'help' if you need the commands again!
```
#### 'wallet'
This action returns the amount of money the player has currently
```
Wow, you have $13.5 right now.

What would you like to do next? Enter 'help' if you need the commands again!
```
#### 'sell'
An important action within the game is to sell fishes which the player has collected. This is done by inputting of `'sell'` by the player. This is an example of the message that the player will receive.
```
What a sale! You've earned $13.5!
You now have $13.5 in total.
Keep working hard :)

What would you like to do next? Enter 'help' if you need the commands again!
```
#### 'upgrade'
Another important action which allows users to upgrade their current rod to a better one with certain amount of payment.
The user receives a prompt which informs them of the stats of their current rod, and the stats of the upgraded rod, as well as
the cost of upgrading. The game then waits for their response on whether they would like to proceed with the upgrading.
```
Yay! Time to upgrade your rod!

Your next available rod is: Newer Rod!

probability of getting Guppy: 20%, 
probability of getting Saba Fish: 40%, 
probability of getting Norweigian Salmon: 30%, 
probability of getting Giant Magikarp??: 10%

COST: $100

Your previous rod (Old Rod)'s specifications:

probability of getting Guppy: 50%, 
probability of getting Saba Fish: 30%, 
probability of getting Norweigian Salmon: 15%, 
probability of getting Giant Magikarp??: 5%

Would you like to upgrade? Y/N

```
#### 'buy'
This action allows the player to purchase single-use fishing nets to use within the game and to store in their inventory. It has similar functions to a Rod, except it catches 5 fishes at a time, with a much more favourable probability. 
The player would receive the following prompt on whether he would like to continue with his purchase of fishing nets, answering with the quantity of nets to be purchased.
```
So you want to buy some fishing nets? Sure!
Let me explain how to use them again:

Each fishing net catches you five fishes at one time, and can only be used once, with:
probability of getting Guppy: 20%, 
probability of getting Saba Fish: 20%, 
probability of getting Norweigian Salmon: 30%, 
probability of getting Giant Magikarp??: 30%

After purchasing fishing nets, the option to enter 'N' will appear when you are FISHING.
Enter 'N' each time to use the fishing net(s) you have purchased.
Once all fishing nets purchased have been used up, you will no longer be given the option 'N'.

Price of 1 fishing net: $20

How many would you like to buy? 
Enter "None" if you'd like to cancel your purchase.
```
#### 'fish'
This action brings the player from the INVENTORY mode to the FISHING mode.
The player would receive a similar message to this:
```
It's fishing time!
...
You're now FISHING. Enter 'F' to cast your rod!
```
## How to Complete the Game
---
Upon the having $10,000 in their wallet, the player completes the game and receives the following message, terminating the game on his behalf:
```
******** WAIT A MINUTE ********

Oh my goodness! You've already earned $10,000! That's enough (in an ideal world) for John to move out from his 
old shack into a proper home! With the excess money, and his newly acquired knowledge on fishing,
John can now run his very own business as a fishing tycoon!

"Give a man a fish, and you feed him for a day. 
Teach a man to fish, and you feed him for a lifetime."

Thank you for helping John in his story of self-growth and perseverance :)

******** CONGRATULATIONS ********

You have completed the game. Kudos to you! 
  
Your Statistics!
					
Guppy : 39
Saba Fish : 32
King Salmon : 41
Giant Magikarp?? : 53
Largest Fish You Ever Caught : 446 cm

------------ GAME TERMINATED ------------

Fishing for Fortune
Copyright 2020 Seah Qi Yan

```
   
## Description of Code
---
### Player Class
The Player class is created to create an instance of the Player object, `user = Player()`, upon running of the python game file

Within the Player class, numerous class and object attributes are defined upon initialisation, such as `self.fishcount=0` and `self.net = "OFF"` to keep track of the player's fishes at hand, and the presence of fishing nets in the inventory for example.

The Player class also stores Rod object instances in a class attribute called `rodlist`, which indicates the types of Rods that players can own over the course of the game.

The Player class also consists of functions defined to be carried out within the game's state machine upon receiving certain input at certain states.

Examples of some important ones are:
#### sell_fishes(self)
This function utilises functions from the Rod object class.
```
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
```
#### upgrade_rod(self)
```
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
```
### Class Inheritance - Rod Class
The Rod class is inherited by subclasses that define different types of Rods within the game.

This class inheritance is integral as all forms of Rods within the game utilise the same functions `startfishing()` and `catch_fish()`, without the need to create new functions but similar for each type of rod.

Class inheritance also allows for subclass attributes to be modified with the change reflected within the inherited functions of the subclasses, without changing that of the superclass, Rod. This is particularly important due to the different probabilities associated with the different Rod types which affect the main functions `startfishing()` and `catch_fish()` for each rod.

More description can be found within the `.py` file of the game, where comments have been added extensively.
### State Machine
The State Machine, sm imported from libdw, allows for users to navigate the game through providing input to the machine, in turn performing desired actions in the game, such as fishing and selling fish. 

More description on code design can be found in comments of `.py` file.

An important aspect of the State Machine which detects completion of the game is the `done(self,state)` function. This functions checks the amount of money the player has accumulated at every `step` performed by the state machine. Should the amount of money exceed or be equal to 10,000, the state machine stops running and the game is terminated to end the game appropriately. 

```
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
```
