import random
tries = 0

num = random.randint(1, 100)
main
choice = 0
while 0 <= choice <= 100:

choice = int(input("Wanna play a guessing game? Guess a number from 1 to 100 and see if it matches the computer! "))
while 0 < choice <= 100:
main
    try:
         tries = tries + 1
         if choice == num:
          print(f"You guessed right! The number was {choice}")
          print(f"It took you {tries} tries")
          tries = 0
          break
         elif (0 > choice) or (choice > 100):
          print(f"{choice} Is not a number from 1 to a 100.")
         elif choice != num:
              if (choice - num >= 30):
                   print("Too high")
              elif (num - choice >= 30):
                  print("Too low")
         print(f"You have tried {tries} times! FAILURE!")
    except ValueError:
       print("THIS ISN'T EVEN A NUMBER TO BEGIN WITH.")   

    
        