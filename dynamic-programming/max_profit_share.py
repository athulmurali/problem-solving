import math
import pytest

def max_share_diff(arr):
    current_val =0
    best_difference =0
    smallest_val =math.inf
    for i in arr:
        #print(i)
        if  i < smallest_val:
            smallest_val = i

        current_difference = i - smallest_val
        #print(current_difference)

        if best_difference < current_difference:

            best_difference = current_difference
            
    return best_difference



def test_case1():
    arr =[0,3,2,5,1,8,5,8]
    assert 8 == max_share_diff(arr)
    
def test_case2():
    arr =[5,4,3,2,1]
    assert 0 == max_share_diff(arr)
pytest.main()
