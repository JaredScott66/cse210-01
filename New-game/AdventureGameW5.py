while True:
    print("Welcome to the text bases adventure game.\nGHOST SHIP\nLets begin!\n")

    print("You wake on an abandoned space craft. Everything is silent...\nYou see a distant blinking light in a darkened room to the left.\nThere is a door directly in front that says Engine Room.\nTo the right there is a cabinet with a loose lock.")

    print("You walk over to the cabinet. It reads on the door. Sr Mechanic John Tayler\nWith the lock being open you easily open it.\nInside you can see some clothes and assorted tools. Among them you find: A keycard, a pistol with a single bullet, and an engine manual. What do you take?")
    print()
    while True:
        print("\nKEYCARD\nGUN\nMANUAL")
        gun = False
        manual = False
        keycard = False
        cab_choice = input("")
    
        if cab_choice.upper() == "GUN":
            gun = True
            bullet_count = 1
            loop_cab = 1
        elif cab_choice.upper() == "KEYCARD":
            keycard = True
            loop_cab = 1
        elif cab_choice.upper() == "MANUAL":
            manual = True 
            loop_cab = 1
        else:
            print("You dont find that.")
            loop_cab = 0
        if loop_cab == 1:break
        
    print("After you pickup the " + str(cab_choice) + " you see the blinking light in front of you and the engine room door to your right.\nWhat do you do?")
    while True:
        print("LIGHT\nENGINE")
        start_choice = input("")
        if start_choice.upper() == "LIGHT":
            loop_1 = 1
            print("You enter a room that appears to be completely wrecked with a single tablet on a table that seems to have recorded something.\nYou hit play on the recording. What you hear is a chaotic mess of alarms and screaming and you hear someone yell “Abandon Ship! They have killed the bridge crew! And we could be next!”. Then, in that moment you hear something fall to the floor with a loud crash outside the door.")
            print("There is a cabinet in one corner of the room that hangs open that you may fit in. You also see stairs that lead up to another floor to a closed door\nWhat do you do?")
       
            while True:
            
                print("HIDE\nRUN")
                if gun == True:
                    print("FIGHT")
                choice_light = input("")
                print()
                if choice_light.upper() == "HIDE":
                    loop_light = 1
                    print("You rush to the cabinet and close the door.\nThrough the slit in the door, you see what seems to be a man in a space suit slowly walk in.\nBut something about him unnerves you. He walks unnaturally, and makes no sound other than his foots steps.")
                    print("He walks in, grasping the air as if he is trying to grap hold of someone.\nYou remain silent as he walks silently around the room and walks back the way he came in.")
                    print("After the figure leaves, you step out of the cabinet. There is the door which the figure just left through. Or there is the door up the stairs\nWhat do you do?")
        
                    while True:
                        choice_after_hide = input("STAIRS\nDOOR")

                        if choice_after_hide.upper() == "STAIRS":
                            print("You go up the stairs and reach the door. The door opens to reveal the damaged bridge of the starship.\nThere are old bloodstains on the walls and floor but no bodies remain. You go to the helm and see the engines are offline and must be restarted before travel is possible.")
                            print("You look and spot a communications console. You try to send a distress call but it is locked and requires a keycard to access.")
                            if keycard == True:
                                print("You pull out the keycard you found in that locker and insert it into the console and it starts up!\nYou activate the automated distress beacon. Will a rescue team make it in time?")
                                print("End of current build")
                                break
                            if keycard == False:
                                print("As you try and figure out your next move. You hear heavy footfalls coming up the stairs. What new danger awaits?")
                                print("End of build")
                                break
                        elif choice_after_hide.upper() == "DOOR":
                            print("You slowly peak around the corner of the door into the hallways to see the figure is no longer in sight.\nYou step into the hallway. And then, all of the sudden the ship jerks to the side! something has happened.\n\nBut what?")
                            print("End of build")
                            break
                        else:
                            print("That may not be a good idea")

                elif choice_light.upper() == "RUN":
                    print()
                    loop_light = 1
                    print("You decide you dont want to know what made that noise and run up the stairs.\nAs you run up the stairs, you can hear rapidly approaching, heavy footsteps close behind.")
                    print("You run through the door and turn around to close it behind you. As you do so, you catch a glimps of a large figure inside a space suit running up the stairs.\nYou close the door and seal it. From behind the door you can hear the suited figure approach the door and start to lightly tap the door steadly.")
                    print("You back away from the door. Hoping you can find a way off this cursed ship.")
                    print("End of build")
                    break

                elif choice_light.upper() == "FIGHT":
                    print()
                    loop_light = 1
                    print("With the gun you picked up in the locker you turn to face the door and take aim. What you see is a figure in a space suit who after seeing you, immediately reaches out to grab you.")
                    print("You point and fire the gun in into the helmet of the figure.\nWhat you see in the helmet is a human skeleton shrouded in darkness. \nThe bullet shattered the skull of this skeleton and it fell to the floor.\nLifeless")
                    print("What is happining!? What happens next!?")
                    print("End of build")
                    break
                else:
                    print("There is no time for that!")
                    loop_light = 0
                if loop_light == 1:break
                     

        elif start_choice.upper() == "ENGINE":
            print()
            loop_1 = 1
            print("You go through the engine room door and see a dimly lit space out of which you can make out a lot of machines and a vast assortment of panels and system readouts.")
            print("Everything is quiet, the engines do not appear to be running and you see a terminal that seems to be blinking in red.\nThere is an upper catwalk that goes up to another floor and you think you can hear a light tapping coming from there.\nWhat do you do?")
            while True:
                choice_engine = input("TERMINAL\nNOISE\n")
                if choice_engine.upper() == "TERMINAL":
                    loop_engine = 1
                    print()
                    print("You walk over to the blinking console and see a lot of dials and reports on the engine. Its appears that there was an overload and the engine requres a manual restart.")
                    if manual == True:
                        print("With the manual you found you are able to walk through the process of starting the engine. You trun the right dials and flip the reset switch and then the engine roars to life!")
                        print("You start to hear all the machines powering up and the lights start to turn on\nYou hear something behind you. You turn around and see standing behind you a figure inside a space suit just starting reach out to grab you!")
                        print("Can you escape? What does this man want?\n")
                        print("End of build")
                        break
                    else:
                        print("Without any way of knowing how to fix the engine you go to walk away and hear something moving somewhere in the engine room.\nWhat is it? Friend or foe?\nWhat should you do?")
                        while True:
                            choice_engine_terminal = input("HIDE\nCALLOUT")
                            if choice_engine_terminal.upper() == "HIDE":
                                loop_engine_terminal = 1
                                print("You think its better to play it safe and go behind the engine console.\nAs you peek around the corner to look into the dark room. You can hear heavy foot steps begin to approach.")
                                print("As the foot steps get closer. You begine to make out the silhouette of a man in a space suit.\nThey make no noise other than their footsteps on the floor. You feel uneasy. Something seems wrong about this figure.")
                                print("What is it? should I call out? Or should I avoid it?")
                                print("End of build")
                                break

                            elif choice_engine_terminal.upper() == "CALLOUT":
                                loop_engine_terminal = 1
                                print("You call out saying 'Hello?' After calling out, you hear footsteps rapidly approach and you see turning a corner a figure inside a space suit running at you reaching out as if to grab you!")
                                print("What are you going to do! Why are they attacking!? You need to defend yourself! Do you try and grab a weapon of some kind, or do you run?")
                                print("What do you do?")

                            else:
                                print("Maybe you should do something else")
                                loop_engine_terminal = 0
                        if loop_engine_terminal == 1:break
                elif choice_engine.upper() == "NOISE":
                    loop_engine = 1
                    print()
                    print("You start walking up the stairs. When you reach the top and look to where the noise is coming from.\nStanding in front of a door on the opposite side, with their back to you")
                    print("is a figure inside a space suit just repeatedly tapping on the door. You get a bad feeling from this figure.\nYou start to go back down the stairs. You take a step and there is a creak that comes from the step.")
                    print("The figure suddenly turns to face you and starts running towards you. Reaching out as if to grab you. Why are they attacking? What happens next?")
                    print("End of build")
                    break
                else:
                    print("Its too dim to do that.")
                    loop_engine = 0
            if loop_engine == 1:break
        else: 
            print("You cant get there")  
            loop_1 = 0
        if loop_1 == 1:break
    again = input("\nThanks for playing, would you like to play again?\n(Y/N)")
    if again.upper() == "Y":
        continue
    else: break

print("finish")