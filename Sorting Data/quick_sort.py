
# Time Complexity: mostly O(n log n)
# Wosrt case can be O(n^2)
# Overall better than mergesort

def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the two partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)

def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotvalue = datavalues[first]
    # establish the upper and lower indexes
    lower = first + 1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # TODO: advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        # TODO: advance the upper index
        while upper >= lower and datavalues[upper] >= pivotvalue:
            upper -= 1

        # TODO: if the two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp
    
    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper

# test the quicksort with data
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(items)
quickSort(items, 0, len(items)-1)
print(items)