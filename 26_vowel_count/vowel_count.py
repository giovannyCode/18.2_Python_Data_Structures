def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """ 
    vowel_dicctionary ={}
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.lower() in  vowel_dicctionary:
                vowel_dicctionary[letter.lower()] =  vowel_dicctionary[letter.lower()] + 1 
            else:
                vowel_dicctionary[letter.lower()] = 1

    return vowel_dicctionary  