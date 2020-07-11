""" using sort() """

# details of 3 students - name, rollnumber and marks/100 in order
students = [ ['stud1', 12333, 44],\
			['stud3', 4534534, 78,], \
			['stud2', 63435, 65] ]

students.sort() # by default, algorithm takes 1st key, i.e name as key to sort
print(students)

roll = lambda stud: stud[1]

students.sort(key=roll, reverse=True) # sort in descending order with roll number as key
print(students)
