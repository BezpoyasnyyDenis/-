class Student:
    
    def _init_(self,full_name = "", group_number = 0, progress = []):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress
    def __repr__(self):
                return repr(("Student: " + self.full_name + " Group: " + self.group_number))

    def set_full_name(self, full_name):
         self.full_name = full_name
    def set_group_number(self, group_number):
         self.group_numder = group_number
    def set_progress(self, progress):
        self.progress = progress

    def get_full_name(self):
         return self.full_name
    def get_group_number(self):
         return self.group_number

    def get_progress(self):
         return self.progress

st_size = 10
students = []
for i in range(st_size):
    st = Student()
    print("Впишіть ім'я: ")
    st.full_name = input()
    print("Впишіть номер групи: ")
    st.group_number = input()
    print("Введіть оцінку: ")
    st.progress = []
    for i in range(5):
        score = int(input()) 
        st.progress.append(score)
    students.appens(st)
print("Sorted students:")
for st in students:
    print(st)

students = sorted(students, key=lambda student: student.full_name)
print("Sorted students:")
for st in students:
    print(st)
