def find_students_with_second_lowest_grade():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    students = []
    for i in range(n):
        name = data[2*i + 1]
        grade = float(data[2*i + 2])
        students.append((name, grade))
    unique_grades = sorted(set(grade for name, grade in students))
    second_lowest_grade = unique_grades[1]
    second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
import sys
from io import StringIO
sample_input = """5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""
sys.stdin = StringIO(sample_input)
find_students_with_second_lowest_grade()
