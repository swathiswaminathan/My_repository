import random

# #creating a list of words for hangman
word_list = ['book', 'cat', 'dog', 'apple', 'banana', 'class', 'python', 'java', 'rock', 'scissors', 'paper', 'run', 'walk', 'talk', 'try', 'evening', 'morning']

# #Word chosen by the program out of the word_list, using 'random' function - **Code works from the main() function**
def pick_random_word(given_list):
	random_word = given_list[random.randrange(len(given_list))]
	return random_word


#below print statment for just checking if the pick_random_word function works
#print "The secret word is ", pick_random_word(word_list)


# ********************+****
# #Function to ask the User for input - **code Works from the main() function **
# Validate the user input
# # *************************
def get_user_input(string_of_my_guess):
	while True:
				user_guess = raw_input("Guess the letter: ")
				user_guess = user_guess.lower()
				if user_guess not in 'abcdefghijklmnopqrstuvwxyz':
					print "Enter a valid letter: "
				elif len(user_guess)!= 1:
					print "Please enter a single letter: "
				elif user_guess in string_of_my_guess:
					print "You have already entered the letter once, please enter again: "
				else:
					return user_guess



# #Function to validate if the User input is present in the secret word, 
#if yes - add it to a string of correct letters, else append it to string of incorrect_letters
def check_user_input(guessed_word):
	length_of_guessed_word = len(guessed_word)
	string_of_my_correct_guess = ["_" for i in range(length_of_guessed_word)]
	print "Length of copy of guessed_word is ",string_of_my_correct_guess


	max_number_of_guesses = 8
	print """\n ***********************************************************************
			    Note that you've got maximum %i number of guesses at the max, """ % max_number_of_guesses
	print "**************************************************************************** \n"
	incorrect_letters = []
	list_of_my_guesses = []
	for i in range(8):
		user_guessed_letter = get_user_input(list_of_my_guesses)
		list_of_my_guesses.append(user_guessed_letter)
		print "the user input in iteration %ith iteration is %s" %(i, user_guessed_letter)

		if user_guessed_letter in guessed_word:
			index_of_correct_letter = guessed_word.index(user_guessed_letter)
			print "The position of the letter is", index_of_correct_letter
			string_of_my_correct_guess[index_of_correct_letter] = user_guessed_letter
			print string_of_my_correct_guess
			# if "".join(string_of_my_guess) == guessed_word:
			# 	print "Yayyyy! you won"
			#print True
		else:
			
			incorrect_letters.append(user_guessed_letter)
			print incorrect_letters

		if "".join(string_of_my_correct_guess) == guessed_word:
			print "Yayyy! you've won"


	print "Sorry, no more guesses, you have reached the limit"



def main():
	# @TODO: pick a word and store it
	guessed_word = pick_random_word(word_list)
	print "Random word is: ", guessed_word

	length_of_guessed_word = len(guessed_word)
	print "length of secret word is: ",length_of_guessed_word

	check_user_input(guessed_word)


	# print "Sorry, no more guesses, you have reached the limit"




								# # @TODO: get user's guess
								# user_guess = get_user_input()
								# print user_guess
								# # @TODO: check if guessed letter in word
								# check_user_input(guessed_word, user_guess)
								# # @TODO: if guessed letter in word update solution list

if __name__ == '__main__':
	main()
	


