# Internal packages
from challenge_2 import calculate_largest_loss


def test_calculate_largest_loss_function():
    """This function tests the calculate_largest_loss function"""
    pricesLst = [2, 5, 10, 12, 13]
    assert calculate_largest_loss(pricesLst) == 5    


def test_calculate_largest_loss_function_with_0_lenght():
    """This function tests the calculate_largest_loss function
    with 0 elements"""
    pricesLst = []
    assert calculate_largest_loss(pricesLst) == 0   
