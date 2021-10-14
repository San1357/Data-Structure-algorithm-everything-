def reverse(string):
    if string == "":
        return ""
    return string[-1]+ reverse(string[:-1])

print(reverse("aayush"))