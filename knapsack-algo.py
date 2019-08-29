#!/usr/bin/env python

# Fractional Knapsack


def fractional_knapsack(knap_weight, data_items):
    """Fractional Knapsack.

    Inputs:
        knap_weight = Total weight the Knapsack can hold
        data_items =  dictionary containing key which is the name of item
                      and value as a tuple (weight of item, value of item)
    """
    ratio_map = {}

    for name, wt_val in data_items.items():
        ratio_map[name] = wt_val[1] / float(wt_val[0])
    import ipdb; ipdb.set_trace()
    # sort value/weight ratio in descending
    # we take value/weight since the goal is to get max value per weight
    sorted_value_weight = sorted(ratio_map.iteritems(), key=lambda (k, v): (v, k), reverse=True)

    knapsack = {}.fromkeys(data_items.keys(), 0)
    knapsack_accum_weight = 0
    while knapsack_accum_weight < knap_weight:
        for each in sorted_value_weight:
            item_name = each[0]
            weight = data_items[each[0]][0]
            if knapsack_accum_weight + weight <= knap_weight:
                knapsack_accum_weight += weight
                knapsack[item_name] += 1
            else:
                # add its fraction
                remaining = knap_weight - knapsack_accum_weight
                fraction_to_add = remaining / float(weight)
                knapsack[item_name] += fraction_to_add
                knapsack_accum_weight += fraction_to_add * weight
                pass
    print knapsack_accum_weight  # this must be equal to knap_weight
    print knapsack

knap_weight = 52
data_items = {'A': (10, 60), 'B': (20, 100), 'C': (30, 120)}
fractional_knapsack(knap_weight, data_items)
