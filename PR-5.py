def max_content_children(greed_factors, cookie_sizes):
    greed_factors.sort()
    cookie_sizes.sort()
    child_index = 0
    cookie_index = 0
    content_children = 0
    while child_index < len(greed_factors) and cookie_index < len(cookie_sizes):
        if cookie_sizes[cookie_index] >= greed_factors[child_index]:
            content_children += 1  
            child_index += 1 
        cookie_index += 1
    return content_children

# Example Usage
if __name__ == "__main__":
    greed_factors = [1, 2, 3]
    cookie_sizes = [1, 1]
    result = max_content_children(greed_factors, cookie_sizes)
    print(f"Maximum number of content children: {result}")
    
OUTPUT:
    Maximum number of content children: 1

