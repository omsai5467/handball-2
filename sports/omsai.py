# arr=[-12, 11, -13, -5, 6, -7, 5, -3, 11]

arr = [1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1]
left = 0
right = 0
while left <len(arr) and right <len(arr):
       if(arr[right]<0):
              arr[right],arr[left] = arr[left],arr[right]
              left = left + 1
       right  =right + 1

print(arr)