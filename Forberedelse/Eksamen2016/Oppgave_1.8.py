arr = [4, 2, 7, 3, 8, 4]
e = 0

for i in range(len(arr)):
    if arr[i] > 5:
        e += arr[i]
    else:
        e += 1

print(e)

# Output
# 19