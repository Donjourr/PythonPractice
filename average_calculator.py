"""
Create an average calculator
Students will have four subjects (Math, History, English, Science)
Scores will be inserted separated by space
if average is above 65, student will pass the semester
print whether the student pass the semester or not
"""


m,h,e,s = map(int, input().split()) # m for math, h for history, e for english, s for science
average = (m + h + e + s) / 4

print(average)
if average >= 65:
    print("This Student Passed this semester!")
else:
    print("This Student Failed")