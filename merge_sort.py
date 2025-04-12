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

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """

    mid = len(list)//2 # // Floor division operator
    left = list[:mid] # Slicing syntax
    right = list[mid:] # Slicing - starting at the midpoint and going to the end of the list

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    """
    l = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1 # or i = i + 1
        else:
            l.append(right[j])
            j += 1 # or j = j + 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        