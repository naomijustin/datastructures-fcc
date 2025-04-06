def merge_sort(list): 
    """ 
    Sorts a list in ascending order 
    Returns a new sorted list 

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sorts the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    if len(list) <= 1: # Stopping condition
        return list
    
    left_half, right_half = split(list) # Split list into 2
    left = merge_sort(left_half) # Recursive section of left
    right = merge_sort(right_half) # Recursive section of right

    return merge(left, right) # Merges left and right sublist backwards