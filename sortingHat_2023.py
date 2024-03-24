#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Sort EYH participants into workshops based on preferences and existance of partners
# Russell W. Burgett
# 3/13/2023 - 3/14/2023
# 3/13/2024

# import packages
import os
import pandas as pd
import numpy as np

import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

rng = np.random.default_rng()

### YEAR-TO-YEAR VARIABLES (CHANGE THESE WHEN NEEDED!) ###

# import csv file as pandas dataframe
# Note: csv file should be in same directory as .py (will put in README.txt)
#       or can use os.chdir(path) to go to location of workshop_preferences file
#       also, made manual changes to csv (and saved under new name) if girl forgot to list partner ID
path = r"/Users/russthebuss/Downloads"
os.chdir(path)

file = "UPDATED_workshop_preferences_EYH_2024.csv"
# keep columns with data relevant for sorting
cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# ['grade', 'girl_id', 'workshop_needs', 'partner_id', 'ws_1'.,.,.'ws9_5', 'special_workshop_preference']
# varies based on what workshops chairs send you
df = pd.read_csv(file, usecols=cols)
# Note: 268 particpants this year (2023)

### Workshop Capacties ###
seventh_eighth_capacities = [
    10,
    13,
    10,
    16,
    13,
    25,
    20,
    12,
    16,
    20,
    15,
    10,
    25,
    12,
    25,
    25,
    11,
    22,
    15,
    11,
    15,
    25,
]
ninth_capacities = [
    10,
    12,
    12,
    10,
    25,
    16,
    10,
    11,
    10,
]


### FUNCTIONS TO SORT EYH PARTICIPANTS DATA (procede with caution) ###


def sort_partners(data_frame):
    yes_partner_list = []
    no_partner_list = []
    unique_partners_list = []
    # for each student
    for row_index in range(len(data_frame["partner_id"])):
        # if not NULL
        if pd.notna(data_frame["partner_id"][row_index]):
            # add to list that says the student has a partner
            yes_partner_list.append(data_frame["girl_id"][row_index])
            # if students partner is NOT already in yes_partner_list, then add pair to unique partners list
            # otherwise don't need to add (would lead to double counting of pairs)
            if data_frame["partner_id"][row_index] not in yes_partner_list:
                unique_partners_list.append(
                    (
                        data_frame["girl_id"][row_index],
                        data_frame["partner_id"][row_index],
                        data_frame["special_workshop_preference"][row_index],
                    )
                )
        # otherwise, no partner and add student to list that says so
        else:
            no_partner_list.append(
                (
                    data_frame["girl_id"][row_index],
                    data_frame["special_workshop_preference"][row_index],
                )
            )
    return yes_partner_list, no_partner_list, unique_partners_list


def sort_special_workshop_preferences(participants_list):
    ninth_workshops = []
    seventh_eighth_workshops = []
    # for each particpant (pair or single student)
    for participant in participants_list:
        # if preference == 'no_preference', put in 9th grade workshops list
        if participant[-1] == "no_preference":
            ninth_workshops.append(participant)
        # if preference == 'special', also put in 9th grade workshops list
        elif participant[-1] == "special":
            ninth_workshops.append(participant)
        # otherwise put in 7th/8th grade workshops list
        else:
            seventh_eighth_workshops.append(participant)
    return seventh_eighth_workshops, ninth_workshops


