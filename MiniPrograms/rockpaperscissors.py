import player
import player2




player = player.Choices("Computer1", 3)

choice= player.setchoice()

player2 = player2.Choice2('Computer2', 3)

choice2=player2.setchoice() 

if choice == 'Rock':
	if choice2 == 'Scissors':
		print(player.getname(), " Wins! He got ", player.getchoice())
		print(player2.getname(), " Got ", player2.getchoice())
	elif choice2== "Paper":
		print(player2.getname(), " Wins! He got ", player2.getchoice())
		print(player.getname(), " Got ", player.getchoice())
	elif choice2== "Rock":
		print("It's a Tie!")

if choice == 'Paper':
	if choice2 == 'Scissors':
		print(player2.getname(), " Wins! He got ", player2.getchoice())
		print(player.getname(), " Got ", player.getchoice())
	elif choice2== "Paper":
		print("It's a Tie!")
	elif choice2 == 'Rock':
		print(player.getname(), " Wins! He got ", player.getchoice())
		print(player2.getname(), " Got ", player2.getchoice())


if choice == 'Scissors':
	if choice2 == 'Scissors':
		print("It's a Tie!")
	elif choice2=="Paper":
		print(player.getname(), " Wins! He got " ,player.getchoice())
		print(player2.getname(), " Got ", player2.getchoice())
	elif choice2 == 'Rock':
		print(player2.getname(), " Wins! He got " , player2.getchoice())
		print(player.getname(), " Got ", player.getchoice())

