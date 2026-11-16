'''
Welcome interface
'''
import  string, time
print("Welcome to TypeMaster!\nYou will need your username to create or access your account.")
username = input("Enter your username (case-sensitive): ")
verifyUserAccount(username)
end = 1
while end == 1:
  print("\nYou can choose a difficulty level or go through a quick tutorial!\nEasy/Medium/Hard/Tutorial (e/m/h/t)")
  lvlchoice = input("Enter your choice: ")
  lvlchoice.strip().lower()
  if lvlchoice in "emh":
    print(chooseWordSet(lvlchoice))
    print("Hit ENTER when finished")
    start = time.perf_counter()
    userParagraph = input("Begin typing here: ")
    end = time.perf_counter()
    userTime = round(end-start)
    


