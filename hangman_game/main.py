from DIR.constant import *
import os
import random
import paiting as p
import json

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Dictionary conversion from letters with accents
def choose ():
    with open(DATA, "r", encoding = "utf-8") as f:
        options = [line.splitlines()[0] for line in f]
        final_word = options[random.randint(0,len(options) - 1 )]
        replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        )
        for a, b in replacements:
            final_word = final_word.replace(a, b).replace(a.upper(), b.upper())
        f.close()
        return final_word

#Validate that the options inserted by the users across the game are those allowed 
def validate(op):
    try:
        if op == 1:
            res = int(input("Choose an option: "))
            if res > 4 or res < 1:
                raise
        if op == 2:
            res = input("Do you want to continue?: Y/N: ")
            if res.upper() != "Y" and res.upper() != "N":
                print(res.upper() != "N")
                raise
        return res            
    except:
        input("Select a valid option.")

#Generate a view of scores from a JSON file.
def show_scores():
    clear()
    try:
        with open(LEADERBOARD, "r", encoding = "utf-8") as f:
            data = f.read()
            jsondata = json.loads(data)
        print("*********************************".center(50, "="))    
        print("LEADERBOARDS".center(50, "="))
        print("*********************************".center(50, "=")+"\n")
        for line in range(len(jsondata)):
            txt = f"{line + 1}. " + jsondata[line]["name"]
            print(txt.ljust(20, "."), end=" ")
            print(jsondata[line]["score"])
        input("\n\nPress Enter to continue....")
        f.close()
    except:
        print("\n\nLeaderboards not fount, please play a game first")
        input("\nPress Enter to continue....")

#Create or edit a JSON file with the top 5 scores and sort them from highest to lowest
def save_score(score):
    name = "     "
    while len(name) > 4:
        name = input("Put your name (max 4 characters): ")
    try:
        with open(LEADERBOARD, "r", encoding = "utf-8") as f:
            data = f.read()
            jsondata = json.loads(data)
    except:
        jsondata = []
        pass
    with open(LEADERBOARD, "w", encoding = "utf-8") as f:
        jsondata.append({
            "name": name,
            "score": score
        })
        for i in range(len(jsondata)):
            for j in range(len(jsondata)):
                if int(jsondata[i]["score"]) > int(jsondata[j]["score"]):
                    aux = jsondata[j]
                    jsondata[j] = jsondata[i]
                    jsondata[i] = aux
        if len(jsondata) > 5:
            jsondata.pop(len(jsondata)-1)
        json.dump(jsondata, f, indent=4)
    f.close()

#This is the logic for survival mode, every 5 rounds your lives restore to ten, and you can choose if you finish the game or continue.
def survival():
    lifes = 10
    score = 0
    hit = 1
    end = False
    res = None
    round_number, count = 0,0
    while end == False:
        round_number +=1
        count +=1
        if count == 5:
            lifes = 10
            count = 0
            while res == None:
                res = validate(2)
                if res == "N":
                    break       
        lifes, score, hit, end = play(lifes,2,score, round_number, hit)
    save_score(score)
    return

# Function play that contains the logic of game.
def play(lifes, mode, score, round_number, hit):
    clear()
    word = choose().upper()
    word_list = [i for i in word]
    game = ["_" for i in word]
    end_try = game.copy()
    while lifes > 0:
        print("Guess the word".center(50, "="), end = " ")
        print("Tries: "+ str(lifes), end = " ")
        #Validate the game mode if it is normal or survival
        if mode == 2:
            if set(game) != set(end_try):
                score += 5 * hit
                hit += 1
            print("  SCORE: " + str(score), end = " ")
            print("  ROUND: "+ str((round_number)))
        #This breaks the while loop when you guess the word
        if set(word_list) == set(game):
            break
        end_try = game.copy()
        print("\n"+" ".join(game))
        p.paint(lifes)
        turn = input().upper()
        #If you write the full word, you win and get 50 points.
        if turn == word:
            score += 50
            break
        clear()
        game = [turn if word[x] == turn else game[x] for x in range(len(word))]
        #This block subtract your lives
        if set(game) == set(end_try):
            lifes -= 1
            hit = 1
        if lifes == 0:
            p.paint(lifes)
            print("The word was: " + " ".join(word))
            print("Game Over")
            input("Press Enter to continue....")
            return lifes, score, hit, True
    clear()
    print("\n"+" ".join(word))
    print("\nYou Win")
    input("\nPress Enter to continue....")
    return lifes, score, hit, False

#In this function, there is a single menu with 4 options
def run():
    option = 0
    while option != 4:    
        clear()
        print("WElCOME TO HANGMAN GAME".center(50, "="))
        print("\n\n1. New Game.\n")
        print("2. Survival.\n")
        print("3. Survival Leaderboards.\n")
        print("4. Exit.\n")
        option = validate(1)
        if option == 1:
            play(10,1,1,1,1)
        if option == 2:
            survival()
        if option == 3:
            show_scores()    
        if option == 4:
            clear()
            return "Thanks for playing"

if __name__ == "__main__":
    print(run())