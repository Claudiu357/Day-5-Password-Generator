student_height = input().split()
max_score = 0
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
    if student_height[n] > max_score:
        max_score = student_height[n]

print(f"The max score is:{max_score} ")
