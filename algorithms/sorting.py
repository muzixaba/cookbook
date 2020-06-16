def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''
    for passnum in range(len(items)-1,0,-1):
        for i in range(passnum):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items


def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0 
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1
    return items


def quick_sort(items):
    '''Return array of items, sorted in ascending order'''
    less = []
    equal = []
    greater = []

    if len(items) > 1:
        pivot = items[0]
        for x in items:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else: 
                if x > pivot:
                    greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)   
    else:  
        return items