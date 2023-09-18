def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    word_list = list(phrase)
    word_dictionary={}
    
    for word in word_list:
        if word in  word_dictionary:
            word_dictionary[word] =  word_dictionary[word]+1
        else:
               word_dictionary[word] = 1
    
    print(word_dictionary)
