def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    
    """
    phase_list = list(phrase)

    phase_list[0]= phase_list[0].upper()

    return ''.join(phase_list)
