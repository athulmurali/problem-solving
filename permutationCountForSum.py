

def get_input():
    str_input = input().split()
    str_input = [int(i) for i in str_input] 
    # Given : the first four values seperated by spaces forms the target array
    target_array,target_sum = str_input[0:4], str_input[4]
    
    return(target_array,target_sum)
     
def find_count_max_ways(target_array, target_sum):
    print(target_array, target_sum)
    pass


def test_base_case():
    tg_arr = [0, 1, 2 , 3]
    tg_sum = 10
    find_count_max_ways(tg_arr, tg_sum)
    pass
    
    
test_base_case()
