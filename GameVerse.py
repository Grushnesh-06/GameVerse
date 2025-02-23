import random
        
def GameVerse():
    print("Welcome to Game Verse: Play Your Way!")
    print("Choose a game to play:")
    print("1. Guess the Number \n2. Rock Paper Scissors \n3. Hand Cricket \n4. Word Scramble \n5. exit")
    choice = input("Enter the number of the Game you want to Play: ").strip()
    if choice == "1":
        guess_game()
    elif choice == "2":
        RockPaperScissors()
    elif choice == "3":
        HandCricket()
    elif choice == "4":
        WordScramble()
    elif choice == "5":
        print("Exiting GameVerse. Have a Good Day!")
        exit()
    else:
        print("Invalid choice. Please select a valid game.")
        GameVerse()

def guess_game():
    number_to_guess = random.randint(1,100)
    guesses = []
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100:"))
        guesses.append(guess)
        attempts += 1

        if guess < number_to_guess :
            print("Guessed number is low")
        elif guess > number_to_guess:
            print("Guessed number is high")
        else:
            print(f"That's a right guess! The number was {number_to_guess}.")
            print(f"You guessed in {attempts} attempts")
            print(f"Your guesses: {guesses}")
            reply = input("1. Play Again \n2. Main Menu:\n").strip().capitalize()
            if reply == "1" or reply == "Play Again":
                guess_game()
            elif reply == "2" or reply == "Main Menu":
                GameVerse()
            else:
                print("Invalid input, returning to Main Menu!")
                GameVerse()
            break
        
def RockPaperScissors():
    list1 = ["Rock", "Paper", "Scissors"]
    attempts = 1
    points = 0
    mypoints = 0
    while attempts <= 5: 
        ch = random.choice(list1)
        mych = input("Rock, Paper or Scissors?:").strip().capitalize()
        
        if ch == mych:
            print("It's a tie")
            continue
        elif (ch == "Rock" and mych == "Paper") or (ch == "Paper" and mych == "Scissors") or (ch == "Scissors" and mych == "Rock"):
            print("You won!")
            mypoints += 1
            print(f"Your Points:{mypoints} \nComputer Points:{points}")
            attempts += 1
        elif (ch == "Paper" and mych == "Rock") or (ch == "Scissors" and mych == "Paper") or (ch == "Rock" and mych == "Scissors"):
            print("Computer won!")
            points += 1
            print(f"Your Points:{mypoints} \nComputer Points:{points}")
            attempts += 1
        else:
            print("Follow the Rules!\nEnter Rock, Paper or Scissors")

    if points > mypoints:
        print("Computer won after 5 rounds")
    else:
        print("You won after 5 rounds")
    reply = input("1. Play Again \n2. Main Menu:\n").strip().capitalize()
    if reply == "1" or reply == "Play Again":
        RockPaperScissors()
    elif reply == "2" or reply == "Main Menu":
        GameVerse()
    else:
        print("Invalid input, returning to Main Menu!")
        GameVerse()

score = 0
myscore = 0
def HandCricket():
    global score, myscore
    list1 = ["Heads", "Tails"]
    list2 = ["Bat", "Bowl"]
    t = random.choice(list1)
    toss = input("Heads or Tails?:").strip().capitalize()
    if t == toss:
        print("You won the toss")
        ch = input("Bat or Bowl?:").strip().capitalize()
        if ch == "Bat":
            print("You chose to Bat first")
            BatFirst()
        
        else:
            print("You chose to Bowl first")
            BowlFirst()
        reply = input("1. Play Again \n2. Main Menu:\n").strip().capitalize()
        if reply == "1" or reply == "Play Again":
            score = 0
            myscore = 0
            HandCricket()
        elif reply == "2" or reply == "Main Menu":
            GameVerse()
        else:
            print("Invalid input, returning to Main Menu!")
            GameVerse()
            
    else:
        print("You lost the toss!")
        ch = random.choice(list2)
        if ch == "Bat":
            print("Computer chose to Bat first")
            BowlFirst()
        else:
            print("Computer chose to Bowl first")
            BatFirst()
        reply = input("1. Play Again \n2. Main Menu:\n").strip().capitalize()
        if reply == "1" or reply == "Play Again":
            score = 0
            myscore = 0
            HandCricket()
        elif reply == "2" or reply == "Main Menu":
            GameVerse()
        else:
            print("Invalid input, returning to Main Menu!")
            GameVerse()

def BatFirst():
    global score, myscore
    while True:
        a = random.randint(0,6)
        b = int(input("Enter from 0 to 6:"))
        print(f"Computer:{a}")
        if a == b:
            print("You are out!")
            print(f"Your score is: {myscore}.")
            print(f"Target is: {myscore+1}")
            break
        elif b == 0:
            myscore += a
            print(f"Score:{myscore}")
        else:
            myscore += b
            print(f"Score:{myscore}")

    while True:
        a = random.randint(0,6)
        b = int(input("Enter from 0 to 6:"))
        print(f"Computer:{a}")
        if a == b:
            print("Computer is out!")
            print(f"Computer score is: {score}.")
            if score < myscore:
                wonby = myscore - score
                print(f"Congratulations! You won by {wonby} runs")
                break
            elif score == myscore:
                print("It's a draw")
                break
            else:
                print("Tough luck! Computer won!")
                break
        elif a == 0:
            score += b
            print(f"Score:{score}")
            if score > myscore:
                print("Tough luck! Computer won!")
                break
        else:
            score += a
            print(f"Score:{score}")
            if score > myscore:
                print("Tough luck! Computer won!")
                break
                
