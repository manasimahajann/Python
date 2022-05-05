arr = [1,3,2,4,3,6,4,8]
count = 0
with open('increasedCount.txt') as f:
    lines = f.readlines()

    lines = [int(i) for i in lines]
    print(len(lines))
for index in range(len(lines)-1):
    # print(arr[index], arr[index+1])
    if(lines[index]<lines[index+1]):
        count = count+1

print(count)