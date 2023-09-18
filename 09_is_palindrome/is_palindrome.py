def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    input_phrase = phrase.replace(" ", "")
    
    input_phase_list_original= list (input_phrase)
    input_phase_list_modified =[]
    for letter in input_phase_list_original:
       input_phase_list_modified.append(letter.lower())

    input_phrase_reversed = input_phase_list_modified[::-1]

    is_palindrome_list= []
    for index, letter in enumerate(input_phase_list_modified):
         if letter == input_phrase_reversed[index]:
             is_palindrome_list.append(True)
         else:
             is_palindrome_list.append(False)

    if False in is_palindrome_list:
        return False
    else:
        return True

        
         
