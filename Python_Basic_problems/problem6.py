#program to take in the marks of 5 subject & display the grade 

s1 = int(input("enter subject 1 marks out of 100"))
s2 = int(input("enter subject 1 marks out of 100"))
s3 = int(input("enter subject 1 marks out of 100"))
s4 = int(input("enter subject 1 marks out of 100"))
s5 = int(input("enter subject 1 marks out of 100"))
average = (s1 +s2 +s3 + s4 + s5)/5
if average >=90:
    print("Grade. A")
elif (average > 70 and average <90):
    print("Grade. B")
elif (average > 40 and average <= 70):
    print("Grade C")
else:
    print("Grade D")