def fl_index():

    arr= [1,2,4,7,7,7,7,7,7,9,9]
    target = 7  
    ls = None
    index_values = []
    for index in range(len(arr)):
        if arr[index] == target:
            index_values.insert(0, index)
            break


    for num in reversed(range(len(arr))) : 
        if arr[num] == target:
            index_values.insert(1, num)
            break
 

    if index_values:
        return index_values
    return [-1,-1]

if __name__ == '__main__':
    print(fl_index())