def fill_workshop_prefrences_list(preference_list):
    # print(preference_list[0])
    new_preference_list = []
    for preference_index in range(len(preference_list[0])):

        # # if 'nan' (i.e. if True), then --> NULL --> only found in 9th grade workshops col
        # if np.isnan(preference_list[0][preference_index]):
        #     # so assign random 9th grade workshop (regardless of preferences)
        #     rand_int = np.random.randint(1, 9, 1)[
        #         0
        #     ]  # index zero to keep scalar, not array
        #     # if already a preference, pick a new one
        #     while rand_int in new_preference_list:
        #         rand_int = np.random.randint(1, 9, 1)[0]
        #     new_preference_list.append(rand_int)

        # if 0, then they don't care which workshop they are assigned
        if preference_list[0][preference_index] == 0:
            # if preference_index < 9
            if preference_index < 9:
                # assign them a random 7th/8th grade workshop
                rand_int = np.random.randint(1, 20, 1)[
                    0
                ]  # index zero to keep scalar, not array
                # make sure it is a new int()
                while rand_int in new_preference_list:
                    rand_int = np.random.randint(1, 20, 1)[
                        0
                    ]  # index zero to keep scalar, not array
                new_preference_list.append(rand_int)
            # if preference_index >= 9
            if preference_index >= 9:
                # then assign a random 9th grade workshop (regardless of special preference)
                rand_int = np.random.randint(1, 9, 1)[
                    0
                ]  # index zero to keep scalar, not array
                # make sure it is a new int()
                while rand_int in new_preference_list:
                    rand_int = np.random.randint(1, 9, 1)[0]
                new_preference_list.append(rand_int)

        # otherwise, keep their workshop preference
        else:
            new_preference_list.append(preference_list[0][preference_index])

    # print(new_preference_list)
    return new_preference_list


def get_workshop_preferences(participant, data_frame):
    preference_list = []

    participant_ID = float(participant[0])

    row_index_num = data_frame[data_frame["girl_id"] == participant_ID].index[0]

    first_preference = data_frame["ws_1"][row_index_num]
    second_preference = data_frame["ws_2"][row_index_num]
    thrid_preference = data_frame["ws_3"][row_index_num]

    fourth_preference = data_frame["ws_4"][row_index_num]
    fifth_preference = data_frame["ws_5"][row_index_num]
    sixth_preference = data_frame["ws_4"][row_index_num]

    seventh_preference = data_frame["ws_7"][row_index_num]
    eighth_preference = data_frame["ws_8"][row_index_num]
    ninth_preference = data_frame["ws9_1"][row_index_num]

    tenth_preference = data_frame["ws9_2"][row_index_num]
    eleventh_preference = data_frame["ws9_3"][row_index_num]
    twelfth_preference = data_frame["ws9_4"][row_index_num]
    thirteenth_preference = data_frame["ws9_5"][row_index_num]

    # three cases for preference:
    #   1) a number that corresponds to the workshop they want
    #   2) zero, which means they don't care and can go into any workshop
    #       -> replace with some random number not already in the list
    #   3) NULL, which means they aren't elegible for those (9th grade) workshops (replace with -1?)
    preference_list.append(
        [
            first_preference,
            second_preference,
            thrid_preference,
            fourth_preference,
            fifth_preference,
            sixth_preference,
            seventh_preference,
            eighth_preference,
            ninth_preference,
            tenth_preference,
            eleventh_preference,
            thirteenth_preference,
        ]
    )
    filled_preference_list = fill_workshop_prefrences_list(preference_list)
    # Now two cases for preference:
    #   1) a unique number corresponding to the workshop they want
    #   2) NULL, which means they aren't elegible for those (9th grade) workshops anyway
    return filled_preference_list


def assign_workshops(
    seventh_eighth_workshops_lists,
    ninth_workshops_lists,
    students_in_seventh_eighth_workshops,
    students_in_ninth_workshops,
    data_frame,
    seventh_eighth_capacities,
    ninth_capacities,
):

    # shuffle arrays
    lower_workshops_array = np.array(students_in_seventh_eighth_workshops)
    rng.shuffle(lower_workshops_array)
    upper_workshops_array = np.array(students_in_ninth_workshops)
    rng.shuffle(upper_workshops_array)

    for participant in lower_workshops_array:
        preference_list = get_workshop_preferences(participant, data_frame)
        for preference in preference_list:
            # dumb fix, but okay for now I think
            if (
                preference > 19
            ):  # 7th/8th student requested a 9th grade workshop (by mistake)
                preference = np.random.randint(1, 20, 1)[
                    0
                ]  # assign them a random workshop preference
            # switch from numerical indexing to list indexing
            preference = preference - 1
            # if workshop is not full (i.e. under capacity)
            if (
                len(seventh_eighth_workshops_lists[preference])
                < seventh_eighth_capacities[preference]
            ):
                # add student to workshop
                seventh_eighth_workshops_lists[preference].append(participant)
                # and stop looking at preferences for that student
                break  # move onto next student

    for participant in upper_workshops_array:
        preference_list = get_workshop_preferences(participant, data_frame)
        # sort list in ascending order (9th grade workshops first)
        preference_list.sort()
        for preference in preference_list:
            # dumb fix, but okay for now I think
            if (
                preference > 8
            ):  # 9th grade student requested 7th/8th grade workshop (even though "special"/"no_preference")
                preference = np.random.randint(1, 9, 1)[
                    0
                ]  # assign them a random workshop preference
            # to go from numerical indexing to list indexing
            preference = preference - 1
            # if workshop is not full (i.e. under capacity)
            if len(ninth_workshops_lists[preference]) <= ninth_capacities[preference]:
                # add student to workshop
                ninth_workshops_lists[preference].append(participant)
                # and stop looking at preferences for that student
                break  # move onto next student

    return seventh_eighth_workshops_lists, ninth_workshops_lists


