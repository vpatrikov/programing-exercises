lst = [8,3,5,10,7]

def bubble_sort(lst):
    index = 0
    end = len(lst) - 1
        
    while (end > 0):
    
        if lst[index] > lst[index + 1]:
            temp = lst[index]
            lst[index] = lst[index + 1]
            lst[index + 1] = temp

        index += 1

        if index == end:
            end -= 1;
            index = 0

    return lst

def selection_sort(lst):
    for i in range (len(lst) -1 ):
        min_i = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_i]:
                min_i = j
        
        temp = lst[i]
        lst[i] = lst[min_i]
        lst[min_i] = temp

    return lst
        
print(selection_sort(lst))

    
