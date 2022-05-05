def lf_ele():


    arr = [3,4,5,6,6,6, 7,8,9]
    target = 5
    for index in range(len(arr)):
        if arr[index] == target:
            start = index
            while arr[index+1] < len(arr) and arr[index+1] == target:
                index += 1
            return [start, index]
    return [-1, -1]


if __name__ == '__main__':
    print(lf_ele())
