import pandas as pd
import numpy as np

def get_special_workshop_preferences(data_frame):
    special_workshop_preferences = []
    for row_index in range(len(data_frame["girl_id"])):
        # if column entry is empty, assign 0 => 7th and 8th only
        if pd.isna(data_frame["special_workshop_preference"][row_index]):
            special_workshop_preferences.append(0)
        # if column entry is 'no_preference', assign 1 => 7th/8th and/or 9th/10th
        elif data_frame["special_workshop_preference"][row_index] == 'no_preference':
            special_workshop_preferences.append(1)
        # if column entry is 'orindary', assign 2 => 7th and 8th only
        elif data_frame["special_workshop_preference"][row_index] == 'ordinary':
            special_workshop_preferences.append(2)
        # if column entry is 'special', assign 3 => 9th/10th only
        elif data_frame["special_workshop_preference"][row_index] == 'special':
            special_workshop_preferences.append(3)
    
    return special_workshop_preferences

def sort_partners(data_frame, special_workshop_preferences):
    middle_school_individuals = []; middle_school_one_partner = []; middle_school_two_partners = []
    high_school_individuals = []; high_school_one_partner = []; high_school_two_partners = []
    # currently: does not account for the fact that high school can be paired up with middle school
    # for each participant 
    for row_index in range(len(data_frame["girl_id"])):
        # if the participant has no partners and is in middle school
        if pd.isna(data_frame["partner_id"][row_index]) and pd.isna(data_frame["partner_id_2"][row_index]) and data_frame["grade"][row_index] < 9:
            middle_school_individuals.append((special_workshop_preferences[row_index], data_frame["girl_id"][row_index]))
        # if the participant has no partners and is in high school
        elif pd.isna(data_frame["partner_id"][row_index]) and pd.isna(data_frame["partner_id_2"][row_index]) and data_frame["grade"][row_index] > 8:
            high_school_individuals.append((special_workshop_preferences[row_index], data_frame["girl_id"][row_index]))
        # if the participant has one partner and is in middle school
        elif pd.isna(data_frame["partner_id_2"][row_index]) and data_frame["grade"][row_index] < 9:
            middle_school_one_partner.append((data_frame["girl_id"][row_index], int(data_frame["partner_id"][row_index]), special_workshop_preferences[row_index]))
        # if the participant has one partner and is in high school
        elif pd.isna(data_frame["partner_id_2"][row_index]) and data_frame["grade"][row_index] > 8:
            high_school_one_partner.append((data_frame["girl_id"][row_index], int(data_frame["partner_id"][row_index]), special_workshop_preferences[row_index]))
        # if the participant has two partners and is in middle school
        elif pd.notna(data_frame["partner_id_2"][row_index]) and data_frame["grade"][row_index] < 9:
            middle_school_two_partners.append((data_frame["girl_id"][row_index], int(data_frame["partner_id"][row_index]), int(data_frame["partner_id_2"][row_index]), special_workshop_preferences[row_index]))
        # if the participant has two partners and is in high school
        elif pd.notna(data_frame["partner_id_2"][row_index]) and data_frame["grade"][row_index] > 8:
            high_school_two_partners.append((data_frame["girl_id"][row_index], int(data_frame["partner_id"][row_index]), int(data_frame["partner_id_2"][row_index]), special_workshop_preferences[row_index]))

    return middle_school_individuals, middle_school_one_partner, middle_school_two_partners, high_school_individuals, high_school_one_partner, high_school_two_partners

def generate_unique_subbroups(mid_ind, mid_one, mid_two, high_ind, high_one, high_two):
    # generate unique subgroups for each category
    # middle school and high school individuals are already unique (duh)
    unique_mid_ind = mid_ind
    unique_high_ind = high_ind
    # middle school one partner
    mid_one_groups = []
    for subgroup in range(len(mid_one)):
        subgroup_ids = []
        for participant in range(len(mid_one[subgroup])):
            subgroup_ids.append(int(mid_one[subgroup][participant]))
        mid_one_groups.append(sorted(subgroup_ids))
    unique_mid_one = [list(x) for x in set(tuple(x) for x in mid_one_groups)]
    # middle school two partners
    mid_two_groups = []
    for subgroup in range(len(mid_two)):
        subgroup_ids = []
        for participant in range(len(mid_two[subgroup])):
            subgroup_ids.append(int(mid_two[subgroup][participant]))
        mid_two_groups.append(sorted(subgroup_ids))
    unique_mid_two = [list(x) for x in set(tuple(x) for x in mid_two_groups)]
    # high school one partner
    high_one_groups = []
    for subgroup in range(len(high_one)):
        subgroup_ids = []
        for participant in range(len(high_one[subgroup])):
            subgroup_ids.append(int(high_one[subgroup][participant]))
        high_one_groups.append(sorted(subgroup_ids))
    unique_high_one = [list(x) for x in set(tuple(x) for x in high_one_groups)]
    # high school two partners
    high_two_groups = []
    for subgroup in range(len(high_two)):
        subgroup_ids = []
        for participant in range(len(high_two[subgroup])):
            subgroup_ids.append(int(high_two[subgroup][participant]))
        high_two_groups.append(sorted(subgroup_ids))
    unique_high_two = [list(x) for x in set(tuple(x) for x in high_two_groups)]

    return unique_mid_ind, unique_mid_one, unique_mid_two, unique_high_ind, unique_high_one, unique_high_two


def sort_partners_no_grades(data_frame, special_workshop_preferences):
    individuals = []; one_partner = []; two_partners = []
    # for each participant 
    for row_index in range(len(data_frame["girl_id"])):
        # if the participant has no partners 
        if pd.isna(data_frame["partner_id"][row_index]) and pd.isna(data_frame["partner_id_2"][row_index]):
            individuals.append((special_workshop_preferences[row_index], data_frame["girl_id"][row_index]))
        # if the participant has one partner 
        elif pd.isna(data_frame["partner_id_2"][row_index]):
            one_partner.append((data_frame["girl_id"][row_index], int(data_frame["partner_id"][row_index]), special_workshop_preferences[row_index]))
        # if the participant has two partners 
        elif pd.notna(data_frame["partner_id_2"][row_index]):
            two_partners.append((data_frame["girl_id"][row_index], int(data_frame["partner_id"][row_index]), int(data_frame["partner_id_2"][row_index]), special_workshop_preferences[row_index]))

    return individuals, one_partner, two_partners

def generate_unique_subbroups_no_grades(ind, one, two):

    ind_groups = []
    for subgroup in range(len(ind)):
        subgroup_ids = []
        for participant in range(len(ind[subgroup])):
            subgroup_ids.append(int(ind[subgroup][participant]))
        ind_groups.append(sorted(subgroup_ids))
    unique_ind = [list(x) for x in set(tuple(x) for x in ind_groups)]

    one_groups = []
    for subgroup in range(len(one)):
        subgroup_ids = []
        for participant in range(len(one[subgroup])):
            subgroup_ids.append(int(one[subgroup][participant]))
        one_groups.append(sorted(subgroup_ids))
    unique_one = [list(x) for x in set(tuple(x) for x in one_groups)]

    two_groups = []
    for subgroup in range(len(two)):
        subgroup_ids = []
        for participant in range(len(two[subgroup])):
            subgroup_ids.append(int(two[subgroup][participant]))
        two_groups.append(sorted(subgroup_ids))
    unique_two = [list(x) for x in set(tuple(x) for x in two_groups)]

    return unique_ind, unique_one, unique_two
