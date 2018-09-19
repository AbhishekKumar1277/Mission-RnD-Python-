__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the index of left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).

- input is an indexable, value is any object.
- return -1 if not found or index of 1st occurance if found.
'''
def left_binary_search(input, value):
    pass
    low=0
    high=len(input)-1
    mid=(low+high)//2
    if value not in input:
        return -1
    else:    
        if input[mid]==value:
            if input[mid-1]==value:
                li=input[0:mid]
                for i in range(0,len(li)):
                    if(li[i]==value):
                        return i
            elif input[mid+1]==value: 
                    li=input[mid: ]
                    for i in range(0,len(li)):
                        if(li[i]==value):
                            return i+mid  
            else:
                return mid                            
        elif input[mid]<value:
            li=input[mid: ]
            for i in range(0,len(li)):
                if(li[i]==value):
                    return i+mid            
        else:
            li=input[0:mid]
            for i in range(0,len(li)):
                if(li[i]==value):
                    return i        
# write your own exhaustive tests :)
def test_left_binary_search_student():
    pass
    assert 2 ==left_binary_search([1,4,5,6,6,9,15,15,43,54,332,405,762,762,9854],5)
    assert 5 ==left_binary_search([0,4,6,6,9,15,15,43,762,9854],15)
    assert 0 ==left_binary_search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,2],1)
    assert 6 ==left_binary_search([1,1,1,1,1,1,2,2,2,2,2,2],2)
    input = range(10)
    for index, value in enumerate(input):
        assert index == left_binary_search(input, value)
    assert -1 == left_binary_search(input, -10)
# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_left_binary_search(left_binary_search)