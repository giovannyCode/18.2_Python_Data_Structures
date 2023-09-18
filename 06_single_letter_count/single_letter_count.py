def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    word_listInput = list(word)
    word_list =[]

    for word in word_listInput:
         word_list.append(word.lower())
         
    word_dictionary={}
    
    for word in word_list:
        if word in  word_dictionary:
            word_dictionary[word] =  word_dictionary[word]+1
        else:
               word_dictionary[word] = 1
    
    if letter.lower() in word_dictionary:
         return word_dictionary.get(letter.lower())
    else:
         return 0 