def assign_next_round_of_workshops(
    previous_workshops_list_7th8th,
    previous_workshops_list_9th,
    current_seventh_eighth_workshops_lists,
    current_ninth_workshops_lists,
    students_in_seventh_eighth_workshops,
    students_in_ninth_workshops,
    data_frame,
    seventh_eighth_capacities,
    ninth_capacities,
):

    # shuffle arrays (again)
    lower_workshops_array = np.array(students_in_seventh_eighth_workshops)
    rng.shuffle(lower_workshops_array)
    upper_workshops_array = np.array(students_in_ninth_workshops)
    rng.shuffle(upper_workshops_array)

    for participant in lower_workshops_array:
        preference_list = get_workshop_preferences(participant, data_frame)
        for preference in preference_list:
            # dumb fix, but okay for now I think
            if (
                preference > 19
            ):  # 7th/8th student requested a 9th grade workshop (by mistake)
                preference = np.random.randint(1, 20, 1)[
                    0
                ]  # assign them a random workshop preference
            # switch from numerical indexing to list indexing
            preference = preference - 1
            if (float(participant[0]) not in previous_workshops_list_7th8th[preference] and len(current_seventh_eighth_workshops_lists[preference]) < seventh_eighth_capacities[preference]):
                # add student to workshop
                current_seventh_eighth_workshops_lists[preference].append(participant)
                # and stop looking at preferences for that student
                break  # move onto next student

    for participant in upper_workshops_array:
        preference_list = get_workshop_preferences(participant, data_frame)
        # sort list in ascending order (9th grade workshops first)
        preference_list.sort()
        for preference in preference_list:
            # dumb fix, but okay for now I think
            if (
                preference > 8
            ):  # 9th grade student requested 7th/8th grade workshop (even though "special"/"no_preference")
                preference = np.random.randint(1, 9, 1)[
                    0
                ]  # assign them a random workshop preference
            # to go from numerical indexing to list indexing
            preference = preference - 1
            # if student not previously in workshop and workshop is not yet full
            if (float(participant[0]) not in previous_workshops_list_9th[preference] and len(current_ninth_workshops_lists[preference]) < ninth_capacities[preference]):
                # add student to workshop
                current_ninth_workshops_lists[preference].append(participant)
                # and stop looking at preferences for that student
                break  # move onto next student

    return current_seventh_eighth_workshops_lists, current_ninth_workshops_lists


