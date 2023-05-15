class Student:
    def __init__(self, email, name, surname, allgrade=None, status=None):
        self.all_grade = allgrade
        self.email = email
        self.name = name
        self.surname = surname
        self.status = status

    def __str__(self):
        return "Email: " + self.email + "\nName: " + self.name + "\nSurname: " + self.surname + "\nAll grades: " + str(
            self.all_grade) + "\nStatus: " + str(self.status)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.email == other.email

    def __repr__(self):
        return self.__str__()

    # bierze najlepsze z prac domowych i je sumuje
    def getSumOfHighestHomeworks(self, amount=1):
        if amount > 3:
            print("Niepoprawna wartość!")
            return 0
        gradelist = [int(self.all_grade["l_1"]), int(self.all_grade["l_2"]), int(self.all_grade["l_3"])]
        gradelist.sort(reverse=True)

        highsum = 0
        for i in range(amount):
            highsum += gradelist[i]

        return highsum

    def getHomeWorkPoints(self):
        if self.all_grade is not None:
            homeworksum = 0
            validhomeworkcounter = 0

            if self.all_grade['h_1'] != -1:
                homeworksum += int(self.all_grade['h_1'])
            validhomeworkcounter += 1

            if self.all_grade['h_2'] != -1:
                homeworksum += int(self.all_grade['h_2'])
            validhomeworkcounter += 1

            if self.all_grade['h_3'] != -1:
                homeworksum += int(self.all_grade['h_3'])
            validhomeworkcounter += 1

            if self.all_grade['h_4'] != -1:
                homeworksum += int(self.all_grade['h_4'])
            validhomeworkcounter += 1

            if self.all_grade['h_5'] != -1:
                homeworksum += int(self.all_grade['h_5'])
            validhomeworkcounter += 1

            if self.all_grade['h_6'] != -1:
                homeworksum += int(self.all_grade['h_6'])
            validhomeworkcounter += 1

            if self.all_grade['h_7'] != -1:
                homeworksum += int(self.all_grade['h_7'])
            validhomeworkcounter += 1

            if self.all_grade['h_8'] != -1:
                homeworksum += int(self.all_grade['h_8'])
            validhomeworkcounter += 1

            if self.all_grade['h_9'] != -1:
                homeworksum += int(self.all_grade['h_9'])
            validhomeworkcounter += 1

            if self.all_grade['h_10'] != -1:
                homeworksum += int(self.all_grade['h_10'])
            validhomeworkcounter += 1

            return homeworksum
        else:
            return -1

    def getProjectPoints(self):
        if self.all_grade is not None:
            return int(self.all_grade["project"])
        else:
            return -1

    def checkIfAllGrades(self):
        return int(self.all_grade["project"]) != -1 \
            and int(self.all_grade["l_1"]) != -1 \
            and int(self.all_grade["l_2"]) != -1 \
            and int(self.all_grade["l_3"]) != -1

    def getStatus(self):
        return self.status

    def addGrade(self, newgrade):
        if self.all_grade is not None:
            self.all_grade["grade"] = newgrade

    def changeStatus(self, newstatus):
        self.status = newstatus

    @staticmethod
    def compareStudentsNames(x, y):
        return x.name >= y.name

    @staticmethod
    def compareStudentsSurname(x, y):
        return x.surname >= y.surname

    @staticmethod
    def compareStudentsEmail(x, y):
        return x.email >= y.email

    @staticmethod
    def getPersonalData(self):
        return self.email, self.name, self.surname
