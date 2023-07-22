class Course:

    def __init__(self, code, name, year, program, hours, groups):
        self.code = code
        self.name = name
        self.year = year
        self.program = program
        self.hours = hours
        self.groups = groups

    def __str__(self):
        return str(self.code) + "," + self.name + "," + str(self.year) + ", " + self.program + ", " + str(self.hours) + "/n" + self.groups.__str__()

    def inEnglish(self) -> bool:
        for group in self.groups:
            if group.inEnglish:
                return True

class Group:

    def __init__(self, code, language, dates):
        self.code = code
        self.language = language
        self.dates = dates

    def inEnglish(self) -> bool:
        return self.language == 'English'
    
    def days(self):
        r = []
        for date in self.dates:
            r.append(date.day)
        return r
    
    def __str__(self):
        return str(self.code) + ", " + self.language + ", " + self.dates.__str__()

class Date:

    def __init__(self, day, time):
        self.day = day
        self.time = time

    def __repr__(self):
        return self.day + ": " + self.time