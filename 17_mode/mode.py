def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    numbersDictionary ={}
    for number in nums:
        if number in numbersDictionary:
            numbersDictionary[number] =  numbersDictionary[number]+1
        else :
            numbersDictionary[number] = 1
    print (numbersDictionary)
    max_value = max(numbersDictionary.values())

    for (number, frecuency) in numbersDictionary.items():
         if frecuency ==max_value:
             return number  

