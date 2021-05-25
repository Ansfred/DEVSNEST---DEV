from questions import QUESTIONS
import sys


print("Welcome to KAUN BANEGA CROREPATI \n")
print("AT ANY POINT IN THE GAME, TO QUIT, ENTER 'quit' \n")
print("TO USE 50-50 LIFELINE, ENTER 'lifeline' \n")


def isAnswerCorrect(question, answer):
    return True if answer == QUESTIONS[question]["answer"] else False


def lifeLine(queIndex):
    MAP = ["option1", "option2", "option3", "option4"]
    i, j = 1, 0
    while i < 4:
        if QUESTIONS[queIndex]["answer"] != i:
            QUESTIONS[queIndex][MAP[i-1]] = None
            j += 1
            if j == 2:
                return
        i += 1


def kbc():
    round_no = 0
    prize_money = 0
    lifeline = 1
    
    while round_no < 15:
        print(f'Question {round_no + 1} : {QUESTIONS[round_no]["name"]} \n')
        print('Your options are:')
        print(f'\t\t Option 1: {QUESTIONS[round_no]["option1"]}')
        print(f'\t\t Option 2: {QUESTIONS[round_no]["option2"]}')
        print(f'\t\t Option 3: {QUESTIONS[round_no]["option3"]}')
        print(f'\t\t Option 4: {QUESTIONS[round_no]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        
        if ans != "lifeline" and ans != "quit":
            ans = int(ans)

        if ans == "lifeline" and round_no + 1 != 15:
            lifeline -= 1
            lifeLine(round_no)
            
            print(f'Question {round_no + 1} : {QUESTIONS[round_no]["name"]} \n')
            print('Your options are:')
            print(f'\t\t Option 1: {QUESTIONS[round_no]["option1"]}')
            print(f'\t\t Option 2: {QUESTIONS[round_no]["option2"]}')
            print(f'\t\t Option 3: {QUESTIONS[round_no]["option3"]}')
            print(f'\t\t Option 4: {QUESTIONS[round_no]["option4"]}')
            ans = input('Your choice ( 1-4 ) : ')
            
            if (ans != "quit"):
                ans = int(ans)
                
        if ans == "quit" or ans == "Quit" or ans == "QUIT":
            print("Well Played !")
            print(f'TOTAL MONEY WON = {prize_money}')
            sys.exit(0)
            
        # check for the input validations
        else:
            if isAnswerCorrect(round_no, int(ans)):
                # print the total money won.
                # See if the user has crossed a level, print that if yes

                prize_money = QUESTIONS[round_no]["money"]
                
                
                print('\nCorrect !')
                print(f'MONEY WON = {prize_money}')
                print("LIFELINE LEFT = ", lifeline)
                print("\n")
                
                if prize_money == 10000:
                    print("Congratulations, you've just crossed LEVEL 1. \n")
                if prize_money == 320000:
                    print("Congratulations, you've just crossed LEVEL 2. \n")
                
            else:
                # end the game now.
                # also print the correct answer
                print('\nIncorrect !')
                print(f'Correct Answer : Option {QUESTIONS[round_no]["answer"]}')
                
                if round_no + 1 <= 5:
                    prize_money = 0
                elif round_no + 1 > 5 and round_no + 1 <= 10:
                    prize_money = 10000
                else:
                    prize_money = 320000
                print(f'TOTAL MONEY WON = {prize_money}')
                return
        round_no += 1


kbc()