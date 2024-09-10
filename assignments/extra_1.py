grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)

students.sort() 

my_dict = {}
for i in range(len(grades)):
    grade_avg = sum(grades[i])/len(grades[i])
    my_dict.update({students[i]:grade_avg})

print(my_dict)