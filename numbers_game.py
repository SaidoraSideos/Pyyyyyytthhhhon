import random
tries = 0
choice = int(input("Wanna play a guessing game? Guess a number from 1 to 100 and see if it matches the computer! "))
num = random.randint(1, 100)
while 0 < choice <= 100:
    try:
         tries = tries + 1
         if choice == num:
          print(f"You guessed right! The number was {choice}")
          print(f"It took you {tries} tries")
          choice = 0
         elif (0 > choice) or (choice > 100):
          print(f"{choice} Is not a number from 1 to a 100.")
         elif choice != num:
              if (choice - num >= 30):
                   print("Too high")
              elif (num - choice >= 30):
                  print("Too low")
         print(f"You have tried {tries} times! FAILURE!")
         choice = int(input("Try again Loser. "))
    except ValueError:
       print("THIS ISN'T EVEN A NUMBER TO BEGIN WITH.")   

    
        