student_height = input().split()
_sum = 0
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
    _sum = student_height[n] + _sum

average = round(_sum / len(student_height), 2)
print(f"The average height is:{average} ")
