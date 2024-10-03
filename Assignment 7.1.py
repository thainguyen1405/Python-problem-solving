#Thai Nguyen, Assignment 7.1
import csv

# open tsv file using the csv reader
with open("StudentInfo.tsv") as file:
    tfile = csv.reader(file, delimiter="\t")

    #Find the grade
    def score_avg():
        if avg >=90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >=70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        elif avg < 60:
            grade = 'F'

        return grade
        
    #Create a 1st row line
    row1 = next(tfile)
    avg = int(row1[2])+int(row1[3])+int(row1[4])
    avg = avg/3.0
    row1.append(score_avg())

    #Create a 2nd row line
    row2 = next(tfile)
    avg = int(row2[2])+int(row2[3])+int(row2[4])
    avg = avg/3.0
    row2.append(score_avg())

    #Create a 3rd row line
    row3 = next(tfile)
    avg = int(row3[2])+int(row3[3])+int(row3[4])
    avg = avg/3.0
    row3.append(score_avg())

    #Create a 4th row line
    row4 = next(tfile)
    avg = int(row4[2])+int(row4[3])+int(row4[4])
    avg = avg/3.0
    row4.append(score_avg())

    #Create a 5th row line
    row5 = next(tfile)
    avg = int(row5[2])+int(row5[3])+int(row5[4])
    avg = avg/3.0
    row5.append(score_avg())

#Calculate the midterm and final score
row6 = ['Averages:']
midterm1 = int(row1[2])+int(row2[2])+int(row3[2])+int(row4[2])+int(row5[2])
midterm1 = "%.2f" % (midterm1/5)

midterm2 = int(row1[3])+int(row2[3])+int(row3[3])+int(row4[3])+int(row5[3])
midterm2 = "%.2f" % (midterm2/5)

final = int(row1[4])+int(row2[4])+int(row3[4])+int(row4[4])+int(row5[4])
final = "%.2f" % (final/5)

#Create a new line for the calculation
row6.append("midterm1 "+str(midterm1)+",")
row6.append("midterm2 "+str(midterm2)+",")
row6.append("final "+str(final))

#Convert list to string
def listToString(s):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(s))
       
#Print the code 
print(listToString(row1))
print(listToString(row2))
print(listToString(row3))
print(listToString(row4))
print(listToString(row5))
print("")
print(listToString(row6))

