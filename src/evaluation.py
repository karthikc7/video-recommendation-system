def calculate_ctr(recommended, actual):
    # Calculate Click-Through Rate (CTR)
    clicks = sum([1 if rec in actual else 0 for rec in recommended])
    ctr = clicks / len(recommended)
    return ctr

# Example: Mean Average Precision (MAP) could be implemented here
def mean_average_precision(recommended, actual):
    map_score = 0
    for idx, rec_list in enumerate(recommended):
        precision = 0
        for i, rec in enumerate(rec_list):
            if rec in actual[idx]:
                precision += 1 / (i+1)
        map_score += precision / len(actual)
    
    return map_score
