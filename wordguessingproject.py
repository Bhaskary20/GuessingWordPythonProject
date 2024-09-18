import random

def word_guessing_game():
    words = ['apple', 'banana', 'dragon', 'orange', 'guava']
    word=random.choice(words)
    guesses_letters=[]
    attempts=4
    guessed_word=['_'] * len(word)
    name=input("What's yo name? ")
    print(f"Welcome {name} to this game")

    while attempts>0:
        print("\nAttempts left: ", attempts)
        print("Current word: ", '_'.join(guessed_word))
        guess=input("Enter your guess: ").lower()

        if not guess.isalpha() or len(guess)!=1:
            print("Enter a valid letter")
            continue
        if guess in guesses_letters:
            print("You have already guessed it")
            continue
        
        guesses_letters.append(guess)

        if guess in word:
            print("Good job!It's on word")
            for i in range(len(word)):
                if word[i]==guess:
                    guessed_word[i]=guess
        else:
            print("Sorry the letter is not in the word")

            attempts-=1


        if '_' not in guessed_word:
            print("Congratulation!")
            break
    else:
            print("Better luck next time")

word_guessing_game()
                             
        



            
        


