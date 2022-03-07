

# x  = input()
x = input()
y = x[::-1]
count = 0
for i in range(len(y) // 2):
    if x[i].isalpha():
        count = count +1
    


print(count - 1)