import datetime
import csv
import os
class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname = None):
        self.surname = surname
        self.first_name = first_name
        if nickname is not None:
            self.nickname = nickname
        else:
            pass
        self.birth_date = birth_date.split('-')
        self.birth_date = datetime.date(int(self.birth_date[0]), int(self.birth_date[1]), int(self.birth_date[2]))
        self.toDay = 0
        self.fullname = 0
        self.date = 0
        self.year = 0
        self.month = 0
        self.day = 0
        self.age = 0
    def get_fullname (self):
        self.fullname = self.surname + ' ' + self.first_name
        return self.fullname

    def get_age (self):
        self.toDay = datetime.date.today()
        self.age = self.toDay.year - self.birth_date.year
        if self.toDay.month < self.birth_date.month:
            self.age -= 1
        elif self.toDay.month == self.birth_date.month and self.toDay.day < self.birth_date.day:
            self.age -= 1
        else:
            pass
        return str(self.age)
def modifier (filename):
    with open(filename, 'r') as data:
        read_file = csv.DictReader(data)
        with open('temp', 'w') as temp:
            titles = read_file.fieldnames[:]
            titles.insert(3, 'fullname')
            titles.append('age')
            write_file = csv.DictWriter(temp, fieldnames=titles)
            write_file.writeheader()
            for row in read_file:
                surname = row['surname']
                name = row['name']
                birth_date = row['birthdate']
                nickname = row['nickname'] or None
                person = Person(surname, name, birth_date, nickname)
                row['fullname'] = person.get_fullname()
                row['age'] = person.get_age()
                write_file.writerow(row)
    temp.close()
    data.close()
    os.rename('temp', filename)
modifier('data.csv')
