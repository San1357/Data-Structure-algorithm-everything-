def reverse(string):
    if string == "":
        return ""
    else:
        return string[-1] + reverse(string[ : -1])


print(reverse("a"))
