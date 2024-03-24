import pandas as pd
import numpy as np

def flatten_comprehension(matrix):
    return [item for row in matrix for item in row]

def assign_9th_10th_workshops(data_frame, previous_ninth_tenth_workshops, ninth_tenth_capacities, previous_seventh_eight_workshops, seventh_eighth_capacities, unique_high_two, unique_high_one, unique_high_ind):
    
    seventh_eight_workshops = [[] for _ in range(len(seventh_eighth_capacities))]
    ninth_tenth_workshops = [[] for _ in range(len(ninth_tenth_capacities))]
    
    # two partner groups
    for participants in unique_high_two:
        if participants[0] == 3: # 3 means they want to be in 9th/10th grade workshops only, only option for these particular groups this year
            workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participants[1]][0]][12:17] # get 9th/10th workshop preferences for that participant (i.e. the whole subgroup)
            count = 0
            for workshop in workshop_preferences:
                count += 1
                if workshop == 0: # means they don't care which workshop they attend
                    workshop = np.random.randint(23, 32)

                id = participants[1]
                list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                # list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])

                    # if adding participants would not put workshop over capacity AND participants not previously assigned to workshop
                if (ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -3 >= 0) and ((id not in list_1)):
                    ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1].append(participants[1:]) # add group of 3 to workshop
                    ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -= 3 # decrement workshop capacity by 3 (since group of 3)
                    break   
                if count > len(workshop_preferences) - 1: 
                    count = 0
                    while count < (len(ninth_tenth_workshops) - 1):
                        workshop = np.arange(23, 32)[count]
                        count += 1

                        id = participants[1]
                        list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                        # list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])

                        if (ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -3 >= 0) and ((id not in list_1)):
                            ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1].append(participants[1:])
                            ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -= 3
                            break
    # one partner groups
    for participants in unique_high_one:
        if participants[0] == 3: # 3 means they want to be in 9th/10th grade workshops only
            workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participants[1]][0]][12:17] # get 9th/10th workshop preferences for that participant (i.e. the whole subgroup)
            count = 0
            for workshop in workshop_preferences:
                count += 1
                if workshop == 0: # means they don't care which workshop they attend
                    workshop = np.random.randint(23, 32)

                id = participants[1]
                list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                # list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])

                if (ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -2 >= 0) and ((id not in list_1)):
                    ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1].append(participants[1:])
                    ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -= 2 # decrement workshop capacity by 2 (since group of 2)
                    break
                if count > len(workshop_preferences) - 1:   
                    count = 0
                    while count < (len(ninth_tenth_workshops) - 1):
                        workshop = np.arange(23, 32)[count]
                        count += 1

                        id = participants[1]
                        list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                        # list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])

                        if (ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -2 >= 0) and ((id not in list_1)):
                            ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1].append(participants[1:])
                            ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -= 2
                            break
        if participants[0] == 2: # 2 means they want to be in 7th/8th grade workshops only
            workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participants[1]][0]][4:12] # get 7th/8th workshop preferences for that participant (i.e. the whole subgroup)
            count = 0
            for workshop in workshop_preferences:
                count += 1
                if workshop == 0: # means they don't care which workshop they attend
                    workshop = np.random.randint(1, 23)

                id = participants[1]
                # list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])

                if (seventh_eighth_capacities[(int(workshop) - 1)] -2 >= 0) and ((id not in list_2)):
                    seventh_eight_workshops[(int(workshop) - 1)].append(participants[1:])
                    seventh_eighth_capacities[(int(workshop) - 1)] -= 2 # decrement workshop capacity by 2 (since group of 2)
                    break   
                if count > len(workshop_preferences) - 1:
                    count = 0
                    while count < (len(seventh_eight_workshops) - 1):
                        workshop = np.arange(1, 23)[count]
                        count += 1
                        if (seventh_eighth_capacities[(int(workshop) - 1)] -2 >= 0) and ((id not in list_2)):
                            seventh_eight_workshops[(int(workshop) - 1)].append(participants[1:])
                            seventh_eighth_capacities[(int(workshop) - 1)] -= 2
                            break
        if participants[0] == 1: # 1 means they have no preference towards 7th/8th or 9th/10th grade workshops, so assign to 9th/10th first if possible
            workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participants[1]][0]][12:17] # get 9th/10th workshop preferences for that participant (i.e. the whole subgroup)
            for workshop in workshop_preferences:
                if workshop == 0: # means they don't care which workshop they attend
                    workshop = np.random.randint(23, 32)

                id = participants[1]
                list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                # list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])

                if (ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -2 >= 0) and ((id not in list_1)):
                    ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1].append(participants[1:])
                    ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -= 2 # decrement workshop capacity by 2 (since group of 2)
                    break
                else:
                    workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participants[1]][0]][4:12]
                    count = 0
                    for workshop in workshop_preferences:
                        count += 1
                        if workshop == 0:
                            workshop = np.random.randint(1, 23)

                        id = participants[1]
                        # list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                        list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])

                        if (seventh_eighth_capacities[(int(workshop) - 1)] -2 >= 0) and ((id not in list_2)):
                            seventh_eight_workshops[(int(workshop) - 1)].append(participants[1:])
                            seventh_eighth_capacities[(int(workshop) - 1)] -= 2 # decrement workshop capacity by 2 (since group of 2)
                            break
                        if count > len(workshop_preferences) - 1:
                            count = 0
                            while count < (len(seventh_eight_workshops) - 1):
                                workshop = np.arange(1, 23)[count]
                                count += 1
                                if (seventh_eighth_capacities[(int(workshop) - 1)] -2 >= 0) and ((id not in list_2)):
                                    seventh_eight_workshops[(int(workshop) - 1)].append(participants[1:])
                                    seventh_eighth_capacities[(int(workshop) - 1)] -= 2
                                    break
    # individual groups
    for participant in unique_high_ind:
        if participant[0] == 3: # 3 means they want to be in 9th/10th grade workshops only
            workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participant[1]][0]][12:17] # get 9th/10th workshop preferences for that participant
            count = 0
            for workshop in workshop_preferences:
                count += 1
                if workshop == 0:
                    workshop = np.random.randint(23, 32)

                id = participant[1]
                list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                # list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])

                if (ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -1 >= 0) and ((id not in list_1)):
                    ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1].append(participant[1:])
                    ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -= 1 # decrement workshop capacity by 1 (since individual)
                    break
                if count > len(workshop_preferences) - 1:
                    count = 0
                    while count < (len(ninth_tenth_workshops) - 1):
                        workshop = np.arange(23, 32)[count]
                        count += 1
                        if (ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1]) -1 >= 0 and ((id not in list_1)):
                            ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1].append(participant[1:])
                            ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -= 1
                            break
        if participant[0] == 2: # 2 means they want to be in 7th/8th grade workshops only
            workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participant[1]][0]][4:12] # get 7th/8th workshop preferences for that participant
            count = 0
            for workshop in workshop_preferences:
                count += 1
                if workshop == 0: # means they don't care which workshop they attend
                    # generate a random number between 1 and 31 -> assign to a random workshop
                    workshop = np.random.randint(1, 23)

                id = participant[1]
                # list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])

                if (seventh_eighth_capacities[(int(workshop) - 1)] -1 >= 0) and ((id not in list_2)):
                    # print(id, list_2)
                    seventh_eight_workshops[(int(workshop) - 1)].append(participant[1:])
                    seventh_eighth_capacities[(int(workshop) - 1)] -= 1 # decrement workshop capacity by 1 (since individual)
                    break
                if count > len(workshop_preferences) - 1:
                    count = 0
                    while count < (len(seventh_eight_workshops) - 1):
                        workshop = np.arange(1, 23)[count]
                        count += 1
                        if (seventh_eighth_capacities[(int(workshop) - 1)] -1 >= 0) and ((id not in list_2)):
                            seventh_eight_workshops[(int(workshop) - 1)].append(participant[1:])
                            # print((int(workshop) - 1))
                            seventh_eighth_capacities[(int(workshop) - 1)] -= 1
                            break
        if participant[0] == 1: # 1 means they have no preference towards 7th/8th or 9th/10th grade workshops, so assign to 9th/10th first if possible
            workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participant[1]][0]][12:17] # get 9th/10th workshop preferences for that participant
            count = 0
            for workshop in workshop_preferences:
                count += 1
                if workshop == 0:
                    workshop = np.random.randint(23, 32)

                id = participant[1]
                list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                # list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])
                
                if (ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -1 >= 0) and ((id not in list_1)):
                    ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1].append(participant[1:])
                    ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -= 1 # decrement workshop capacity by 1 (since individual)
                    break
                if count > len(workshop_preferences) - 1:
                    count = 0
                    while count < (len(ninth_tenth_workshops) - 1):
                        workshop = np.arange(23, 32)[count]
                        count += 1
                        if (ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -1 >= 0) and ((id not in list_1)):
                            ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1].append(participant[1:])
                            ninth_tenth_capacities[(int(workshop) - 1) % 21 - 1] -= 1
                            break
                else:
                    workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participant[1]][0]][4:12]
                    count = 0
                    for workshop in workshop_preferences:
                        count += 1
                        if workshop == 0:
                            workshop = np.random.randint(1, 23)

                        id = participant[1]
                        # list_1 = flatten_comprehension(previous_ninth_tenth_workshops[(int(workshop) - 1) % 21 - 1])
                        list_2 = flatten_comprehension(previous_seventh_eight_workshops[(int(workshop) - 1)])

                        if (seventh_eighth_capacities[(int(workshop) - 1)] -1 >= 0) and ((id not in list_2)):
                            seventh_eight_workshops[(int(workshop) - 1)].append(participant[1:])
                            seventh_eighth_capacities[(int(workshop) - 1)] -= 1 # decrement workshop capacity by 1 (since individual)
                            break
                        if count > len(workshop_preferences) - 1:
                            count = 0
                            while count < (len(seventh_eight_workshops) - 1):
                                workshop = np.arange(1, 23)[count]
                                count += 1
                                if (seventh_eighth_capacities[(int(workshop) - 1)] -1 >= 0) and ((id not in list_2)):
                                    seventh_eight_workshops[(int(workshop) - 1)].append(participant[1:])
                                    seventh_eighth_capacities[(int(workshop) - 1)] -= 1
                                    break
    return seventh_eight_workshops, ninth_tenth_workshops, seventh_eighth_capacities

