def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30

       >>> m2 = [
        ...    [1, 2, 3,4],
        ...    [4, 5, 6,2],
        ...    [7, 8, 9,3],
               [1, 8, 9,3],
        ... ]

        
    """
    count = 0
    for i, item in enumerate(matrix):
       count= item[i]+count +item [len(item) - (i+1)]
       
    return count

        

    