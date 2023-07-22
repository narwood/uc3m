from course import *
from scraper import *


def printAll():
    with open('output.txt', 'w') as f:
        f.write("Name,Group,Times,Language,Hours\n")
        for row in getAllRows():
            for group in getGroups(row):
                course = createClass(row)
                f.write(course.name + "," + group.code + "," + group.dates.__str__() + "," + group.language + "," + course.hours + "\n")

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
                    f.write(course.name + "," + group.code + "," + group.dates.__str__() + "," + group.language + "," + course.hours + "\n")

def main():
    filt(['English'], ['Fri'], ['6'])
    print("Done")
    
if __name__ == '__main__':
    main()