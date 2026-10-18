
#this file is genorated by mahdi Ahmed
#the perpeus is all about cleaning our Dataset to train a Machin learning model       #######
#the simple programe wroted here in this file is about to separate the main csv file into two parts the first one has all the missing valeus for special tratment and the second don't
#the steps i think that am going to take is :                                         #######
# - importing the data into a perfect data structer                                   #######
# - removing the repeated/related columns so we can prevent the redendency            #######
# - looking for any repeated students "rows" to elemenate                             ####### here in some where i need to ceparate the date into training/testing parts
# - start the cleaning proccess by fill the missing values as possibol as we can      ####### and i don't know with what to start at first devaid the data or clean it first ?
# - take decisions about the outlayers and how to deal with them

import csv
#the step
with open("./Dataset/student_performance_updated_1000.csv", "r") as file :
    # students = csv.reader(file)
    # next(students)
    students = csv.DictReader(file)




    students = list(students) ### this in so helpfull at the second with statment becouse students as a csv.DictReader dose not work after this block cloased
    # for student in students :
    #     # print(type(student))  ## --> this one show that student in a object of dictionary class
    #     print(student)  ### here after printing the values of student i can say that students is  a list of dictionarys
    #     print(student.keys())  # in here with using the keys() method with the

    # student in students   // dose'nt work'

    # print(students.keys()) # why this line dont display the dictionary keys?? -- i got the answer after printing the type and values of the student object i find that i was looking at the students as a big global dictionary and it is not
                             # now  i see it as a list of dictionarys

    # print(type(students)) --> csv.DictReader


    ##### -1 Filtering rows that contain missing values

with open("./filtred dataset - step1/without_missing_values.csv" , "w") as file , open("./filtred dataset - step1/with_missing_values.csv" , "w") as file2:
    
    field_Names = ["StudentID","Name","Gender","AttendanceRate","StudyHoursPerWeek","PreviousGrade","ExtracurricularActivities","ParentalSupport","FinalGrade","Study Hours","Attendance (%)","Online Classes Taken"]

    without_M = csv.DictWriter(file,field_Names)
    without_M.writeheader()
    with_M = csv.DictWriter(file2,field_Names)
    with_M.writeheader()



    for student in students :
        if '' in student.values() :
            with_M.writerow(student)
        else :
            without_M.writerow(student)






