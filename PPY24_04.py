import smtplib
from email.mime.text import MIMEText

import LinkedList
import Stack
import Student


def emailStudents(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()


myList = LinkedList.LinkedList()

myList.add_node("bbbbb")
myList.add_node("aaaa")
myList.add_node("cccc")

print("Lista po dodaniu elementów:")
print(myList)

myList.delete("aaaa")

print("Lista po usunięciu elementów:")
print(myList)

studentLinkedList = LinkedList.LinkedList()
studentList = []
filepath = "students0.txt"

with open(filepath) as file_object:
    for line in file_object:
        x = line.rstrip().split(",")

        if len(x) == 3:
            studentList.append(Student.Student(x[0], x[1], x[2]))
        elif len(x) == 18 or len(x) == 19:
            selfgrade = {
                "project": x[3],
                "l_1": x[4],
                "l_2": x[5],
                "l_3": x[6],
                "h_1": x[7],
                "h_2": x[8],
                "h_3": x[9],
                "h_4": x[10],
                "h_5": x[11],
                "h_6": x[12],
                "h_7": x[13],
                "h_8": x[14],
                "h_9": x[15],
                "h_10": x[16],
                "grade": x[17],
            }
            if len(x) == 19:
                studentList.append(Student.Student(x[0], x[1], x[2], selfgrade, x[18]))
            else:
                studentList.append(Student.Student(x[0], x[1], x[2], selfgrade))
        else:
            print("Niepoprawny obiekt!")

for student in studentList:
    studentLinkedList.add_node(student, Student.Student.compareStudentsSurname)

print(studentLinkedList)

print("Co chcesz zrobic z danymi studentow?")
while True:
    print("Wybierz |grade| aby wpisac oceny lub |email| aby wyslac mail do studentow z wybranym statusem")

    command = input("Wpisz komende")

    if command == "grade":

        print("Ok, ocenianie studentow w toku")
        for studenttmp in studentList:
            if studenttmp.checkIfAllGrades():
                homeworksum = studenttmp.getHomeWorkPoints()
                allpoints = 0
                if homeworksum >= 80:
                    allpoints += 60
                elif homeworksum >= 70:
                    allpoints += 40
                    allpoints += studenttmp.getSumOfHighestHomeworks(1)
                elif homeworksum >= 60:
                    allpoints += 20
                    allpoints += studenttmp.getSumOfHighestHomeworks(2)
                else:
                    allpoints += studenttmp.getSumOfHighestHomeworks(3)

                allpoints += int(studenttmp.all_grade["project"])

                if allpoints < 50:
                    studenttmp.addGrade(2)
                elif 60 >= allpoints >= 51:
                    studenttmp.addGrade(3)
                elif 70 >= allpoints >= 61:
                    studenttmp.addGrade(3.5)
                elif 80 >= allpoints >= 71:
                    studenttmp.addGrade(4)
                elif 90 >= allpoints >= 81:
                    studenttmp.addGrade(4.5)
                else:
                    studenttmp.addGrade(5)
                studenttmp.changeStatus("GRADED")
        break
    elif command == "email":

        print("Ok, rozpoczynam emailowanie")
        newStatus = input("Podaj status dla ktorego wyslac maile")

        for studenttmp in studentList:
            if studenttmp.getStatus() == newStatus:
                emailtemp = studenttmp.email
                gradetemp = studenttmp.all_grade["grade"]

                emailStudents("Ocena", f"Twoja ocena z przedmiotu PPY to {gradetemp}",
                              "dummy@gmail.com", emailtemp, "temppass")

                studenttmp.changeStatus("MAILED")
        break
    else:
        print("Niepoprawna komenda!")

print(studentList)
print("+====================================================================================")
print(studentLinkedList)
