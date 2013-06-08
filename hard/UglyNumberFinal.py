def permute(numstr, ops):
    """
    Given a string rep of a number, return all possible 
    permuations of that number by inserting any one of ops
    in between each number.
    """
    try:
        int(numstr)
        result = []
        for i in range(len(numstr)):
            for op in ops:
                s = numstr[:i]+op+numstr[i:]
                print s
            print i
    except:
        raise Exception("String does not represent a number")
