# Write a function that returns True if there is a Pythagorean triplet that satisfies a^2+ b^2 = c^2. 
# sqaure all elements
# sort the array
# two loops
    # outer loop start with the largest number acting as c^2, moves backwards to the second element
    # inner loop start with the second largest number acting as b^2, moves backwards to the first element
    # find a
# use set to store values
# check if minus of the value match the values in the set, if so return true

def checkTriplet(array):
    n = len(array)
    for i in range(n):
        array[i] = array[i]**2

    array.sort()

    for i in range(n - 1, 1, -1):
        s = set()
        for j in range(i - 1, -1, -1):
            if (array[i] - array[j]) in s:
                return True
            s.add(array[j])
    return False


arr = [3, 2, 4, 6, 5]
arr2 = [10, 4, 6, 12, 5] 
print(checkTriplet(arr), checkTriplet(arr2))
# True, false

# Time complexity
# Squaring and sorting: O(nlogn)
# Outer and Inner Loops: O(n^2)
# Set Operations: O(1) per insertion and lookup.
# Overall time complexity: O(n^2)

# Space complexity
# O(n)
