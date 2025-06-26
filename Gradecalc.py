subjects = [
    ("Introduction to Data Science", 4),
    ("Programming in Python", 3),
    ("R Programming and Math for AI", 3),
    ("Computer Organization and Architecture", 4),
    ("Probability and Statistics", 4),
    ("Software Lab III", 2)
]

total_credits=0
total_weighted_points=0

print("\nSemester 3 SGPA Calculator")
print("Enter marks out of 5 (A+ = 5, A = 4.5, B+ = 4, B = 3.5, C+ = 3, C = 2.5, D = 2, E = 0)")

for name, credit in subjects:
    print("\n",name ,"(Credits:",credit,")")
    int1=float(input(" Internal 1 Grade Point: "))
    int2 = float(input(" Internal 2 Grade Point: "))
    endsem = float(input("End Semester Grade Point: "))

    internal_avg = (int1+int2)/ 2
    final_gp = (internal_avg*1+endsem* 3)/ 4
    total_weighted_points+= final_gp* credit
    total_credits+= credit

sgpa = total_weighted_points / total_credits
print("\n Your Semester 3 SGPA is:",sgpa)