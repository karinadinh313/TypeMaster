'''
Welcome interface
'''
import  string, time
print("Welcome to TypeMaster!\nYou will need your username to create or access your account.")
username = input("Enter your username (case-sensitive): ")
verifyUserAccount(username)
end = 1
while end == 1:
  '''
  main dashboard
  '''
  print("\nYou can choose a difficulty level or go through a quick tutorial!\nEasy [1]/Medium [2]/Hard [3]/Tutorial [4]")
  lvlchoice = input("Enter your choice: ")
  lvlchoice.strip()
  if lvlchoice in "123":
    print(chooseWordSet(lvlchoice))
    print("Hit ENTER when finished")
    start = time.perf_counter()
    userParagraph = input("Begin typing here: ")
    end = time.perf_counter()
    userTime = round(end-start)/60
    '''
    need to handle invalid inputs here
    '''
    wpm = calcWPM(lvlchoice, textNum, userTime)
    accuracy = calcAccuracy(lvlchoice, textNum, calcCharsMissed(lvlchoice, textNum, userParagraph))
    print("\nWPM: "+str(wpm))
    print("Accuracy: "+str(accuracy))
    '''
    calc improvement functions
    '''
    displayUserStats(username, lvlchoice, textNum)
    saveUserStats(username, lvlchoice, textNum, wpm, accuracy)
    freqmissed = FreqMissedChar(userParagraph)
    print("Frequently Missed Character: "+freqmissed)
    print("\nWhat would you like to do next?\nNew Word Set [1]/Practice Frequently Missed Character [2]/Quit [3]")
    newchoice = input("Enter your choice: ")
    newchoice.strip()
    if newchoice == "1":
      continue
    elif newchoice == "2":
      #freq missed char
      print(chooseWordSet(freqmissed))
      print("Hit ENTER when finished")
      start = time.perf_counter()
      userParagraph = input("Begin typing here: ")
      end = time.perf_counter()
      userTime = round(end-start)/60
    '''
    need to handle invalid inputs here
    '''
     '''
     are we gonna caculate wpm and accuracy here too?
     '''
      print("\nWhat would you like to do next?\nNew Word Set [1]/Quit [2]")
      newchoice = input("Enter your choice: ")
      newchoice.strip()
      if newchoice == "1":
        continue
      elif newchoice == "2":
        end = 0
      else:
        print("Invalid input.")
        endchoice = input("Press [1] to continue and [0] to quit: ")
        if endchoice == "1":
          continue
        else:
          end = 0
    elif newchoice == "3":
      end = 0
    else:
      print("Invalid input.")
      endchoice = input("Press [1] to continue and [0] to quit: ")
      if endchoice == "1":
        continue
      else:
        end = 0
  elif lvlchoice == "4":
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
    if endchoice == "1":
      continue
    else:
      end = 0

