'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    for i in arr:
        if i == 0:
            print(f'IF--> i: {i}')
            print(arr)
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(f'i after next: {i}')
        else:
            print(f'Else--> i: {i}')
            arr[i] = arr[i]
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")