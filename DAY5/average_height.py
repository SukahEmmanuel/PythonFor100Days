student_heights = input("Input a list of student heights ").split()
height_counter = 0
sum_of_height = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    height_counter = height_counter + 1
    sum_of_height += student_heights[n]
print(student_heights)
print(height_counter)
print(sum_of_height)
average_height = sum_of_height / height_counter
print(f"The average of the heights is {round(average_height)}")