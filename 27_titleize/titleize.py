def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lower_case_phrase = phrase.lower()
    list_of_words = lower_case_phrase.split(" ")
    capitalized_list =[]
    for word in list_of_words:
        capitalized_list.append(word.capitalize())
    return ' '.join(capitalized_list)
