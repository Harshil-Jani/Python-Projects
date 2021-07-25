import random

print("Try Your Luck with this Guess Game")
print("Credited to : Harshil Jani")
print("Made using Python Language !")
print("Dated : 2nd July 2021")
print("\n")
t = int(input("Enter the number of Rounds You wanna play : "))
print("\n")
score = 0
k = 0
while t>0 :
	print("\n")
	num = random.randint(0,1000)	
	low = int(input("Guess the Lowest Possible Range : "))
	high = int(input("Guess the Highest Possible Range : "))
	
	if num>=low and num<=high :
		print("\n")
		print("YOU WON")
		score += 1000/(high - low)
		
	else:
		print("\n")
		print("YOU LOSE")
		score -= 1
	k += 1
	print("\n")
	print("The Random number was ", num)	
	print("Your Score is ",score)
	print("\n")
	print("######---------Round",k,"Ends here---------#####")
	t -= 1
	
print("\n")
print("!!!!!!!!!!!!!Game Ends Here!!!!!!!!!!!!!")
print("\n")
print("Your Final Score is ",score/k)

