num_of_students = int(input())
dict = {}

for _ in range(num_of_students):
    data = tuple(input().split())
    student, grade = data
    if student not in dict:
        dict[student] = []
    dict[student].append(float(grade))

for student_name, gr in dict.items():
    print(f"{student_name} -> {' '.join(f'{grades:.2f}' for grades in gr)} (avg: {(sum(gr) / len(gr)):.2f})")

