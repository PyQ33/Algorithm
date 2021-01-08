array = [7, 5,9,3,4,5,6,7,8,9,1,3,0,45]
print(f"before :: {array}")

for i in range(0, len(array)):
    for j in range(i, 0, -1): # index will be munus from i to 1
        if array[j] < array[j-1]: # left 1 move
            array[j], array[j-1] = array[j-1], array[j]

        else:
            break
            
print(f"after :: {array}")