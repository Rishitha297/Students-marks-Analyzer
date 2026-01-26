# Student Marks Analyzer

subjects = int(input("Enter number of subjects: "))
total = 0

for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total += marks

percentage = total / subjects

print("\n--- Results ---")
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")
