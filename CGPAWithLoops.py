print("\n\t Program To Calculate CGPA")
n=int(input("Enter the total number of papers: "))
GradeSum=0
TotalCredit=0
for i in range(0,n):
    grade=int(input("Enter Your Grade: "))
    credit=float(input("Enter the credit: "))
    GradeSum=GradeSum+(grade*credit)
    TotalCredit+=credit
CGPA=GradeSum/TotalCredit
print("Your CGPA is: ",CGPA)
