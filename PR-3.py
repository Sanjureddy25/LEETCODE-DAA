class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
def fractional_knapsack(W, items, n):
    items.sort(key=lambda x: x.value / x.weight, reverse=True) 
    total_value = 0.0  
    for i in range(n):
        if items[i].weight <= W:
            total_value += items[i].value  
            W -= items[i].weight 
        else:
            total_value += items[i].value * (W / items[i].weight)
            break  
    return total_value
# Example usage
if __name__ == "__main__":
    W = 50  
    items = [
        Item(60, 10),  
        Item(100, 20),  
        Item(120, 30) 
    ]
    n = len(items)
    max_value = fractional_knapsack(W, items, n)
    print(f"Maximum value in knapsack: {max_value:.2f}")
