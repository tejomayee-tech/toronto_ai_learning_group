class Student:

    def __init__(self,name):
        self.name = name
        self.marks = []

    def add_marks(self,mark):
        self.marks.append(mark)

    def calculate_average(self):
        total_marks = sum(self.marks)
        count = len(self.marks)
        avarage = total_marks/count
        return avarage
    
    def grade_student(self):
        avg = self.calculate_average()

        for index,mark in enumerate(self.marks):
            print(f"{index+1} subject - marks {mark}")
        
        # for mark in self.marks:
        #     print(f"marks {mark}")

        if avg > 70 and avg < 80:
            print(f"{self.name} is awared grade B")
        elif avg > 81 and avg <= 90:
            print(f"{self.name} is awared grade A")
        elif avg >= 91:
            print(f"{self.name} is awared grade E")
        else:
            print(f"{self.name} is awared grade C")


Student_v = Student("vijay")
Student_v.add_marks(60)
Student_v.add_marks(55)
Student_v.add_marks(70)
Student_v.add_marks(75)
vijay_avg_marks = Student_v.calculate_average()
print(f"Student Vijay had average marks of : {vijay_avg_marks}")
Student_v.grade_student()

Student_m = Student("Mahesh")
Student_m.add_marks(90)
Student_m.add_marks(99)
Student_m.add_marks(100)
Student_m.add_marks(89)
Mahesh_avg_marks = Student_m.calculate_average()
print(f"Student Mahesh had average marks of : {Mahesh_avg_marks}")
Student_m.grade_student()