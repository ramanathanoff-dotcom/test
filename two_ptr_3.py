def rm_duplicates(list):
    if not list:
        return 0
    slow=0
    for fast in range(1,len(list)):
        if list[slow]!=list[fast]:
            slow+=1
            list[slow]=list[fast]

    return list[:slow+1]


# Get list input
numbers = [int(x) for x in input().split(",")]
print(rm_duplicates(numbers))