def assign_final_round_of_workshops_7th8th(
    first_round_workshops_list_7th8th,
    second_round_workshops_list_7th8th,
    current_seventh_eighth_workshops_lists,
    students_in_seventh_eighth_workshops,
    data_frame,
    seventh_eighth_capacities,
):

    # shuffle arrays (again)
    lower_workshops_array = np.array(students_in_seventh_eighth_workshops)
    rng.shuffle(lower_workshops_array)

    for participant in lower_workshops_array:
        preference_list = get_workshop_preferences(participant, data_frame)
        for preference in preference_list:
            # dumb fix, but okay for now I think
            if (
                preference > 19
            ):  # 7th/8th student requested a 9th grade workshop (by mistake)
                preference = np.random.randint(1, 20, 1)[
                    0
                ]  # assign them a random workshop preference
            # switch from numerical indexing to list indexing
            preference = preference - 1
            # if student wasn't in workshop during first round AND student wansn't in workshop during second round AND the workshop is not yet full
            if (
                float(participant[0]) not in first_round_workshops_list_7th8th[preference]

                and float(participant[0]) not in second_round_workshops_list_7th8th[preference]

                and len(current_seventh_eighth_workshops_lists[preference]) < seventh_eighth_capacities[preference]
            ):
                # add student to workshop
                current_seventh_eighth_workshops_lists[preference].append(participant)
                # and stop looking at preferences for that student
                break  # move onto next student

    return current_seventh_eighth_workshops_lists


def cleanup_workshop_assignments_pairs(workshops_list):
    cleaner_workshops_list = []
    for workshop_index in range(len(workshops_list)):
        workshop = []
        for pair_index in range(len(workshops_list[workshop_index])):
            participant_1 = workshops_list[workshop_index][pair_index][0]
            workshop.append(participant_1)
            participant_2 = workshops_list[workshop_index][pair_index][1]
            workshop.append(participant_2)
        cleaner_workshops_list.append(workshop)
    return cleaner_workshops_list


def cleanup_workshop_assignments_solos(workshops_list):
    cleaner_workshops_list = []
    for workshop_index in range(len(workshops_list)):
        workshop = []
        for student_index in range(len(workshops_list[workshop_index])):
            # if string
            if "str" in str(type(workshops_list[workshop_index][student_index])):
                participant = float(workshops_list[workshop_index][student_index])
            # else array
            else:
                participant = float(workshops_list[workshop_index][student_index][0])
            workshop.append(participant)
        cleaner_workshops_list.append(workshop)
    return cleaner_workshops_list


def unpack_workshop_assignemtns(
    workshops_1_7th8th,
    workshops_1_9th,
    workshops_2_7th8th,
    workshops_2_9th,
    workshops_3_7th8th,
    data_frame,
):
    participants = data_frame["girl_id"]
    first_workshop_assignments_list = []
    second_workshop_assignments_list = []
    third_workshop_assignments_list = []
    # for each student
    for participant_index in range(len(participants)):
        # FIND FIRST WORKSHOP
        # search 7th/8th grade workshops
        for workshop_1_index in range(len(workshops_1_7th8th)):
            if (
                data_frame["girl_id"][participant_index]
                in workshops_1_7th8th[workshop_1_index]
            ):
                # add ID and assignment to list, stop looking for their first workshop and move onto the next student
                first_workshop_assignments_list.append(
                    (
                        data_frame["girl_id"][participant_index],
                        workshop_1_index + 1,
                    )  # back to list indexing
                )
                break
        # search 9th grade workshops
        for workshop_1_index in range(len(workshops_1_9th)):
            if (
                data_frame["girl_id"][participant_index]
                in workshops_1_9th[workshop_1_index]
            ):
                # add ID and assignment to list, stop looking for their first workshop and move onto the next student
                first_workshop_assignments_list.append(
                    (
                        data_frame["girl_id"][participant_index],
                        workshop_1_index + 20,
                    )  # back to list indexing and appropriate workshop # for 9th grade workshops
                )
                break
        # FIND SECOND WORKSHOP
        # search 7th/8th grade workshops
        for workshop_2_index in range(len(workshops_2_7th8th)):
            if (
                data_frame["girl_id"][participant_index]
                in workshops_2_7th8th[workshop_2_index]
            ):
                # add ID and assignment to list, stop looking for their first workshop and move onto the next student
                second_workshop_assignments_list.append(
                    (
                        data_frame["girl_id"][participant_index],
                        workshop_2_index + 1,
                    )  # back to list indexing
                )
                break
        # search 9th grade workshops
        for workshop_2_index in range(len(workshops_2_9th)):
            if (
                data_frame["girl_id"][participant_index]
                in workshops_2_9th[workshop_2_index]
            ):
                # add ID and assignment to list, stop looking for their first workshop and move onto the next student
                second_workshop_assignments_list.append(
                    (
                        data_frame["girl_id"][participant_index],
                        workshop_2_index + 20,
                    )  # back to list indexing and appropriate workshop # for 9th grade workshops
                )
                break
        # FIND THIRD WORKSHOP
        for workshop_3_index in range(len(workshops_3_7th8th)):
            if (
                data_frame["girl_id"][participant_index]
                in workshops_3_7th8th[workshop_3_index]
            ):
                # add ID and assignment to list, stop looking for their first workshop and move onto the next student
                third_workshop_assignments_list.append(
                    (
                        data_frame["girl_id"][participant_index],
                        workshop_3_index + 1,
                    )  # back to list indexing
                )
                break

    return (
        first_workshop_assignments_list,
        second_workshop_assignments_list,
        third_workshop_assignments_list,
    )


