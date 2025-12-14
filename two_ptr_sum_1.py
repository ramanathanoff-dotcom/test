def two_ptr_sum(list,target):
    left,right=0,len(list)-1
    sum=0
    while left<right:
        sum=list[left]+list[right]
        if sum==target:
            return [left,right]
        elif sum>target:
            right-=1
        else:
            left+=1
    return []




# Get list input
numbers = [int(x) for x in input().split(",")]

# Get target number
target = int(input())
print("List:", numbers.sort)
print("Target:", target)
print(two_ptr_sum(numbers,target))
