'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    length = len(arr)
    # for i in range(length-1):
    #     for checked_index in range(0, length-i-1):
    #         if arr[checked_index] == 0:
    #             arr[checked_index], arr[checked_index+1] = arr[checked_index+1], arr[checked_index]
    # return arr
    count = 0
    for i in range(length):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < length:
        arr[count] = 0
        count += 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")