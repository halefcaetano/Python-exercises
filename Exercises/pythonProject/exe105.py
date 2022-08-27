def grades(*num, sit=False):
    """
    :param num: One or more student grades (multiple accepted).
    :param sit: Optional value, indicating whether or not to add the situation.
    :return: Dictionary with various information about the situation of the class.
    """
    media = 0
    d = {}
    for c, i in enumerate(num):
        if c == 0:
            smart = notSmart = i
        else:
            if i > smart:
                smart = i
            if i < notSmart:
                notSmart = i
        media += i
    mediaFinal = media / len(num)
    d['Total'] = len(num)
    d['Highest'] = smart
    d['Lowest'] = notSmart
    d['Media'] = mediaFinal
    if sit:
        if mediaFinal > 7:
            status = 'Good'
            d['Status'] = status
        elif (mediaFinal < 7) and (mediaFinal > 6):
            status = 'Reasonable'
            d['Status'] = status
        else:
            status = 'Bad'
            d['Status'] = status
    return d



print(grades(10, 9, 8, 5, 4, 3, 2, sit=True))
