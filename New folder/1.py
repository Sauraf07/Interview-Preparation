'''Problem 1: Find Duplicate Elements'''
nums = [1,2,3,4,5,1,6,2]
seen = set()
dublicate = set()
for num in nums:
    if num in seen:
        dublicate.add(num)
    else:
        seen.add(num)
print(list(dublicate))