def lemonade_change(bills):
    five_count = 0  
    ten_count = 0   
    for bill in bills:
        if bill == 5:
            five_count += 1
        elif bill == 10:
            if five_count > 0:
                five_count -= 1
                ten_count += 1
            else:
                return False
        elif bill == 20:
            if ten_count > 0 and five_count > 0:
                ten_count -= 1
                five_count -= 1
            elif five_count >= 3:
                five_count -= 3
            else:
                return False

    return True

# Example Usage
if __name__ == "__main__":
    bills = [5, 5, 10, 10, 20]
    result = lemonade_change(bills)
    print(f"Can provide correct change to all customers: {result}")


OUTPUT:
    Can provide correct change to all customers: False
