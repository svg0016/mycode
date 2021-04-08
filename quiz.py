def introduction():
    print("Do you want to play a game.....?")
    print("WEll if not that's too bad.")
    print("We will now begin the selection quiz. You will be asked random questions to test you brain /n If you "
          "fail, then  the world will eventually be taken over by apes because obviously humanity has done something"
          " wrong")


def first_questions():
    print("=======================================================================")

    name = input("What is your name?  :")
    answer2 = int(input("How many States are there in the United States  :"))

    if answer2 == 50:
        print("Good Job " + name + ", You got the first part right. Now it is about to get tricky")
    else:
        print("We are all doomed. This laptop wil self destruct in  3")
        print("2")
        print("1")
        exit()


def second_questions():
    # Questions
    answer3 = input("Who created the programing language python.Answer should be the full name.(ex. fist last): ")
    answer4 = int(input("How many layers are there of the OSI Model: "))
    answer5 = input("What is better Xbox or PlayStation: ")
    counter = 0
    playstation = True

    # if else logic for answers
    if answer3.lower() == "guido van rossum":
        counter += 1
    else:
        counter = 0
    if answer4 == 7:
        counter += 1
    else:
        counter += 0
    if answer5.lower() == "playstation":
        counter += 1
        playstation = True
    else:
        counter += 0
    # logic for results to answers
    if counter == 3:
        print("Congratulations!! You did not fail.Humanity is Saved. Most importantly, You Chose playstation the "
              "superior gaming system ")
    elif counter == 2 and playstation:
        print("You were close but still failed. That's unfortunate. Luckily you chose PlayStation so there is still "
              "hope for humanity  ")
    elif counter == 2 and not playstation:
        print(" You were close but failed. Humanity is Doomed because you like Xbox. Good Job.")
    elif counter == 1 and playstation:
        print ("Man, you really have some work to do. You got the first two questions wrong but you like Playstation."
               "So I need you to do better next time!")
    elif counter == 1 and not playstation:
        print("You Failed very badly. Humanity is doomed and the Apes are coming. You should really watch Planet of "
              "The Apes so you can know what to do.")
    else:
        print("You got every question wrong! Humanity is doomed and the apes are coming. You should really watch "
              "Planet of The Apes so you can know what to do. Also you suck because you like Xbox.")


# calling functions
introduction()
first_questions()
second_questions()
