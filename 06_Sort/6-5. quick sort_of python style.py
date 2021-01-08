array = [7, 5, 9, 3, 4, 5, 6, 7, 8, 9, 1, 3, 0, 45]
print(f"before :: {array}")

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:] # all esle pivot

    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽부분

    # after part , each sort at left right , array list
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))