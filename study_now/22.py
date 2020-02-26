students = ['小明','小刚','小花']

for i in students:
    #students = students.append(students[i])
    students.append(i)
    del students[0]
    print(students)