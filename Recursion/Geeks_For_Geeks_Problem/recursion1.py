def recursion(n):
    if n < 4 : # General Case
        print(n, "Start")
        recursion(n+1)
        print(n, "End")
    else:  #base case
        print(n, "Start")
        print(n, "End")

recursion(0)
