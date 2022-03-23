def get_min_avg_max(numbers):
    return min(numbers),sum(numbers)/len(numbers),max(numbers)
print(get_min_avg_max([0,10,1,9]))