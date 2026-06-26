'''Problem 4: Second Largest Number'''
arr = [10, 20, 5, 40, 30]
first = second = float('-inf')
for i in arr:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i
print(second)