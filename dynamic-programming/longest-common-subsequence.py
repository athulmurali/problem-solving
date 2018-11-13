import pytest



def lcs(str1, str2,  index_str1, index_str2):    
    if index_str1 < 0 or index_str2 < 0:
        return 0
    if str1[index_str1] == str2[index_str2]:
        print("common character: {}    str1: {}  str2 :{} ".format(str1[index_str1],index_str1, index_str2))
        return  1 + lcs(str1, str2,  index_str1-1, index_str2 -1)
    else: 
        return max( lcs(str1, str2,  index_str1-1, index_str2),
                   lcs(str1, str2,  index_str1, index_str2 -1))




def test_asdf():
    str1 = "abcde"
    str2 = "ae"
    print("str1 :", str1, "    str2: ", str2)
    assert lcs(str1, str2, len(str1)-1 , len(str2) -1) == 2
    

def test_empty():
    str1 = ""
    str2 = ""
    print("str1 :", str1, "    str2: ", str2)
    assert lcs(str1, str2, len(str1)-1 , len(str2) -1) == 0
    
def test_no_common():
    str1 = "123456"
    str2 = "abcdffgf"
    print("str1 :", str1, "    str2: ", str2)
    assert lcs(str1, str2, len(str1)-1 , len(str2) -1) == 0
pytest.main()
