class Marksheet:
    subjectList = []
    
    def addMarksAndSubject(self, subject, mark):

        for i in range(len(subject)):
            sub = {'subName': subject[i], 'mark': mark[i]}
            self.subjectList.append(sub)
    
    def calculatePercentage(self):

        result = 0
        for i in range(len(self.subjectList)):
            n = int(self.subjectList[i]['mark'])
            result += n
        percentage = result/len(self.subjectList)
        return percentage    
        
    def findDivision(self):
        #calculate the division on the basis of the percentage
        percentage = self.calculatePercentage()
        if percentage >= 80:
            print("Congratulations! You got Distinction.")
        elif percentage < 80 and percentage >=60:
            print("Congratulations! You got First Division.")
        elif percentage < 60 and percentage >= 50:
            print("Congratulations! You got Second Division.")
        elif percentage > 50:
            print("Congratulations! You got Third Division.")
        else:
            print("Sorry! No Division. Better luck next time.")


subject = []
mark = []
n = int(input("how many subjects?"))
for i in range(n):
    s = input("enter subject name: ")
    m = input("enter marks obtained: ")
    subject.append(s)
    mark.append(m)

std = Marksheet()
std.addMarksAndSubject(subject, mark)
p = std.calculatePercentage()
print("You have got {} %".format(p))
std.findDivision()