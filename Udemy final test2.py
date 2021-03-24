s_grades = [['Robin',95],['Justin',88],['Leo',96],['Kevin',80]
        ,['Tom',65],['Sunny',72],['Zack',92]]


only_score = [i[1]for i in s_grades]
only_score = sorted(only_score,reverse=True)
second_high = only_score[1]

second_high_student = [i[0]for i in s_grades
                        if i[1] == second_high]

for result in second_high_student:
    print(result)


