"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    for i in range(len(array)):
        if array[i] > array[len(array)-1-i]:
            
            #print(array[i] , array[len(array)-1-i])
    return array

# 21 4	1	3	9	20	25	6	21	14
# 21 4	1	3	9	20	25	6	14	21
# 6	 4	1	3	9	20	25	14	21	21
# 6	 4	1	3	9	25	14	20	21	21
# 6	 4	1	3	9	14	25	20	21	21
# 1	 4	3	6	9	14	25	20	21	21
# 1	 3	4	6	9	14	25	20	21	21
# 1	 3	4	6	9	14	21	20	21	25
# 1	 3	4	6	9	14	20	21	21	25

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(test)
print(quicksort(test))