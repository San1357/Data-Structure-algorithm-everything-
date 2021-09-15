class GFG:
    def solve(self, arr):
        print(self.res.add(tuple(arr))) # add current partitioning to result
        if len(arr)<=1:  # Base case when there is nothing to merge
            return
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i][::-1]: # When two adjacent such that one is reverse of another
                brr = arr[:i-1] + [arr[i-1]+arr[i]] + arr[i+1:]
                self.solve(brr)
            if i+1<len(arr) and arr[i-1]==arr[i+1][::-1]:  # All are individually palindrome,
              # when one left and one right of i are reverse of each other then we can merge
              # the three of them to form a new partitioning way
                brr = arr[:i-1] + [arr[i-1]+arr[i]+arr[i+1]] + arr[i+2:]
                self.solve(brr)
    def getGray(self, S):
        self.res = set()  # result is a set of tuples to avoid same partition multiple times
        self.solve(list(S)) # Call recursive function to solve for S
        return sorted(list(self.res))
# Driver Code
if __name__ == '__main__':
    ob = GFG()
    allPart = ob.getGray("geeks")
    for i in range(len(allPart)):
        for j in range(len(allPart[i])):
            print(allPart[i][j], end = " ")
        print()
# This code is contributed by Gautam Wadhwani
