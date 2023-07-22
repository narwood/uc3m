from course import *
from scraper import *

class Main:

    def printAll():
        with open('output.txt', 'w') as f:
            f.write("Name,Group,Times,Language,Hours\n")
            for row in getAllRows():
                for group in getGroups(row):
                    #put condition here, indent two rows below in if block
                    if group.language == 'English':
                        course = createClass(row)
                        f.write(course.name + "," + group.code + "," + group.dates.__str__() + "," + group.language + "," + course.hours + "\n")
    
    def filter(langList, hourList, daysList):
        with open('output.txt', 'w') as f:
            f.write("Name,Group,Times,Language,Hours\n")
            for row in getAllRows():
                for group in getGroups(row):
                    course = createClass(row)
                    dayFlag = True
                    for day in group.days:
                        if day not in daysList:
                            dayFlag = False
                    if (group.language in langList) and (course.hours in hourList) and dayFlag:
                        f.write(course.name + "," + group.code + "," + group.dates.__str__() + "," + group.language + "," + course.hours + "\n")
    
    def main():
        #printAll()
        x = 2
        

    if __name__ == '__main__':
        printAll()