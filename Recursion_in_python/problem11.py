#write a recursive function called reverse which accepts a string and returns a new string in reverse.
#string = 'aay'
def reverse(string):
    if len(string) == 0:
        return ''
    else:
        return string[-1] + reverse(string[:-1])

print(reverse('nohtyp'))