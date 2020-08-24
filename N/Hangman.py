#Words classified by difficulty
easy=["time","person","thing","world","child","point","Bottle","Table","Chair","Ball","Rabbit","Elephant","Chicken","Horse","bunch","apple","Orange"]
medium=["pearls","Star","galaxy","Diary","Jumble","Umbrella","Dolphin","Jelly","Ocean","Guitar","Mirror","Jeans","silk","Chocolate","bouquet","grape"]
hard=["Awkward","Guitar","Piano","Coffin","Crypt","Fishhook","Fjord","Ivory","Oxygen","Pixel","Rhythmic","Yacht","Zigzag"]
#Starting the game
import random
print("Let's play Hangman!")
while True:
    #Choosing difficulty
    while True:
        diff=int(input("Choose difficulty:\n1-Easy\n2-Medium\n3-Hard\n"))
        length=0
        if diff==1:
            diff=easy
            length=len(easy)
            break
        elif diff==2:
            diff=medium
            length=len(medium)
            break
        elif diff==3:
            diff=hard
            length=len(hard)
            break
        else:
            print("Incorrect Input")
    #Choosing the word
    rand_int=random.randint(0,length-1)
    word=diff[rand_int].upper()
    length=len(word)
    #Space
    space=[]
    for a in range(0,length):
        space+="_"
    print(*space)
    #In play
    wrong_guess=6
    guesses=0
    print("Enter one letter per guess!")
    while wrong_guess>0 and guesses<=length-1:
        guess=input("Enter guess\n").upper()
        if guess in word:
            for a in range(0,length):
                if guess==word[a]:
                    space[a]=guess
                    guesses+=1
        elif guess not in word:
            wrong_guess-=1
        print(*space,"\t","Wrong guesses left:",wrong_guess)
    if wrong_guess>=1 and guesses==length:
        print("You won!")
    elif wrong_guess==0:
        print("You lost! The word was",word)
    retry=input("Play Again?(Y/N)\n").upper()
    if retry=="N":
        break
