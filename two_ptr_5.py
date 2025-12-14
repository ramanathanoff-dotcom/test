#the maximum area of water that can be contained
#  between two lines represented by an array of heights.
def mx_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        h = min(height[left], height[right])
        width = right - left
        current_area = h * width
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


height=[int(x) for x in input().split(',')]
print(mx_area(height))