def BowlFirst():
    global score, myscore
    while True:
        a = random.randint(0,6)
        b = int(input("Enter from 0 to 6:"))
        print(f"Computer:{a}")
        if a == b:
            print("Computer is out!")
            print(f"Computer score is: {score}.")
            print(f"Target is: {score+1}")
            break
        elif a == 0:
            score = score + b
            print(f"Score:{score}")
        else:
            score = score + a
            print(f"Score:{score}")
    while True:
        a = random.randint(0,6)
        b = int(input("Enter from 0 to 6:"))
        print(f"Computer:{a}")
        if a == b:
            print("You are out!")
            print(f"Your score is: {myscore}.")
            if score < myscore:
                print(f"Congratulations! You won.")
                break
            elif score == myscore:
                print("It's a draw")
                break
            else:
                wonby = score - myscore
                print(f"Tough luck! Computer won by {wonby} runs!")
            break
        elif b == 0:
            myscore += a
            print(f"Score:{myscore}")
            if score < myscore:
                print(f"Congratulations! You won.")
                break
        else:
            myscore += b
            print(f"Score:{myscore}")
            if score < myscore:
                print(f"Congratulations! You won.")
                break

def WordScramble():
    print("Welcome to Word Scramble!")
    print("Categories:")
    print("1. Colors \n2. Fruits \n3. Animals \n4. Vehicles \n5. Shapes \n6. Body Parts \n7.Days of the week \n8. Vegetables \n9. Common Foods \n10. Months")

    while True:
        choice = input("Select one category:").strip().title()
        if choice == "1" or choice == "Colors":
            Colors()
            break
        elif choice == "2" or choice == "Fruits":
            Fruits()
            break
        elif choice == "3" or choice == "Animals":
            Animals()
            break

        elif choice == "4" or choice == "Vehicles":
            Vehicles()
            break
        elif choice == "5" or choice == "Shapes":
            Shapes()
            break
        elif choice == "6" or choice == "Body Parts":
            BodyParts()
            break
        elif choice == "7" or choice == "Days Of The Week":
            Days()

            break
        elif choice == "8" or choice == "Vegetables":

            Vegetables()
            break
        elif choice == "9" or choice == "Common Foods":
            Foods()
            break
        elif choice == "10" or choice == "Months":
            Months()
            break
        else:
            print("Please select a valid category")
    

def Colors():
    colors = ["red", "blue", "green", "yellow", "pink", "orange", "purple", "black", "white", "brown"]
    rand = random.choice(colors)
    won(rand)
            
def Fruits():
    fruits = ["apple", "banana", "grape", "orange", "mango", "strawberry", "pineapple", "watermelon", "cherry", "pear"]
    rand = random.choice(fruits)
    won(rand)

def Animals():
    animals = ["dog", "cat", "elephant", "lion", "tiger", "rabbit", "giraffe", "monkey", "zebra", "bear"]
    rand = random.choice(animals)
    won(rand)

def Vehicles():
    vehicles = ["car", "bus", "bicycle", "motorcycle", "train", "truck", "airplane", "boat", "helicopter", "van"]
    rand = random.choice(vehicles)
    won(rand)

def Shapes():
    shapes = ["circle", "square", "triangle", "rectangle", "oval", "star", "hexagon", "pentagon", "diamond", "heart"]
    rand = random.choice(shapes)
    won(rand)

def BodyParts():
    body_parts = ["head", "hand", "leg", "eye", "ear", "nose", "mouth", "finger", "foot", "hair"]
    rand = random.choice(body_parts)
    won(rand)

def Days():
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    rand = random.choice(days_of_week)
    won(rand)

def Vegetables():
    vegetables = ["carrot", "potato", "tomato", "onion", "cucumber", "broccoli", "spinach", "cabbage", "pumpkin", "cauliflower"]
    rand = random.choice(vegetables)
    won(rand)

def Foods():
    foods = ["pizza", "burger", "rice", "bread", "pasta", "cheese", "chocolate", "ice cream", "egg", "fish"]
    rand = random.choice(foods)
    won(rand)

def Months():
    months = ["january", "february", "march", "april", "may", "june", 
          "july", "august", "september", "october", "november", "december"]
    rand = random.choice(months)
    won(rand)

def won(rand):
    rand_s = list(rand)
    random.shuffle(rand_s)
    s_word = "".join(rand_s)
    print(f"Scrambled word: {s_word}")
    count = 1
    while True:
        guess = input("Guess the correct word:").strip().lower()
        if rand == guess:
            a = rand.capitalize()
            print(f"Congratulations! You won.\nThe guess, {a} is correct!")
            print(f"You guessed in {count} attempts")
            reply = input("1. Play Again \n2. Main Menu:\n").strip().capitalize()
            if reply == "1" or reply == "Play Again":
                WordScramble()
            elif reply == "2" or reply == "Main Menu":
                GameVerse()
            else:
                print("Invalid input, returning to Main Menu!")
                GameVerse()
                break
        else:
            count += 1
            print("Wrong guess!\nTry again.")

GameVerse()