### FUNCTION CALLS/SORTING ###

# get lists of participants and their partners (or just solo participants)
yes_partner_list, no_partner_list, unique_partners_list = sort_partners(df)

# split partners into those attending 7th/8th grade workshops, and those attending 9th grade workshops
(
    seventh_eighth_workshops_pairs,
    ninth_workshops_pairs,
) = sort_special_workshop_preferences(unique_partners_list)

# split solos into those attending 7th/8th grade workshops, and those attending 9th grade workshops
(
    seventh_eighth_workshops_solos,
    ninth_workshops_solos,
) = sort_special_workshop_preferences(no_partner_list)


### FIRST ROUND OF WORKSHOP ASSIGNMENT ###

num_7th8th_workshops = 19 # int
num_9th_workshops = 9 # int

# initialize emtpy workshop lists
seventh_eighth_workshops_lists = [[] for _ in range(num_7th8th_workshops)]
ninth_workshops_lists = [[] for _ in range(num_9th_workshops)]

# assign workshops for pairs of students
(
    ws_1_seventh_eighth_pairs,
    ws_1_ninth_pairs,
) = assign_workshops(
    seventh_eighth_workshops_lists,
    ninth_workshops_lists,
    seventh_eighth_workshops_pairs,
    ninth_workshops_pairs,
    df,
    seventh_eighth_capacities,
    ninth_capacities,
)
# cleanup/reorganize workshop lists
ws_1_seventh_eighth_pairs = cleanup_workshop_assignments_pairs(
    ws_1_seventh_eighth_pairs
)
ws_1_ninth_pairs = cleanup_workshop_assignments_pairs(
    ws_1_ninth_pairs
)

# add workshop assignments for solo students
ws_1_seventh_eighth, ws_1_ninth = assign_workshops(
    ws_1_seventh_eighth_pairs,
    ws_1_ninth_pairs,
    seventh_eighth_workshops_solos,
    ninth_workshops_solos,
    df,
    seventh_eighth_capacities,
    ninth_capacities,
)
# cleanup/reorganize workshop lists
ws_1_7th8th = cleanup_workshop_assignments_solos(ws_1_seventh_eighth)
ws_1_9th = cleanup_workshop_assignments_solos(ws_1_ninth)


# ### SECOND ROUND OF WORKSHOPS ###

# initialize emtpy workshop lists
seventh_eighth_workshops_lists = [[] for _ in range(num_7th8th_workshops)]
ninth_workshops_lists = [[] for _ in range(num_9th_workshops)]

# assign workshops for pairs of students
(
    ws_2_seventh_eighth_pairs,
    ws_2_ninth_pairs,
) = assign_next_round_of_workshops(
    ws_1_7th8th,
    ws_1_9th,
    seventh_eighth_workshops_lists,
    ninth_workshops_lists,
    seventh_eighth_workshops_pairs,
    ninth_workshops_pairs,
    df,
    seventh_eighth_capacities,
    ninth_capacities,
)

# cleanup/reorganize workshop lists
ws_2_seventh_eighth_pairs = cleanup_workshop_assignments_pairs(
    ws_2_seventh_eighth_pairs
)
ws_2_ninth_pairs = cleanup_workshop_assignments_pairs(
    ws_2_ninth_pairs
)

