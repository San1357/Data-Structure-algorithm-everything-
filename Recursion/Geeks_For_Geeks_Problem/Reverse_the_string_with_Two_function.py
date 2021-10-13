def reverse_main(string):
    return reverse_help(string,0)


def reverse_help(string, n):
    if n == len(string):
        return " " 
    return reverse_help(string, n+1) +string[n]


print(reverse_main("aayush"))
