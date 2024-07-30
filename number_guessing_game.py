import random as r

welcome_messages = [
    "Welcome to the Number Guessing Challenge! Are you ready to test your luck?",
    "Get ready to flex your mental muscles in our Number Guessing Game!",
    "Welcome, number sleuth! Can you crack the code in our guessing game?",
    "Prepare for a numerical adventure in our Guess the Number game!",
    "Hello, brave guesser! Think you can find our secret number?",
    "Welcome to Number Nebula! Navigate through digits to find the hidden target.",
    "Greetings, number ninja! Your quest to find the secret digit begins now.",
    "Step right up to the Digit Dojo! Sharpen your guessing skills here.",
    "Welcome to the Number Hunt! Can you track down our elusive target?",
    "Enter the Realm of Random Numbers! Your journey to find the hidden value starts here."
]

range_messages = [
    "First, let's set the boundaries of our numerical playground.",
    "Time to choose your numerical arena!",
    "How wide do you want your guessing field to be?",
    "Let's define the scope of your number-hunting grounds."
]


mode_messages = [
    "Now, let's determine how challenging you want this quest to be.",
    "Time to choose your difficulty level, brave number warrior!",
    "How daring do you feel today? Let's pick a challenge level.",
    "The path of a number guesser has many difficulties. Which one will you choose?"
]

game_start_messages = [
    "The hunt begins! May the odds be ever in your favor.",
    "Your numerical adventure starts now. Good luck!",
    "The secret number is set. Can you uncover it?",
    "Let the guessing games commence! Trust your instincts."
]

correct_guess_messages = [
    "Eureka! You've cracked the code!",
    "Brilliant deduction! You've found the secret number!",
    "Victory! Your numerical prowess is unmatched!",
    "Amazing! You've successfully tracked down the elusive number!"
]

game_over_messages = [
    "And that's a wrap! Thanks for playing the Number Guessing Game!",
    "Game over! We hope you enjoyed this numerical adventure!",
    "The curtain falls on another thrilling number hunt. Until next time!",
    "That concludes our digit-chasing escapade. Come back soon for more!"
]



attempts,rng=0,0
ranges={1:10,2:50,3:100}
modes={1:["Easy",10],2:["Medium",5],3:["Hard",3]}

print(r.choice(welcome_messages))
print()
print("\n",r.choice(range_messages))
print("1.1-10")
print("2.1-50")
print("3.1-100")
c=int(input("Your Range:"))

if c in ranges:
  rng=ranges[c]

print("\n",r.choice(mode_messages))
print("1.Easy")
print("2.Medium")
print("3.Hard")
m=int(input("Your Mode:"))

if m in modes:
  mode,max_attempts=modes[m]

target=r.randint(1,rng)
print("\n",r.choice(game_start_messages))
print(f"\nYou've chosen {mode} mode. You have {max_attempts} attempts to guess a number between 1 and {rng}.")

while attempts<max_attempts:
  userInput=int(input("Guess the target:"))
  attempts=attempts+1

  if target==userInput:
    print(r.choice(correct_guess_messages))
    break
  elif target>userInput:
    print("Your no. was too small, Take a bigger guess....")
  elif target<userInput:
    print("Your no. was too big, Take a lower guess....")
  print(f"Attempts left: {max_attempts - attempts}")


if target!=userInput and attempts==max_attempts:
  print(f"\nSorry, you've run out of attempts. The target was {target}.")
else:
  print(f"You take {attempts} Guess to reach the correct target")

print(r.choice(game_over_messages))
