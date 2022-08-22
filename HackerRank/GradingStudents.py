def gradingStudents(grades):
    rounded_grades = []
    for i in grades:
        next_multiple = (((i//5)+1)*5)
        if i < 38:
            rounded_grades.append(i)

        elif (next_multiple - i ) < 3:
            rounded_grades.append(next_multiple)
        else:
            rounded_grades.append(i)
    return rounded_grades

print(gradingStudents(grades=[73, 67, 38, 33]))