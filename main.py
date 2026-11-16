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
    userTime = round(end-start)/60
    wpm = calcWPM(lvlchoice, textNum, userTime)
    accuracy = calcAccuracy(lvlchoice, textNum, calcCharsMissed(lvlchoice, textNum, userParagraph)
    print("\nWPM: "+str(wpm))
    print("Accuracy: "+str(accuracy))
    #calc improvement functions
    displayUserStats(username, lvlchoice, textNum)
    saveUserStats(username, lvlchoice, textNum, wpm, accuracy)
    print("Frequently missed character: "+FreqMissedChar(userParagraph))
    '''
                            ask user for next choice etc.
    '''
  elif lvlchoice == "t":
    print("\nHere is a quick tutorial!")
    print("        HOME ROW FINGER PLACEMENT GUIDE")
    print("Left Hand:   Pinky [A] | Ring [S] | Middle [D] | Index [F]")
    print("Right Hand:  Index [J] | Middle [K] | Ring [L] | Pinky [;]")
    print("Thumbs:      Rest lightly on the [SPACEBAR]")
    print("\nTip: Feel for the small bumps on the F and J keys!")
    input("\nPress Enter when your fingers are in position...")
    continue
  else:
    print("Invalid input.")
    endchoice = input("Press [1] to continue and [0] to quit: ")
    if endchoice == 1:
      continue
    else:
      end = 0

