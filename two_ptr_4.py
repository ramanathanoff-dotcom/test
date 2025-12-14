def mv_zero_end(arr):
    slow=0
    for fast in range(1,len(arr)):
        if arr[fast]!=0:
            arr[slow],arr[fast]=arr[fast],arr[slow]
            slow+=1
    return arr


# Get list input
numbers = [int(x) for x in input().split(",")]
print(mv_zero_end(numbers))