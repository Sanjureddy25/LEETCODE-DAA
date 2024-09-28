def maximum_units(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    total_units = 0  
    for number_of_boxes, units_per_box in boxTypes:
        if truckSize == 0: 
            break
        boxes_to_take = min(number_of_boxes, truckSize)
        total_units += boxes_to_take * units_per_box
        truckSize -= boxes_to_take
    return total_units

# Example Usage
if __name__ == "__main__":
    boxTypes = [[1, 3], [2, 2], [3, 1]] 
    truckSize = 4  
    result = maximum_units(boxTypes, truckSize)
    print(f"Maximum total number of units that can be put on the truck: {result}")


OUTPUT:
    Maximum total number of units that can be put on the truck: 8