# assign workshops for solo students
(
    ws_2_seventh_eighth,
    ws_2_ninth,
) = assign_next_round_of_workshops(
    ws_1_7th8th,
    ws_1_9th,
    ws_2_seventh_eighth_pairs,
    ws_2_ninth_pairs,
    seventh_eighth_workshops_solos,
    ninth_workshops_solos,
    df,
    seventh_eighth_capacities,
    ninth_capacities,
)

# cleanup/reorganize workshop lists
ws_2_7th8th = cleanup_workshop_assignments_solos(
    ws_2_seventh_eighth
)
ws_2_9th = cleanup_workshop_assignments_solos(ws_2_ninth)


### THIRD (FINAL) ROUND OF WORKSHOPS ###

# initialize emtpy workshop lists
seventh_eighth_workshops_lists = [[] for _ in range(num_7th8th_workshops)]

# assign workshops for pairs of students
ws_3_seventh_eighth_pairs = assign_final_round_of_workshops_7th8th(
    ws_1_7th8th,
    ws_2_7th8th,
    seventh_eighth_workshops_lists,
    seventh_eighth_workshops_pairs,
    df,
    seventh_eighth_capacities,
)

# cleanup/reorganize workshop lists
ws_3_seventh_eighth_pairs = cleanup_workshop_assignments_pairs(
    ws_3_seventh_eighth_pairs
)

# assign workshops for solo students
ws_3_seventh_eighth = assign_final_round_of_workshops_7th8th(
    ws_1_7th8th,
    ws_2_7th8th,
    ws_3_seventh_eighth_pairs,
    seventh_eighth_workshops_solos,
    df,
    seventh_eighth_capacities,
)

# cleanup/reorganize workshop lists
ws_3_7th8th = cleanup_workshop_assignments_solos(
    ws_3_seventh_eighth
)

### FINAL OUTPUT (.csv) ###
# lists -> pandas df -> .csv
# cols = ['girl_id', 'partner_id', '#_workshop_1', '#_workshop_2', '#_workshop_3']

unpacked_ws1, unpacked_ws2, unpacked_ws3 = unpack_workshop_assignemtns(
    ws_1_7th8th,
    ws_1_9th,
    ws_2_7th8th,
    ws_2_9th,
    ws_3_7th8th,
    df,
)

# unpacked_ws1 -> tuple with ('girl_id', '#_ws_1') in ascending order

# construct output dataframe
ws_1 = []
for participant in unpacked_ws1:
    ws_1.append(participant[1])

ws_2 = []
for participant in unpacked_ws2:
    ws_2.append(participant[1])

# careful with the third one (7th/8th only)
ws_3_participants = []
ws_3_workshops = []
for participant_index in range(len(unpacked_ws3)):
    ws_3_participants.append(unpacked_ws3[participant_index][0])
    ws_3_workshops.append(unpacked_ws3[participant_index][1])

# for student in data frame
ws_3_list = []
ws_3_index_counter = 0
# for each participant
for participant_index in range(len(df["girl_id"])):
    # if girl_id is in ws_3 (girl is participating in thrid workshop)
    if df["girl_id"][participant_index] in ws_3_participants:
        # add that girl_id and the workshop # to list
        ws_3_list.append(
            (df["girl_id"][participant_index], ws_3_workshops[ws_3_index_counter])
        )
        # increase the ws_3_workshops index counter
        ws_3_index_counter += 1
    else:
        # otherwise, add the girl_id and np.nan, but don't move to the next ws_3_workshops index
        ws_3_list.append((df["girl_id"][participant_index], np.nan))

ws_3 = []
for participant in ws_3_list:
    ws_3.append(participant[1])

new_cols = [0, 2]  # ['girl_id', 'partner_id']

new_df = pd.read_csv(file, usecols=new_cols)

new_df["ws_1"] = ws_1
new_df["ws_2"] = ws_2
new_df["ws_3"] = ws_3

# save new data_frame
new_df.to_csv("sorted_workshop_assignments.csv", index = False)

# Works okay, though certainly not optimal (superfilous code). Some small bugs maybe.
# Will make notes in README.txt
# Upload to Github and make note for website chairs to point to URL
