from course import *
from scraper import *

def printRow(course, group, file):
    file.write(course.name + "," + group.code + "," + group.dates.__str__() + "," + group.language + "," + course.hours + "\n")

def printAll():
    with open('output.txt', 'w') as f:
        f.write("Name,Group,Times,Language,Hours\n")
        for row in getAllRows():
            for group in getGroups(row):
                course = createClass(row)
                printRow(course, group, f)

def filt(langList, daysList, hourList):
    with open('output.txt', 'w') as f:
        f.write("Name,Group,Times,Language,Hours\n")
        for row in getAllRows():
            for group in getGroups(row):
                course = createClass(row)
                dayFlag = True
                for day in daysList:
                    if day not in group.days():
                        dayFlag = False
                if (group.language in langList) and (course.hours in hourList) and dayFlag:
                    printRow(course, group, f)

def threeDayWeek():
    with open('output.txt', 'w') as f:
        for row in getAllRows():
            for group in getGroups(row):
                course = createClass(row)
                if 'Mon' not in group.days() and 'Fri' not in group.days() and course.hours == '3' and group.language == 'English':
                    printRow(course, group, f)


def main():
    #filt(['English'], ['Fri'], ['6'])
    threeDayWeek()
    print("Done")
    
if __name__ == '__main__':
    main()