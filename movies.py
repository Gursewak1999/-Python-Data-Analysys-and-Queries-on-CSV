import csv


class movie:

    serial = 0
    name = ''
    year = 1900
    rating = 0.0
    runtime = 0

    def __init__(self, row):

        # print(type(self.rating))

        if row[0] == '':
            self.serial = 0
        else:
            self.serial = int(row[0])

        self.name = row[1]

        if row[2] == '':
            self.year = 0
        else:
            self.year = int(row[2])

        if row[3] == '':
            self.rating = float(0)
        else:
            self.rating = float(row[3])

        if row[4] == '':
            self.runtime = 0
        else:
            self.runtime = int(row[4])

        # print(type(self.rating))

    def general(self):
        self._rat = ''
        self._serial = ''
        self._year = ''
        self._runtime = ''

        if self.serial == 0:
            self._serial = '----'
        else:
            self._serial = str(self.serial)

        if self.year == 0:
            self._year = '----'
        else:
            self._year = str(self.year)

        if self.runtime == 0:
            self._runtime = '----'
        else:
            self._runtime = str(self.runtime)

        if self.rating == 0.0:
            self.rat = '0.0'
        else:
            self.rat = str(self.rating)

    def toString(self):
        self.general()
        string = '| ' + self._serial + ' ' * (5 - len(self._serial)) \
            + '| ' + self.name + ' ' * (102- len(self.name)) + '| ' \
            + self._year + ' |' + self.rat + ' ' * 3 + '| ' \
            + self._runtime + ' ' * (6 - len(self._runtime)) + ' |'
        return string

    def printe(self, _n=0,_y=0,_ra=0,_ru=0):
        self.general()
        toPrint = '| ' + self._serial + ' ' * (5 - len(self._serial))
        if _n == 1:
            toPrint = toPrint + '| ' + self.name + ' ' * (102- len(self.name))
        if _y == 1:
            toPrint = toPrint + '| ' + self._year
        if _ra == 1:
            toPrint = toPrint + ' |' + self.rat + ' ' * 3
        if _ru == 1:
            toPrint = toPrint + '| ' + self._runtime + ' ' * (6 - len(self._runtime))
        toPrint = toPrint + ' |'
        return toPrint


movieAr = []

with open('data/dataset-movies.csv') as dataset:
    csv_read = csv.reader(dataset, delimiter=',')
    for row in csv_read:
        movieAr.append(movie(row))
