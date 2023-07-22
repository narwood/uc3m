from bs4 import BeautifulSoup
import re
from course import *

with open("classes.html", errors='ignore') as f:
    soup = BeautifulSoup(f, 'html.parser')


def getAllRows():
    return soup.find_all(class_="filaPadre")

def createClass(row):
    code = row.contents[3].text
    name = row.contents[5].contents[1].text.strip()
    year = row.contents[7].text
    program = row.contents[9].text.strip()
    hours = row.contents[13].text[0:1]
    groups = getGroups(row)
    return Course(code, name, year, program, hours, groups)

def getGroups(row):
    groups = []
    for group in row.next_sibling.next_sibling.contents[3].find_all(class_="grupos")[1::]:
        code = group.tbody.contents[1].contents[5].text
        language = group.tbody.contents[5].contents[3].contents[1].a['title']
        dates = getDates(group)
        groups.append(Group(code, language, dates))
    return groups

def getDates(group):
    dates = []
    for date in group.tbody.contents[1].contents[7].table.tbody.contents[5].td.table.tbody.contents[1::2]:
        day = getDay(date)
        time = getTime(date)
        dates.append(Date(day, time))
    return dates

def getDay(date):
    return date.contents[1].text.strip()

def getTime(date):
    return date.contents[3].text.strip()

def main():
    print(getDay(getDates(getGroups()[0])[0]))

if __name__ == "__main__":
    main()