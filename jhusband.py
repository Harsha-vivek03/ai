people_dict = {"h1": 0, "h2": 0, "h3": 0, "w1": 0, "w2": 0, "w3": 0}

people_names = list(people_dict.keys())

boat = 0

 

def alterbit(bit):

    return abs(bit - 1)

 

def jealousy(d):

    for i in [1, 2, 3]:

        if d["h" + str(i)] != d["w" + str(i)]:

            if (d["h1"] == d["w" + str(i)]) or (d["h2"] == d["w" + str(i)]) or (d["h3"] == d["w" + str(i)]):

                return 1

    return 0

 

def turn():

    global boat

    good_people = []

    for i in people_names:

        if people_dict[i] == boat:

            good_people.append(i)

    print("Available to choose from: " + ', '.join(good_people))

    move = input("Choose your move. ")

    boat_other = 0

    for i in people_names:

        if i in move:

            if not (i in good_people):

                boat_other = 1

                print("Cannot move " + i + "; the boat is on the wrong side!\n")

                return 0

    counter = 0

    for i in people_names:

        if i in move:

            counter += 1

    if counter > 2:

        print("Cannot move more than two!\n")

        return 0

    temp_people_dict = dict(people_dict)

    for i in people_names:

        if i in move:

            temp_people_dict[i] = alterbit(temp_people_dict[i])

    if jealousy(temp_people_dict):

        print("A wife cannot be left with another man unless her husband is present.")

        return 0

    counter = 0

    for i in people_names:

        if i in move:

            people_dict[i] = alterbit(people_dict[i])

            counter += 1

    if counter != 0:

        boat = alterbit(boat)

 

turn_number = 0

while not (sum(people_dict[i] for i in people_names) == 6):

    turn()

    turn_number += 1

print("Congratulations! You won in " + str(turn_number) + " turns. (Minimum 11)")