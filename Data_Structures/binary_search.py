def binary_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
def verify(index):
    if index is not None:
        print("target found at: ", index)
    else:
        print("target not found in the list")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 12)
verify(result)        
result = binary_search(numbers, 6)
verify(result)  
        