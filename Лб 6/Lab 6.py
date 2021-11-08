class Student:

    def __init__(self, name = "", group_number = 0, progress = []):
        self.name = name
        self.group_number = group_number
        self.progress = progress
    def __repr__(self):
                return repr(("Студент: " + self.name + "Група: " + self.group.number))

    def set_name(self, name):
        self.name = name
    def set_group_number(self, group_number):
        self.group_number = group_number
    def set_progress(self, progress):
        self.progress = progress

    def get_name(self):
        return self.name
    def get_group_number(self):
        return self.group_number
    def get_progress(self):
        return self.progress

st_size = 10
students = []
for i in range(st_size):
    st = Student()
    print("Введіть ім'я та прізвище: ")
    st.name = input()
    print("Введіть номер групи: ")
    st.group_number = input()
    print("Введіть оцінку: ")
    st.progress = []
    for i in range(5):
        score = int(input())
        st.progress.append(st)
print("Відсортовані студенти: ")
for st in students:
    print(st)

students = sorted(students , key = lambda student: student.name)
print("Відсортовані студенти: ")
for st in students:
    print(st)
    