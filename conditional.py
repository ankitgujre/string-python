# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible for vote.")
# else:
#     print("You are not eligible for vote.")

marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A", marks)
elif marks >= 75 and marks < 90:
    print("Grade B", marks)
elif marks >= 65 and marks < 75:
    print("Grade C", marks)

else:
    print("Fail")