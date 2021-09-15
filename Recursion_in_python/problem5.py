def remove(a):
    #basecase
    if not a:
        return ""

    if a[0] == "\t" or a[0] == " ":
        return remove(a[1:])
    else:
        return a[0] + remove(a[1:])

print(remove(" Hello\tWorld"))
print(remove(" Aayu sh"))
