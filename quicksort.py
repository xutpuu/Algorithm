"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    i = len(array) - 1
    j = 0
    b = True
    while b == True:
        if i != j:
            if array[i] <= array[j]:
                f = array[j]
                l = array[i]
                p = array[i - 1]
                array[j] = p
                array[i] = f
                array[i - 1] = l
                i -= 1
            else:
                j += 1
        else:
            b = False
    k = i
    i = i - 2
    j = 0
    b = True
    while b == True:
        if i != j:
            if array[i] <= array[j]:
                f = array[j]
                l = array[i]
                p = array[i - 1]
                array[j] = p
                array[i] = f
                array[i - 1] = l
                i -= 1
            else:
                j += 1
        else:
            b = False
    i = len(array) - 1
    j = k + 1
    b = True
    while b == True:
        if i != j:
            if array[i] <= array[j]:
                f = array[j]
                l = array[i]
                p = array[i - 1]
                array[j] = p
                array[i] = f
                array[i - 1] = l
                i -= 1
            else:
                j += 1
        else:
            b = False

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
