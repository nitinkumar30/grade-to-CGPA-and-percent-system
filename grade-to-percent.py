dic={'D':4,'C2':5,'C1':6,'B2':7,'B1':8,'A2':9,'A1':10}   # declaration of grade to percent range. You can change as per the rule.

n=int(input("Enter number of subjects: "))  # Subject number may change so asking to input number of subjects
count=0
for i in range(n):
    marks = input("Enter grade of Subject: ")  # asking user to input the grade. It should be uppercase letter & not lowercase.
    if marks in dic:
        count = count + dic[marks]
print("Total CGPA approximate is",round((count/n),2),'.')   # This is the output screen to showcase the approximate CGPA.
print("Total percent approximate is",round((count/n),2)*9.5,'.')   # This is the output screen to showcase the approximate percentage
