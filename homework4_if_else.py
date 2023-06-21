"""
Homework4.

Description:
    we have four values w,x,y,z
    write if-elif-else statement that will search minimum value
    and print smth aka "'y' is minimum value"
    advice use python debugger and different values to check your algorithm

"""

w, x, y, z = 300, 200, 40, 300

if w <= x and w <= y and w <= z:
    minimum_value = 'w'
elif x <= w and x <= y and x <= z:
    minimum_value = 'x'
elif y <= w and y <= x and y <= z:
    minimum_value = 'y'
else:
    minimum_value = 'z'
print(minimum_value, 'is minimum value')
