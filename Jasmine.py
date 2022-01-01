def adventure():
    '''
    note: The if-else statements at the beginning of every room is in regards to if you've been in there before or not.
    My hope was that by giving two sets of descriptions, it felt more alive as a game. 
    '''

    def strike(text): # this is for crossed off names in wake up room, needs work (doesn't convert well in console)
        result = ''
        for c in text:
            result = result + '\u0336'+  c 
        return result

    bag = []
    keyhole = []
    game_mechanics = []
    
    '''
    Below are the five rooms that are accessible within this game.
    They will all be defined with 4 interactive walls.
    '''


    def pos_neg1_0(): # Kitchen
        
        if "pos_neg1_0_mark" not in game_mechanics:
            print('''
                As you enter this room, the smell of jasmine is overwhelmed by a strong, savory aroma.
                You take a deep breath through your nose when you locate a huge pot of soup in the center of the room.
                Realizing you are starving, you grab the ladel.
                You scoop yourself some of the best tasting soup you've ever had.
                If whoever is keeping you is going to eat well, you figure you should too.
                Enough of that now; you're standing next to the island with a full belly. What do you do?
            ''')
            game_mechanics.append("pos_neg1_0_mark")
        else:
            print('''
                You return to the Kitchen. What do you do?
            ''')
        
        while 'jasmine_key' not in keyhole:
            action = input("Enter an action:")
            if action == 'n': # victory exit
                b = input('You see a keyhole that glows faintly white. Do you have a key? (y/n)')
                if b == 'y':
                    if 'jasmine_key' in bag:
                        keyhole.append('jasmine_key')
                    else:
                        print("You have no keys in your posession. Keep searching.")
                        exit
                elif b == 'n':
                    print("Ok sounds like maybe it's not quite time for you to be here. Go poke around the Southern rooms.")
                    exit
                else:
                    print('That makes no sense, so go stand back in the midde of the room and really think this time.')
                    exit
            elif action == 's':
                if "pos_neg1_neg1_mark" not in game_mechanics: # entering that room for the first time
                    print('''
                The South side of this room has a classic, wooden door. There is a rickety sign above: "Supply Room."
                You walk through the door wondering what supplies this building needs a whole room for.
                    ''')
                    pos_neg1_neg1()
                    break # this helps pop up back through stack on way out of loops
                else: # going back to Supply Room for the second+ time
                    print('''
                Back through the wooden door you go.
                    ''')
                    pos_neg1_neg1()
                    break
            elif action == 'e':
                print('''
                Back through the metal door you go.
                ''')
                pos_0_0()
                break
            elif action == 'w':
                if "secret seasoning" not in bag:
                    print('''
                Sitting on the shelf along the west wall are many seasonings.
                Presumably they are the ones that made that soup so delicious.
                However, one stands out as it is in a golden bottle marked "secret seasoning."
                You pocket it immediately as anything in gold seems vastly more important.
                    ''')
                    bag.append("secret seasoning")
                else:
                    print('''
                The shelf which once held the secret seasoning is a testament to your gluttony (and good taste).
                    ''')
            elif action == 'b':
                print(bag)
            elif action == 'p':
                print('You are 1 room west of your starting location.')
            elif action == 'q':
                print('Goodbye.')
                break
            else:
                print('That is an invalid action.')
    
    
    def pos_0_0(): # Wake Up Room
        
        if "pos_0_0_mark" not in game_mechanics:
            print('''
            You wake up in the center of a small, well lit room.
            It smells faintly like jasmine. Where are you? Who are you?
            Most importantly... how do you get out?
            Something is off about this situation even with soft lighting and flowery smells.
            Your head hurts worse than ever, and you don't even remember your name.
            How hard was that hit? You need to get out of this... house? Jail? You don't even know that.
            You pull out your compass. You are facing North. What do you do?

        CONTROLS ARE AS FOLLOWS:
            n IS INVESTIGATE WHAT IS ON THE NORTH WALL
            s IS INVESTIGATE WHAT IS ON THE SOUTH WALL
            e IS INVESTIGATE WHAT IS ON THE EAST WALL
            w IS INVESTIGATE WHAT IS ON THE WEST WALL
            b IS TO CHECK CONTENTS OF YOUR BAG
            p IS CURRENT POSITION IN REFERENCE FROM WAKE UP LOCATION
            q IS TO STOP PLAYING

        NOTE: YOU ARE ALWAYS STANDING IN THE CENTER OF THE ROOM
        ''')
            game_mechanics.append("pos_0_0_mark")
        else:
            print('''
                You return to the room you woke up in. What do you do?
            ''')
        
        while ('jasmine_key' not in keyhole) or ("quit" not in game_mechanics):
            action = input("Enter an action:")
            if action == 'n':
                if "driver's license" not in bag: # first time at north wall
                    print('''
                You look at the North wall and notice it is cobblestone. As you walk closer, you hear a small whirring.
                You suppose it is some sort of machine spinning, but can deduce nothing more.''')
                    bag.append("driver's license")
                    if "Kip" in game_mechanics: # saw list of names first on east wall
                        print('''
                In the corner of the North wall you see an end table. You pull a drawer open and find a driver's license.
                The name on it is... "Kip." The picture is yours. That was you on the list. Something is wrong here.
                        ''')
                    else: # discover name here first on license
                        print('''
                In the corner of the North wall you see an end table. You pull a drawer open and find a driver's license.
                The name on it is "Kip." The picture is yours, so at least you have your name now. You pocket the license.
                        ''')
                else: # second+ time at north wall, repeats
                    print('''
                You look at the cobblestone North wall. As you walk closer, you hear that small whirring again.
                    ''')
            elif action == 's':
                print('''
                As you approach a small crack in the South wall, you smell that jasmine again.
                You press your face against the cold cobblestone and the smell of jasmine is overwhelming.
                If you closed your eyes, you could be convinced you were not in a strange, unknown building.
                What is in that room? For now, you return to your search.
                ''')
            elif action == 'e':
                if "list" not in game_mechanics: # first visit to east wall
                    print('''
                There is a chalkboard with a list of names.
                The list is not labeled, but some are crossed off... why? You read the list:
                Avery''')
                    print("\t\t" + strike("Ruby"))
                    print("\t\tCharlie")
                    print("\t\t" + strike("John"))
                    print("\t\t" + strike("Rylie"))
                    print("\t\tScarlette")
                    print("\t\tKip")
                    if "driver's license" in bag:
                        print('''
                As you read the last name, you start to feel like your suspicion of this being a bad place is correct.
                You feel uneasy staying in this room any longer. You should go. Who put your name on this list?
                    ''')
                        game_mechanics.append("list")
                    else:
                        print('''
                You wonder why some are crossed off. Did something bad happen to them? 
                That last person, Kip, rings a bell.
                        ''')
                        game_mechanics.append("Kip")
                        game_mechanics.append("list")
                else: # second+ visit
                        print('''
                The chalkboard of names is still there. Nothing else of interest is here.
                        ''')
                        
            elif action == 'w':
                if "pos_neg1_0_mark" not in game_mechanics: # entering that room for the first time
                    print('''
                To the west of this room, you see a metal door. It is seemingly your only way out.
                You open the door and walk into the next room.
                    ''')
                    pos_neg1_0()
                    break # this helps pop up back through stack on way out of loops
                else: # going back to kitchen for the second+ time
                    print('''
                Back through the metal door you go.
                    ''')
                    pos_neg1_0()
                    break
            elif action == 'b':
                print(bag)
            elif action == 'p':
                print('You are where you woke up.')
            elif action == 'q':
                print('Goodbye.')
                break
            else:
                print('That is an invalid action.')

    

    def pos_neg1_neg1(): # Supply Room
        
        if "pos_neg1_neg1_mark" not in game_mechanics:
            print('''
                As you close the wooden door behind you, you enter what is basically a huge supply closet.
                There are tools lying around on the floor, and the air is dry.
                There is low lighting coming from a single bulb exposed on the ceiling above the center of the room.
                You wonder what, if anything, is useful in here.
            ''')
            game_mechanics.append("pos_neg1_neg1_mark")
        else:
            print('''
                You return to the Supply Room. What do you do?
            ''')
        
        while 'jasmine_key' not in keyhole:
            action = input("Enter an action: ")
            if action == 'n':
                print('''
                Back through the wooden door you go.
                ''')
                pos_neg1_0()
                break
            elif action == 's':
                print('''
                Along the south wall you see a large wardrobe. You open it revealing about 10 uniforms.
                They are not all the same. They are organized by a couple jobs.
                Some look like chefs and some look like guards. Weirdly you haven't seen any guards around.
                You go back to your snooping.
                ''')
            elif action == 'e':
                if "pos_0_neg1_mark" not in game_mechanics: # entering that room for the first time
                    print('''
                On the east side of this room you see a rickety wooden door similar to the one on the north side.
                This door is a bit more beaten up, and you see some lighting peaking through from the next room.
                As you put your hand on the door knob, you smell the jasmine again! You enter the room.
                    ''')
                    pos_0_neg1()
                    break # this helps pop up back through stack on way out of loops
                else: # going back to Jasmine Room for the second+ time
                    print('''
                Back through the wooden door you go.
                    ''')
                    pos_0_neg1()
                    break
            elif action == 'w':
                if "supply_list" not in game_mechanics:
                    print('''
                    There is only one thing on the west wall: a chalkboard.
                    There is a title that reads "Supplies We Need For Projects."
                    That seems unimposing enough, but in a place like this... what is a project? You read the list:

                        Supplies We Need For Projects

                        sodium hypochlorite
                        light bulbs
                        acetone
                        duct tape
                        plates
                        zip ties
                        laundry detergent

                    After reading the list, you ponder what those could be used for. You continue your search.
                    ''')
                    game_mechanics.append("supply_list")
                else:
                    print('''
                    The lone chalkboard lines the west wall. Nothing else of interest is there.
                    ''')
            elif action == 'b':
                print(bag)
            elif action == 'p':
                print('You are 1 room west and 1 room south of your starting location.')
            elif action == 'q':
                print('Goodbye.')
                break
            else:
                print('That is an invalid action.')
    
    
    def pos_0_neg1(): # Jasmine Room
        
        if "pos_0_neg1_mark" not in game_mechanics:
            print('''
                As you walk through the rickety wooden door, you realize you have found the source of the jasmine smell.
                There is jasmine everywhere: dried leaves, live plants, and paintings.
                Whoever owns this room is obsessed with the plant.
                You do admit, it smelled good at first, but now the smell is becoming overwhelming. Make your search quick.
            ''')
            game_mechanics.append("pos_0_neg1_mark")
        else:
            print('''
                You return to the Jasmine Room. What do you do?
            ''')
        
        while 'jasmine_key' not in keyhole:
            action = input("Enter an action: ")
            if action == 'n':
                print('''
                There is a long, narrow, wooden table that is covered in a heap of dried jasmine.
                Right above the pile of jasmine is a small crack in the wall that leads to the room you woke up in.
                You deduce that the smell in the room to the north was coming from this room.
                Nothing else of interest is here.
                ''')
            elif action == 's': # location of jasmine_key
                if "jasmine_key" not in bag:
                    print('''
                Sitting on a small end table in the south side of this room you find 
                a small jasmine scented key... this may be helpful.
                    ''')
                    bag.append("jasmine_key")
                else:
                    print('''
                The end table where you found the jasmine key stands against the south wall.
                    ''')
            elif action == 'e':
                if "pos_1_neg1_mark" not in game_mechanics: # entering that room for the first time
                    print('''
                Whatever lies in the next room may not be good, but the smell of this room is hurting your head.
                You're just glad to be out of that room for now. You walk through the door.
                    ''')
                    pos_1_neg1()
                    break # this helps pop up back through stack on way out of loops
                else: # going back to Supply Room for the second+ time
                    print('''
                Back through the wooden door you go.
                    ''')
                    pos_1_neg1()
                    break
            elif action == 'w':
                print('''
                Back through the wooden door you go.
                ''')
                pos_neg1_neg1()
                break
            elif action == 'b':
                print(bag)
            elif action == 'p':
                print('You are 1 room south of your starting location.')
            elif action == 'q':
                print('Goodbye.')
                break
            else:
                print('That is an invalid action.')
    
    
    def pos_1_neg1(): # Guard Room
        
        if "pos_1_neg1_mark" not in game_mechanics:
            print('''
                As you walk into this new room you find something that you haven't seen before... a person.
                At the east wall is a guard posted still as can be... watching you.
                There's more to this room than the guard, but it is the most pressing thing at first.
                Now that your head is starting to clear up, you can think more clearly. What do you do?
            ''')
            game_mechanics.append("pos_1_neg1_mark")
        else:
            print('''
                You return to the Guard Room. What do you do?
            ''')
        
        while 'jasmine_key' not in keyhole:
            action = input("Enter an action: ")
            if action == 'n':
                print("""
                There is a door with many boards nailed along it. Whatever is beyond that door is not for you to see.
                """)
            elif action == 's':
                print("""
                Along the south wall there is a huge painting. As you look it over you appreciate its beauty.
                It looks like an old painting, but don't recognize it.
                The painting is of a ship docked in a harbor. There are a couple of men working in a smaller boat nearby.
                It is a gorgeous day, and even the reflection of the boat is painted in the water with detail.
                You should keep searching for a way out and reflect on this painting when you are free again.
                """)
                # https://www.vosegalleries.com/artists/frederick-j-mulhaupt (the painting)
            elif action == 'e':
                print("""
                There is a guard. They are wearing a uniform, and are posted up looking right at you. They start talking.
                "Hey there. I would get out of here soon. You won't like what comes if you stay too long."
                They start walking to the door at the north wall, and then settle.
                "Don't just stand there. Get on with it. You don't have long."
                They walk back to their eastern wall and return to their original position.
                """)
            elif action == 'w':
                print('''
                Back through the wooden door you go.
                ''')
                pos_0_neg1()
                break
            elif action == 'b':
                print(bag)
            elif action == 'p':
                print('You are 1 room east and 1 room south of your starting location.')
            elif action == 'q':
                print('Goodbye.')
                break
            else:
                print('That is an invalid action.')

    pos_0_0() # here is calling the wake up room

    if 'jasmine_key' in keyhole:
        print('''
        You turn the jasmine key in the door... it clicks. You push the door open and feel a strong breeze against your face.
        Then... you are grabbed by your shoulder. You whip around to see that guard with a cleaver in their hand.
        "Never come back here. You live, but not all of you gets to leave. This'll be good for the stew."
        Right then they shove your arm against the door and before you really know what's happening, you feel a massive pain.
        "Now get lost. Not everyone makes it Kip. Count yourself lucky."
        The door is slammed in your face and you fall over. As you reach for the ground to catch yourself... you notice.
        Your right arm past the elbow is gushing blood. Your body is in shock, and you don't know what to do.
        Your eyes adjust to the bright sunshine. It's midday and you look out to find a field of jasmine growing.
        You walk forward to find a bag on the ground. A grocery bag? Is there a town nearby? You hope so.
        You wrap your stump, and run as fast as you can.
        As you run, their words run through your head.
        "This'll be good for the stew." Oh god. You gag.
        Ahead you see a sign for a general hospital. You made it... almost all of you.
        
        THE END. Thank you so much for playing. Hope you had a good time.
        ''')
        
adventure() # this initiates the start of game
input()