def assign_7th_8th_workshops(data_frame, semi_filled_seventh_eighth_workshops, previous_seventh_eighth_workshops_1, previous_seventh_eighth_workshops_2, seventh_eighth_capacities, unique_mid_two, unique_mid_one, unique_mid_ind, third_round = False):

    # do this instead
    if third_round == False:
        seventh_eighth_workshops = semi_filled_seventh_eighth_workshops
    if third_round == True:
        seventh_eighth_workshops = [[] for _ in range(len(seventh_eighth_capacities))]

    # two partner groups
    for participants in unique_mid_two:
        workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participants[1]][0]][4:12] # get 7th/8th workshop preferences for that participant (i.e. the whole subgroup)
        count = 0
        for workshop in workshop_preferences:
            count += 1
            if workshop == 0:
                workshop = np.random.randint(1, 23)
            
            id = participants[1]
            list_1 = flatten_comprehension(previous_seventh_eighth_workshops_1[(int(workshop) - 1)])
            list_2 = flatten_comprehension(previous_seventh_eighth_workshops_2[(int(workshop) - 1)])

            if (seventh_eighth_capacities[(int(workshop) - 1)] -3 >= 0) and ((id not in list_1) and (id not in list_2)):
                seventh_eighth_workshops[(int(workshop) - 1)].append(participants[1:])
                seventh_eighth_capacities[(int(workshop) - 1)] -= 3 # decrement workshop capacity by 3 (since group of 3)
                break
            if count > len(workshop_preferences) - 1:
                count = 0
                while count < (len(seventh_eighth_workshops) - 1):
                    workshop = np.arange(1, 23)[count]
                    count += 1
                    if (seventh_eighth_capacities[(int(workshop) - 1)] -3 >= 0) and ((id not in list_1) and (id not in list_2)):
                        seventh_eighth_workshops[(int(workshop) - 1)].append(participants[1:])
                        seventh_eighth_capacities[(int(workshop) - 1)] -= 3
                        break
    # one partner groups
    for participants in unique_mid_one:
        workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participants[1]][0]][4:12] # get 7th/8th workshop preferences for that participant (i.e. the whole subgroup)
        count = 0
        for workshop in workshop_preferences:
            count += 1
            if workshop == 0:
                workshop = np.random.randint(1, 23)

            id = participants[1]
            list_1 = flatten_comprehension(previous_seventh_eighth_workshops_1[(int(workshop) - 1)])
            list_2 = flatten_comprehension(previous_seventh_eighth_workshops_2[(int(workshop) - 1)])

            if (seventh_eighth_capacities[(int(workshop) - 1)] -2 >= 0) and ((id not in list_1) and (id not in list_2)):
                seventh_eighth_workshops[(int(workshop) - 1)].append(participants[1:])
                seventh_eighth_capacities[(int(workshop) - 1)] -= 2 # decrement workshop capacity by 2 (since group of 2)
                break
            if count > len(workshop_preferences) - 1: 
                count = 0
                while count < (len(seventh_eighth_workshops) - 1):
                    workshop = np.arange(1, 23)[count]
                    count += 1
                    if (seventh_eighth_capacities[(int(workshop) - 1)] -2 >= 0) and ((id not in list_1) and (id not in list_2)):
                        seventh_eighth_workshops[(int(workshop) - 1)].append(participants[1:])
                        seventh_eighth_capacities[(int(workshop) - 1)] -= 2
                        break
    # individual groups
    for participant in unique_mid_ind:
        workshop_preferences = data_frame.iloc[data_frame.index[data_frame["girl_id"] == participant[1]][0]][4:12] # get 7th/8th workshop preferences for that participant
        count = 0
        for workshop in workshop_preferences:
            count += 1
            if workshop == 0:
                workshop = np.random.randint(1, 23)

            id = participant[1]
            list_1 = flatten_comprehension(previous_seventh_eighth_workshops_1[(int(workshop) - 1)])
            list_2 = flatten_comprehension(previous_seventh_eighth_workshops_2[(int(workshop) - 1)])

            if (seventh_eighth_capacities[(int(workshop) - 1)] -1 >= 0) and ((id not in list_1) and (id not in list_2)):
                seventh_eighth_workshops[(int(workshop) - 1)].append(participant[1:])
                seventh_eighth_capacities[(int(workshop) - 1)] -= 1 # decrement workshop capacity by 1 (since individual)
                break
            # if you've exhausted all preferences, ascend through the list of workshops and assign to the first one that has space
            if count > len(workshop_preferences) - 1:
                count = 0
                while count < (len(seventh_eighth_workshops)):
                    workshop = np.arange(1, 23)[count]
                    count += 1
                    if (seventh_eighth_capacities[(int(workshop) - 1)] -1 >= 0) and ((id not in list_1) and (id not in list_2)):
                        seventh_eighth_workshops[(int(workshop) - 1)].append(participant[1:])
                        seventh_eighth_capacities[(int(workshop) - 1)] -= 1
                        break
    return seventh_eighth_workshops
