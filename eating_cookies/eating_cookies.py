'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # Your code here
#     #Runtime is O(3^n)
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

# the cache allows us to save our work
# can be a dictionary where keys = n, value = the answer
# def eating_cookies(n, cache):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     # check if the answer is in our cache
#     elif cache[n] > 0:
#         return cache[n]
#     else:
#         #otherwise cache doesn't contain answer, so we'll continue our recursive logic
#         #save the answer in our cache for future use
#         cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
#         return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
