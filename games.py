import random
import cards

def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response


def ask_number(question,low,high):
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low,high):
                break
            else:
                response = input(question)
        else:
            print("you must enter a number")


def switch_turn(num_players,turn):
    while True:
        turn + 1
        if turn == 4:
            turn = 1
            break
    return turn

def roll(self):
        die1 = random.randint(1, 6)
        print("you rolled a",die1)
        roll = die1
        return roll

def welcome(title):
    print("\t\tWelcome to the game\n")
    print("\t\t",title,"\n")


class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = cards.Hand()
        return rep
    
    def __str__(self):
        rep = self.name
        rep = rep +" "+str(self.hand.cards[0])
        return rep









if __name__=="__main__":
    print("You ran this module directly and did not import it")
    input("\n\npress enter key to exit")
    
















    
