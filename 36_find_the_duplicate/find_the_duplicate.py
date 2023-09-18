def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    count_of_numbers_dicctionary ={}

    for number in nums:
        if number in count_of_numbers_dicctionary:
            count_of_numbers_dicctionary[number]= count_of_numbers_dicctionary[number]+1
        else:
            count_of_numbers_dicctionary[number]= 1
    
    for key , value in count_of_numbers_dicctionary.items():
        if value >= 2:
            return key

            


