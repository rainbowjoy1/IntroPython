# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 17:41:57 2021

@author: danie
"""
class University:
    distinct_threshold=-1
    #this variable is keeping track of how many courses a student needs to get 
    #a 4/5 on an assignment and still pass with distinction. It starts at a -1 
    #because the first course will always be the 5/5 requirement
    grade_threshold=0
    #this variable keeps track of how many courses are registered. This way 
    #graduation can be determined no matter how many registered courses
    def __init__(self):
        self.studentlist=[]
        self.coursecatelog=[]
    #the University class here has no need for data (outside of list initilization)
    #in the constructor because I only have one University
    def new_student(self, fname, lname):
        #I chose to make the new student function in the university because 
        #new students are created at the university level and so that the operator 
        #would have to run less code
        student=Student(fname,lname)
        self.studentlist.append(student)
        for course in self.coursecatelog:
            course.add_student(student)
            #this for loop is important so that it can go through each course thats created
            #and create a student list so we can ensure that all students are enrolled
        return student

    def remove_student(self, student):
        self.studentlist.remove(student)
        for course in self.coursecatelog:
            course.delete_student(student)
        print("Student",student,"has been unenrolled and removed from the course catelog and their grades have been deleted.")
    
    def find_student_by_id(self, studentid):
        for student in self.studentlist:
            if (student.id==studentid):
                return student
        return None   
    #This code is what allows me to search for a student by studentid and return the Student object
    
    def new_course(self, coursename):
        course=Course(coursename)  
        self.coursecatelog.append(course)
        University.distinct_threshold+=1
        University.grade_threshold+=1 
        for student in self.studentlist:
            course.student_register.append(student)
            course.grade_book.add_student(student)
        print("You have added",coursename,"into the course catelog. All current students have been enrolled and students now must pass one additional class to graduate.")
        return course
        #creating courses at the university enrolls all registered students, adjusts
        #counts and creates new gradebooks
    
    def remove_course(self, course):
        self.coursecatelog.remove(course)
        University.distinct_threshold-=1
        University.grade_threshold-=1
        for student in self.studentlist:
            course.delete_student(student)
        print("You have removed",course,"from the course catelog. Student have been unenrolled and gradebooks have been deleted. Students now need one less course to graduate with distinction and one less to graduate")
    
    def graduate(self):
        print("Graduation Status:")
        #here I am checking if every student has graduated on the fly. I do not 
        #store P/F for the course but instead analyze each student
        for student in self.studentlist:
            countofpass=0
            distinction_perfect=False
            distinction_almost=0
            #all these variables allow me to keep track of if someone graduated
            #and if someone graduated with distinction 
            print(student.fname, student.lname, end="")
            for course in self.coursecatelog:
                x=course.number_of_passed_assignments(student)
                if x==5:
                    distinction_perfect=True
                    distinction_almost+=1
                if x==4:
                    distinction_almost+=1
                if x>=3:
                    countofpass+=1
            if countofpass >= University.grade_threshold:
                print(" has graduated ",end="")
            else: 
                print(" has failed",end="")
            if distinction_perfect==True and distinction_almost >= University.distinct_threshold:
                print("and with distinction!",end="")
            print()
        
            #help again
    def coursePF(self):
        print("Course Status:")
        for student in self.studentlist:        
            print(student.fname, student.lname, end="\n")
            for course in self.coursecatelog:
                x=course.number_of_passed_assignments(student)
                if x>=3:
                    print("Passed:",course)
                else: 
                    print("Failed:", course)
                    
class Student:
    id_counter=111111
    #my id counter is keeping track of the student id 
    def __init__(self, fname, lname):
        if len(fname)<2 or len(lname)<2:
            raise Exception("Names must have more than one charecter")
        if fname.isalpha()==0 or lname.isalpha()==0:
            raise Exception("Names cannot contain special charecters or numbers")
        else:
            self.fname, self.lname = fname, lname
            self.studentid = Student.id_counter
            Student.id_counter+=1
            print("You have registered ", fname," ",lname,". Their student ID is: ", self.studentid,sep='')
    def __eq__(self, o):
        if isinstance(o,Student):
            return self.studentid == o.studentid
        return False
    def __str__(self):
        return self.fname+" "+self.lname
    def __hash__(self):
        return hash((self.fname, self.lname, self.studentid))
    def __repr__(self):
        return self.fname+" "+self.lname
    #because I want to search for students to return information I had to 
    #create an Equality statement
    
    
class Course:
    def __init__(self,course_name):
        if isinstance(course_name,str):
            self.student_register=[]
            #creating a course automatically creates a list. This is where 
            #registered students will populate
            self.course_name=course_name
            self.grade_book=GradeBook()
        else:
            raise Exception("Course names must be strings. Thay can contain any charecters or length.")
    def __repr__(self):
        return self.course_name
    def __eq__(self, o):
        if isinstance(o, Course):
            return self.coursename == o.coursename
        #Same equality statement that was needed in the Student class so that I 
        #can look up a course and remove it
    def __str__(self):
        return self.course_name
    def add_student(self, student):
        self.student_register.append(student) 
        self.grade_book.add_student(student)
    def delete_student(self, student):
        self.student_register.remove(student)
        self.grade_book.delete_student(student)
    def grade(self, student, grades):
        self.grade_book.grade(student, grades)
    def number_of_passed_assignments(self, student):
        return self.grade_book.num_passed(student)
    def print_gradebook(self):
        print(self.course_name,":")
        self.grade_book.print_gradebook()

            
class GradeBook:
    def __init__ (self):
        self.grade_book={}
    def add_student(self, student):
        self.grade_book[student]=()
    def grade(self, student, grades):
        #grading checks that its all a list and correct terminology and records it
        if isinstance(grades, list) and len(grades)==5:
            for letter in grades:
                if letter!="P" and letter!= "F":
                    raise Exception('Grades can only be entered at "F" or "P"')
            self.grade_book[student]=grades
            print("Grades:",self.grade_book[student], "have been entered for", student.fname)     
        else:
            raise Exception("Grades must be entered as a list []. 5 assignments in length.")
    def print_gradebook(self):
        for student in self.grade_book:
            print('Gradebook:',student.fname, student.lname, self.grade_book[student])
    def delete_student(self,student):
        del self.grade_book[student]
    def num_passed(self,student):
        pflist=self.grade_book[student]
        if len(pflist)==0:
            raise Exception("Grades are not entered for",student)
        else:
            passcount=0
            for entry in pflist:
                if entry=="P":
                    passcount+=1
            return passcount
  
m=University()
ppc=m.new_course("Python Programing Course")
vac=m.new_course("Visual Analytics Course")
dmml=m.new_course("Data Mining and Machine Learning")

a=m.new_student("Bamse","Krea")
b=m.new_student("Kylling","Krea")
c=m.new_student("John","Jacob")
d=m.new_student("Peter","Piper")
e=m.new_student("Aurora","Beauty")
f=m.new_student("Cinder","Ella")
g=m.new_student("Hemli","Helicopter")
h=m.new_student("Bluey","Heeler")
i=m.new_student("Daniel","Tiger")
j=m.new_student("Prince","Wednesday")
k=m.new_student("Baby","Shark")
l=m.new_student("Rapunzel","Frisør")

tac=m.new_course("Text Analytics Course")

ppc.grade(a,["P","F","P","F","P"])
ppc.grade(b,["P","P","F","P","P"])
ppc.grade(c,["F","P","P","P","P"])
ppc.grade(d,["F","P","F","P","P"])
ppc.grade(e,["F","P","F","P","P"])
ppc.grade(f,["F","P","F","F","P"])
ppc.grade(g,["F","P","F","F","P"])
ppc.grade(h,["F","P","F","F","P"])
ppc.grade(i,["P","P","F","F","P"])
ppc.grade(j,["P","P","F","P","P"])
ppc.grade(k,["P","P","F","F","P"])

vac.grade(a,["P","P","P","P","P"])
vac.grade(b,["P","P","F","F","P"])
vac.grade(c,["P","P","F","F","P"])
vac.grade(d,["P","P","P","P","P"])
vac.grade(e,["P","P","F","F","P"])
vac.grade(f,["F","F","F","F","F"])
vac.grade(g,["P","P","P","P","P"])
vac.grade(h,["P","F","P","F","F"])
vac.grade(i,["P","P","P","P","P"])
vac.grade(j,["P","P","P","P","F"])
vac.grade(k,["P","P","P","P","F"])

dmml.grade(a,["F","P","P","P","P"])
dmml.grade(b,["F","P","F","F","P"])
dmml.grade(c,["P","P","F","F","P"])
dmml.grade(d,["P","P","F","P","P"])
dmml.grade(e,["P","P","F","F","P"])
dmml.grade(f,["P","P","P","P","P"])
dmml.grade(g,["P","P","F","P","P"])
dmml.grade(h,["P","P","F","P","P"])
dmml.grade(i,["F","P","P","P","P"])
dmml.grade(j,["F","P","F","P","P"])
dmml.grade(k,["F","P","F","P","P"])

tac.grade(a,["P","P","P","P","P"])
tac.grade(b,["P","F","P","F","F"])
tac.grade(c,["P","P","P","P","P"])
tac.grade(d,["P","P","P","P","F"])
tac.grade(e,["P","P","P","P","F"])
tac.grade(f,["F","F","F","F","F"])
tac.grade(g,["P","P","P","P","P"])
tac.grade(h,["P","P","F","F","P"])
tac.grade(i,["P","P","F","F","P"])
tac.grade(j,["P","P","P","P","P"])
tac.grade(k,["P","P","F","F","P"])

#m.graduate()

vac.grade(l,["F","F","F","F","F"])
ppc.grade(l,["P","P","P","P","P"])
dmml.grade(l,["F","P","F","F","P"])
tac.grade(l,["F","F","F","F","F"])

ppc.print_gradebook()
tac.print_gradebook()
vac.print_gradebook()
dmml.print_gradebook()

m.graduate()

m.remove_course(ppc)

m.graduate()

m.remove_student(h)

m.coursePF()
m.graduate()
