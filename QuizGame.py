#For this game we will use 4 functions
#To make it all readable it will be seperated with comments

#----------------------------------------------
def new_game():
#now inside this function we declare a few things
    guesses = []            #We declare a empty list called guesses
    correct_guesses = 0     #A variable equal to 0 since we havent guessed anything yet
    questions_num = 1       #And a question number set to 1 since we start at the first question

#Now to actually display something in the game, we will use a for loop to display the key(questions) in order.
    for key in questions:                   #For each key in the questions dictionary
        print("--------------")             #Just a line to seperate the questions.
        print(key)                          #print all questions
        for i in options[questions_num-1]:  #For each itteration in the options collection,
                                            # depending on the index number of which question were on, -1 because computers count from 0.
            print(i)                        #print the itteration of the options list
        guess = input("Enter(A,B,C, or D):")#Prompt the user to input an answer, A,B,C, or D.
        guess = guess.upper()               #Correct any  lowercase letters to uppercase
        guesses.append(guess)               #Append the empty guesses list, with the users input

        correct_guesses += check_answer(questions.get(key),guess)  #Execute check_answer function with the key from the questions list,
        #Add correct_guesses variable += check answer, so the return value of check_answer is added to correct_guesses.
                                                # and the users guess as arguments.
        questions_num += 1                      #After each itteration, increment questions_num by 1
    #To display the score we will place the variables in the outer for loop, so that it executes after all questions have been answered.
    display_score(correct_guesses, guesses)     #We call the display_score function with the correct_guesses variable, and guesses list as arguments.
#----------------------------------------------
#Now to define a function that compares the users input with the answer value in the key value dictionary.
def check_answer(answer, guess):    #define function named check_answer with parameters answer and guess.
    if answer == guess:             #If the answer value from the key value is equals to the user input guess
        print("CORRECT!")           #print correct
        return 1                    #And return a value of 1
    else:                           #if this does not happen
        print("WRONG!")             #print wrong
        return 0                    #and return a value of 0
#----------------------------------------------
def display_score(correct_guesses, guesses): #Define function named display_score with 2 arguments. Variable correct_guesses and list guesses
    print("-----------------")               #print a line
    print("RESULTS")                         #print RESULTS
    print("-----------------")               #print a line
    print("Correct Answers: ", end="")               #print ANSWERS, with end because we dont want to end on a new line.
    for i in questions:                      #display all values in the questions dictionary with a for loop.
        print(questions.get(i), end=" ")      #print each itereration(i) in questions dictionary and dont end in a new line with end=" "<- 1 space to seperate iterations
    print()                                  #print an empty line

    #Same thing, but for guesses
    print("Your Guesses: ", end="")               #print Guesses, with end because we dont want to end on a new line.
    for i in guesses:                        #display all values in the guesses library with a for loop.
        print(i, end=" ")                     #print each itereration(i) and dont end in a new line with end=" " <- 1 space to seperate iterations
    print()                                  #print an empty line

    #To calculate the final score we will define a new variable
    score = int(correct_guesses/len(questions)*100) #Define variable named score that is a integer value of correct_guesses value divided by the length(number of key values) in questions*100
    print("Your score is "+str(score)+"%")          #Print the final score
#----------------------------------------------
#To allow the player the choice to play again, we define a last function called play_again
def play_again():                                             #Define new feunction called play_again
    response = input("Do you want to play again?(yes/no):")   #Ask for the players input
    response = response.upper()                               #Make the player input uppercase
    if response == "YES":                                     #if the response is YES
        return True                                           #then play_again is true
    else:                                                     #otherwise
        return False                                          #play again is false
#----------------------------------------------

#We will also need some variables to refer to that contains the data used in the game.
#In order to line up various questions and pair them with an appropriate answer, a dictionary is useful
#as it pairs up a key, with value

#each key is the question, with the correct answer being its value.
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Which shape is the Earth?: ": "D"
}

#The game will require the player to choose one of four options for each question, which be used in 2d list collections
#A tuple could work too I guess
#Each list is in order of the question it corresponds to
options = [["A. Guido van Rossum", "B. Elon Must", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989","B. 1991","C.2000","D. 2077"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. A cube", "B. A Cone", "C. A flat circle", "D. A sphere"]]

new_game() #After ALL OF THIS, start a new game.

while play_again(): #To allow the choice to end the game, create a loop depending on the choice made in play_again
    new_game()      #If the choice in play_again() is True, execute new_game() and start over

print("Bye!")       #If the choice in play_again() is False, print bye and break.