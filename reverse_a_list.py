class Solution:
    #  Function to reverse an array
    def reverseArray(self, arr):
        # Get the length of the input array
        n = len(arr)

        # Create a new array of same size to store reversed elements
        ans = [0] * n

        # Start a loop to fill ans[] from the back of arr[]
        for i in range(n):
            # Place elements from the end of arr into the start of ans
            ans[i] = arr[n - 1 - i]

        # Return the reversed array
        return ans

# Driver code
if __name__ == "__main__":
    # Create an object of the Solution class
    obj = Solution()

    # Input array
    arr = [1, 2, 3, 4, 5]

    # Call the reverseArray function
    result = obj.reverseArray(arr)

    # Print the result
    print("Reversed Array:", result)