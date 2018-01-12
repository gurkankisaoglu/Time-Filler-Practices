import getpass
import os

player1Name=raw_input("Enter your name: ")
while True:
	dic1={}
	player1Number=getpass.getpass("Choose your number: ")
	for index in range(len(player1Number)):
		dic1.setdefault(index,player1Number[index])
	if len(player1Number)!=5 or len(dic1.values())!=len(player1Number):
		print "Choose a 5digit number with different numbers!!!"
	else:
		break

player2Name=raw_input("Enter your name: ")
while True:
	dic2={}
	player2Number=getpass.getpass("Choose your number: ")
	for index in range(len(player2Number)):
		dic2.setdefault(index,player2Number[index])
	if len(player2Number)!=5 or len(dic2.values())!=len(player2Number):
		print "Choose a 5digit number with different numbers!!!"
	else:
		break

guesses1=[]
guesses1keys=[]
guesses2=[]
guesses2keys=[]


while True:
	clear = lambda: os.system('clear')
	print "Make your guess"+" "+player1Name
	while True:
		guess1=raw_input()
		if guess1 in guesses1keys:
			print "You have allready said this number, guess another number"+" "+player1Name
		else:
			guesses1keys.append(guess1)
		break
	if guess1==player2Number:
		print player1Name.upper()+" "+"GUESSED CORRECT!!!!"
		print "You have one more chance to Draw"+" "+player2Name
		guesslast2=raw_input()
		if guesslast2==player1Number:
			print player2Name.upper()+" "+"GUESSED CORRECT!!!!"
			print "DRAW"
		else:
			print player2Name+" couldnt guessed correct number; "+player1Name.upper()+" "+"HAS WON"
		break
	trueIndex1=0
	trueNumber1=0
	for number in guess1:
		if number in dic2.values() and player2Number.find(number)==guess1.find(number):
			trueIndex1+=1
		if number in dic2.values() and player2Number.find(number)!=guess1.find(number):
			trueNumber1-=1
	guesses1.append([guess1,[trueNumber1,trueIndex1]])
	clear()
	print player1Name.upper()+"'s"+" "+"GUESSES:"	
	for element in guesses1:
		print element 
	print ""
	print player2Name.upper()+"'s"+" "+"GUESSES:"
	for element in guesses2:
		print element  
	print ""
	while True:
		print "Make your guess"+" "+player2Name
		while True:
			guess2=raw_input()
			if guess2 in guesses2keys:
				print "You have allready said this number, guess another number"+" "+player2Name
			else:
				guesses2keys.append(guess2)
			break
		if guess2==player1Number:
			print player2Name.upper()+" "+"GUESSED CORRECT!!!!"
			print "You have one more chance to Draw"+" "+player1Name
			guesslast1=raw_input()
			if guesslast1==player2Number:
				print player1Name.upper()+" "+"GUESSED CORRECT!!!!"
				print "DRAW"
			else:
				print player1Name+" couldnt guessed correct number; "+player2Name.upper()+" "+"HAS WON"
			break
		trueIndex2=0
		trueNumber2=0
		for number in guess2:
			if number in dic1.values() and player1Number.find(number)==guess2.find(number):
				trueIndex2+=1
			if number in dic1.values() and player1Number.find(number)!=guess2.find(number):
				trueNumber2-=1
		guesses2.append([guess2,[trueNumber2,trueIndex2]])
		clear()
		print player1Name.upper()+"'s"+" "+"GUESSES:"
		for element in guesses1:
			print element 
		print ""
		print player2Name.upper()+"'s"+" "+"GUESSES:"
		for element in guesses2:
			print element 
		print ""
		break
	if guess2==player1Number:
		break	
