def calculate_largest_loss(pricesLst: list) -> int:
    """ 
    This function calculates the largest possible lost that a client 
    could have made.
    """
    if len(pricesLst) == 0:
        return 0
    return max((pricesLst[item+1]-pricesLst[item] for item in range(len(pricesLst)-1)))
