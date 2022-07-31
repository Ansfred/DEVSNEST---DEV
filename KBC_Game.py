from KBC_Questions import questions
import sys

print("Welcome to Kaun Banega Crorepati \n")
print("At any point in the game, to quit, enter 'quit' \n")
print("To use 50-50 lifeline, enter 'lifeline' \n")

def is_answer_correct(question, answer):
    """
    If the answer is equal to the answer in the dictionary, return True, otherwise return False
    
    :param question: The question number
    :param answer: The answer the user gave
    :return: True
    """

    return True if answer == questions[question]["answer"] else False

def use_lifeline(quetion_index):
    """
    It takes the index of the question as an argument and removes two incorrect options from the
    question
    
    :param queIndex: The index of the question in the questions list
    :return: None
    """
    
    MAP = ["option1", "option2", "option3", "option4"]
    i, j = 1, 0
    while i < 4:
        if questions[quetion_index]["answer"] != i:
            questions[quetion_index][MAP[i-1]] = None
            j += 1
            if j == 2:
                return
        i += 1


# Driver Function
def kbc():
    round_number = 0
    prize_money = 0
    lifeline = 1

    while round_number < 15:
        print(f'Question {round_number + 1} : {questions[round_number]["name"]} \n')
        print('Your options are:')
        print(f'\t\t Option 1: {questions[round_number]["option1"]}')
        print(f'\t\t Option 2: {questions[round_number]["option2"]}')
        print(f'\t\t Option 3: {questions[round_number]["option3"]}')
        print(f'\t\t Option 4: {questions[round_number]["option4"]}')
        answer = input('Your choice ( 1-4 ) : ')
        
        if answer != "lifeline" and answer != "quit":
            answer = int(answer)

        if answer == "lifeline" and round_number + 1 != 15:
            if lifeline > 0:
                lifeline -= 1
                use_lifeline(round_number)
                
                print(f'Question {round_number + 1} : {questions[round_number]["name"]} \n')
                print('Your options are:')
                print(f'\t\t Option 1: {questions[round_number]["option1"]}')
                print(f'\t\t Option 2: {questions[round_number]["option2"]}')
                print(f'\t\t Option 3: {questions[round_number]["option3"]}')
                print(f'\t\t Option 4: {questions[round_number]["option4"]}')
                answer = input('Your choice ( 1-4 ) : ')
            
                if (answer != "quit"):
                    answer = int(answer)
            else:
                print("Sorry, lifeline already used once :(")
                print(f'Total money won = {prize_money}')
                sys.exit(0)
                
        if answer == "quit":
            print("Well played !")
            print(f'Total money won = {prize_money}')
            sys.exit(0)
            
        # Check for input validations
        else:
            if is_answer_correct(round_number, int(answer)):
                # Print the total money won
                # Check if the user has crossed a level, if yes, print it

                prize_money = questions[round_number]["money"]
                
                
                print('\nCorrect !')
                print(f'Money won = {prize_money}')
                print("Lifeline left = ", lifeline)
                print("\n")
                
                if prize_money == 10000:
                    print("Congratulations, you've just crossed Level 1. \n")
                if prize_money == 320000:
                    print("Congratulations, you've just crossed Level 2. \n")
                
            else:
                # End the game now
                # Also print the correct answer
                print('\nIncorrect !')
                print(f'Correct Answer : Option {questions[round_number]["answer"]}')
                
                if round_number + 1 <= 5:
                    prize_money = 0
                elif round_number + 1 > 5 and round_number + 1 <= 10:
                    prize_money = 10000
                else:
                    prize_money = 320000

                print(f'Total money won = {prize_money}')
                return

        round_number += 1

kbc()