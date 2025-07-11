def largest_number(lst):
    # Base case: if the list has only one element
    if len(lst) == 1:
        return lst[0]
    
    # Compare the first element with the largest of the rest of the list
    else:
        max_of_rest = largest_number(lst[1:])
        if lst[0] > max_of_rest:
            return lst[0]
        else:
            return max_of_rest

if __name__ == "__main__":
    print(largest_number([1, 4, 5, 3]))            # Returns largest number: 5
    print(largest_number([3, 1, 6, 8, 2, 4, 5]))    # Returns largest number: 8
