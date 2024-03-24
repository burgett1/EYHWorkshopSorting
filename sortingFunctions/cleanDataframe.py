import pandas as pd
import numpy as np
import math

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def flatten_comprehension(matrix):
    return [item for row in matrix for item in row]

def create_mid_only_dataframe(data_frame, first_round_seventh_eight_workshops, second_round_seventh_eight_workshops):

    # edit unique_mid_ids to include 9th/10th grader who go assigned two 7th/8th grade workshops in the first two rounds
    first_round_seventh_eight_workshops_flat = [flatten_comprehension(workshop) for workshop in first_round_seventh_eight_workshops]
    first_round_seventh_eight_workshops_flatter = flatten_comprehension(first_round_seventh_eight_workshops_flat)        
    # print(first_round_seventh_eight_workshops_flatter)


    second_round_seventh_eight_workshops_flat = [flatten_comprehension(workshop) for workshop in second_round_seventh_eight_workshops]
    second_round_seventh_eight_workshops_flatter = flatten_comprehension(second_round_seventh_eight_workshops_flat)
    # print(second_round_seventh_eight_workshops_flatter)

    unique_mid_ids = first_round_seventh_eight_workshops_flatter + second_round_seventh_eight_workshops_flatter

    for row_index in range(len(data_frame["grade"])):
        if int(data_frame["girl_id"][row_index]) not in unique_mid_ids:
            # print(data_frame["girl_id"][row_index])
            data_frame.drop(row_index, inplace=True)
    data_frame.reset_index(drop=True, inplace=True)
    return data_frame

def create_workshop_assignments_dataframe(data_frame, first_round_seventh_eight_workshops, first_round_ninth_tenth_workshops, second_round_seventh_eight_workshops, second_round_ninth_tenth_workshops, third_round_seventh_eighth_workshops):
    
    workshop_assignments_df = pd.DataFrame(columns=["girl_id", "grade", "partner_id", "partner_id_2", "workshop_1", "workshop_2", "workshop_3"])

    first_round_seventh_eight_workshops_flat = []
    for workshop in first_round_seventh_eight_workshops:
        first_round_seventh_eight_workshops_flat.append(flatten_comprehension(workshop))
    
    first_round_ninth_tenth_workshops_flat = []
    for workshop in first_round_ninth_tenth_workshops:
        first_round_ninth_tenth_workshops_flat.append(flatten_comprehension(workshop))

    # for each girl in data_frame
    for row_index in range(len(data_frame)):
        # get girl_id
        girl_id = data_frame["girl_id"][row_index].astype(int)
        grade = data_frame["grade"][row_index].astype(int)

        if pd.notna(data_frame["partner_id"][row_index]):
            partner_id = data_frame["partner_id"][row_index].astype(int)
        else:
            partner_id = data_frame["partner_id"][row_index]

        if pd.notna(data_frame["partner_id_2"][row_index]):
            partner_id_2 = data_frame["partner_id_2"][row_index].astype(int)
        else:
            partner_id_2 = data_frame["partner_id_2"][row_index]
        # cross reference girl_id with workshop assignments
        for workshop_index in range(len(first_round_seventh_eight_workshops_flat)):
            if girl_id in first_round_seventh_eight_workshops_flat[workshop_index]:
                workshop_assignments_df = workshop_assignments_df.append({"girl_id": girl_id, "grade": grade, "partner_id": partner_id, "partner_id_2": partner_id_2, "workshop_1": workshop_index + 1, "workshop_2": np.nan, "workshop_3": np.nan}, ignore_index=True)
                break 

        for workshop_index in range(len(first_round_ninth_tenth_workshops_flat)):
            if girl_id in first_round_ninth_tenth_workshops_flat[workshop_index]:
                workshop_assignments_df = workshop_assignments_df.append({"girl_id": girl_id, "grade": grade, "partner_id": partner_id, "partner_id_2": partner_id_2, "workshop_1": (workshop_index + 1 + 22), "workshop_2": np.nan, "workshop_3": np.nan}, ignore_index=True)
                break

    second_round_seventh_eight_workshops_flat = []
    for workshop in second_round_seventh_eight_workshops:
        second_round_seventh_eight_workshops_flat.append(flatten_comprehension(workshop))
    
    second_round_ninth_tenth_workshops_flat = []
    for workshop in second_round_ninth_tenth_workshops:
        second_round_ninth_tenth_workshops_flat.append(flatten_comprehension(workshop))

    for row_index in range(len(data_frame)):
        girl_id = data_frame["girl_id"][row_index].astype(int)
        for workshop_index in range(len(second_round_seventh_eight_workshops_flat)):
            if girl_id in second_round_seventh_eight_workshops_flat[workshop_index]:
                workshop_assignments_df["workshop_2"][row_index] = workshop_index + 1
                break
        
        for workshop_index in range(len(second_round_ninth_tenth_workshops_flat)):
            if girl_id in second_round_ninth_tenth_workshops_flat[workshop_index]:
                workshop_assignments_df["workshop_2"][row_index] = workshop_index + 1 + 22
                break

    third_round_seventh_eight_workshops_flat = []
    for workshop in third_round_seventh_eighth_workshops:
        third_round_seventh_eight_workshops_flat.append(flatten_comprehension(workshop))

    for row_index in range(len(data_frame)):
        girl_id = data_frame["girl_id"][row_index].astype(int)
        for workshop_index in range(len(third_round_seventh_eight_workshops_flat)):
            list = third_round_seventh_eight_workshops_flat[workshop_index] 
            if girl_id in list:
                workshop_assignments_df["workshop_3"][row_index] = workshop_index + 1
                break
            else:
                workshop_assignments_df["workshop_3"][row_index] = np.nan


    return workshop_assignments_df
                                