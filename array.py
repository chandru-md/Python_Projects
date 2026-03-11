import array

'''my_array = array.array('i')
print(my_array)
print('*'*100)
my_array_2 = array.array('i',[1,2,3,4,5])
print(my_array_2)

print('*'*100)
import numpy as np

np_array = np.array([],dtype=int)

print(np_array)
print('*'*100)

np_arr_2 = np.array([1,2,3,4,5,6])
print(np_arr_2)
print('*'*100)'''

"""my_arr_1 = array.array('i',[1,2,3,4,5])
print(my_arr_1)
#my_arr_1.insert(0,6)
print(my_arr_1)
my_arr_1.insert(5,6)

print(my_arr_1)"""

"""arr_1 = array.array('i',[1,2,3,4,5,6])

def traverseArray(array):
    for i in array:
        print(i)


traverseArray(arr_1)
"""

myArr = array.array('i',[1,2,3,4,5,6])

"""def accessElement(array,index):
    if index>len(array):
        print("None")
    else:
        print(array[index])

accessElement(myArr,100)"""

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] ==target:
            return i
    return -1

print(linear_search(myArr,3))
