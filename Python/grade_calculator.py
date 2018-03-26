marks=input("Enter your marks: ")
marks=int(marks)
if marks==marks>=80 and marks<=100:
    grade='A+'
elif marks==marks>=70 and marks<=79:
    grade='A'
elif marks==marks>=60 and marks<=69:
    grade='A-'
elif marks==marks>=50 and marks<=59:
    grade='B'
elif marks==marks>=0 and marks<=49:
    grade='F'
elif marks>100:
    grade='none'
else:
    grade='none'
print("Your Grade is: ",grade)
