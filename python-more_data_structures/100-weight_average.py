#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight = 0
    total_weighted_score = 0

    for score_weight in my_list:
        score = score_weight[0]
        weight = score_weight[1]
        total_weighted_score += score * weight
        total_weight += weight
    return total_weighted_score / total_weight
