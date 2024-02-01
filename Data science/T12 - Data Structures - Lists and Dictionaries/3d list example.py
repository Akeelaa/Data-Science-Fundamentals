data_3D = [
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ],        
    [
        [13,14,15],
        [16,17,18]
    ]
]
total_sum = 0
for layer in data_3D:
    for row in layer:
        for value in row:
            total_sum += value

for i in range (10):
    total_sum += i
    if i == 5:
        print(f"breaking the loop at i = {i}")
        break

print(f"total sum is {total_sum}")
