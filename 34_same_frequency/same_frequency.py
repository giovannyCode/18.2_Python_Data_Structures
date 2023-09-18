def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dictionary_one ={}
    for number in str(num1):
        if number in dictionary_one:
            dictionary_one[number] = dictionary_one[number]+1
        else:
            dictionary_one[number]=1

    dictionary_two ={}
    for number in str(num2):
        if number in dictionary_two:
            dictionary_two[number] = dictionary_two[number]+1
        else:
            dictionary_two[number]=1

    return  dictionary_one ==  dictionary_two


   