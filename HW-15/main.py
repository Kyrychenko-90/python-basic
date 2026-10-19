from student import Student
from group import Group, GroupFullException

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)

test_group = Group('PD2')

for i in range(10):
    student = Student('Male', 20, f'Name{i}', f'Surname{i}', f'AN{i}')
    test_group.add_student(student)

try:
    test_group.add_student(st1)
except GroupFullException as e:
    print(e)