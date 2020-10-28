import xlsxwriter
import csv

file = open('hacuGradList.txt')

schools=[]

for line in file:
    stuff = line.split()

    # handles the lines with State and Acronym only
    if len(stuff) is 2:
        state=stuff[0]
        #print(state)
        continue

    # skips any blank lines
    if len(stuff) is 0:
        continue

    #skips over the summary lines of each state, which have 6 elements
    if len(stuff) is 6:
        continue


    if (len(stuff)> 7):
        school= {}
        ipos= line.find('4')
        jpos=line.find(';')
        university=line[0:jpos]
        city=line[jpos+2:ipos].rstrip()

        # building each school key value pair

        school['name']=line[0:jpos]
        school['city']=city
        school['state']=state
        school['sector']=stuff[(len(stuff)-5)]
        school['totalGradStudents']=stuff[(len(stuff)-4)]
        school['totalHispanicGradStudents']=stuff[(len(stuff)-3)]
        school['graduateHispanicPercentage']=stuff[(len(stuff)-2)]
        school['undergraduateHispanicPercentage']=stuff[(len(stuff)-1)]

        schools.append(school)

        print(school)

#writeToFile

filename='hacuGradSchools.csv'
with open(filename, 'w') as f:
    w=csv.DictWriter(f,['name', 'city', 'state', 'sector', 'totalGradStudents', 'totalHispanicGradStudents', 'graduateHispanicPercentage', 'undergraduateHispanicPercentage'])
    w.writeheader()
    for school in schools:
        w.writerow(school)
