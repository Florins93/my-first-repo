from total_sum import total_sum

def calculate_average(prices):
    if len(prices) == 0:
        return 0  

    return total_sum(prices) / len(prices)