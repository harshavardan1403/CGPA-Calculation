print("\n\t Program To Calculate CGPA")
print("\nSelect among the following options in lower case")
print('a: Only Grade and Credits')
print('b: GPA of first two semester and Grades of Third Sem')
print('c: GPA of  All semester')
selection=input("Enter the Options among the above: ")
if selection=="a":
    n=int(input("Enter the total number of papers: "))
    GradeSum=0
    TotalCredit=0
    for i in range(0,n):
        grade=float(input("Enter Your Grade: "))
        credit=float(input("Enter the credit: "))
        GradeSum=GradeSum+(grade*credit)
        TotalCredit+=credit
    CGPA=GradeSum/TotalCredit
    print("\n\nYour CGPA is: ",CGPA)
elif selection=="b":
    sem1=float(input("Enter your GPA in first semester: "))
    Total_Credit_In_Sem1=float(input("Enter the total credit in first sem: "))
    sem2=float(input("Enter your GPA in second semester: "))
    Total_Credit_In_Sem2=float(input("Enter the total credit in second sem: "))
    n=int(input("Enter the total number of papers: "))
    GradeSum=0
    TotalCredit=0
    for i in range(0,n):
        grade=float(input("Enter Your Grade: "))
        credit=float(input("Enter the credit: "))
        GradeSum=GradeSum+(grade*credit)
        TotalCredit+=credit
    WholeCredit=(sem1*Total_Credit_In_Sem1)+(sem2*Total_Credit_In_Sem2)+GradeSum
    TotalCredit=TotalCredit+Total_Credit_In_Sem1+Total_Credit_In_Sem2
    CGPA=WholeCredit/TotalCredit
    print("\n\nYour CGPA is: ",CGPA)
else:
    sem1=float(input("Enter your GPA in first semester: "))
    Total_Credit_In_Sem1=float(input("Enter the total credit in first sem: "))
    sem2=float(input("Enter your GPA in second semester: "))
    Total_Credit_In_Sem2=float(input("Enter the total credit in second sem: "))
    sem3=float(input("Enter your GPA in third semester: "))
    Total_Credit_In_Sem3=float(input("Enter the total credit in third sem: "))
    GradeSum=(sem1*Total_Credit_In_Sem1)+(sem2*Total_Credit_In_Sem2)+(sem3*Total_Credit_In_Sem3)
    TotalCredit=Total_Credit_In_Sem1+Total_Credit_In_Sem2+Total_Credit_In_Sem3
    CGPA=GradeSum/TotalCredit
    print("\n\nYour CGPA is: ",CGPA)
