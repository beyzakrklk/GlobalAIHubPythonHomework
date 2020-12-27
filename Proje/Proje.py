class Student:
    name =""

    surname =""
    course=[]
    course_not={}
    def __init__(self, studentName, studentSurname):
        self.name = studentName
        self.surname = studentSurname
    def course_kayit(self,course_name):
        self.course.append(course_name)
    def course_yazdir(self):
        for a in self.course:
            print(a)
    def course_not_gir(self):
         self.course_not["midterm"]=int(input("enter the midtherm: "))
         self.course_not["final"]=int(input("enter the final: "))
         self.course_not["project"]=int(input("enter the project: "))
        

student1=Student("Beyzanur","Karakulak")

nameSurnameControl=True

for i in range(3):
    enterName = input("Student name: ")
    enterSurname = input("Student surname: ")
    if student1.name == enterName and student1.surname == enterSurname:
        print("Welcome")
        nameSurnameControl=True
        break
    else:
        nameSurnameControl=False
       
if not nameSurnameControl:
    print("please try again later!")
    pass

else:
    courseNumber=int(input("Ders Sayısını giriniz: "))
    if(courseNumber<3):
        print("You failed in class")
    elif(3<=courseNumber<=5):
        for n in range(0,(courseNumber)):
            
            student1.course_kayit(input(f"{n+1}. kursun adını giriniz: "))
    else:
        print("You failed in class")
    control=1
    for i in student1.course:
        print(f"{control}-{i}")
        control+=1

    courseName=input("Kurs Seçin: ") 
    for i in student1.course:
        if(courseName==i):
            student1.course_not_gir()
    
    grade=student1.course_not["midterm"]*0.3+student1.course_not["final"]*0.5+student1.course_not["project"]*0.2
    if(grade>=90):
        print("AA İLE GEÇTİN")
    elif(70<=grade<90):
        print("BB İLE GEÇTİN")
    elif(50<=grade<70):
        print("CC İLE GEÇTİN")
    elif(30<=grade<50):
        print("DD İLE GEÇTİN")
    elif grade<30:
        print("FF İLE GEÇTİN")