import csv

class ppl:
    
    fname = ""
    lname = ""
    email = ""

    def __init__(self, v1, v2, v3):
        self.fname = v1
        self.lname = v2
        self.email = v3

    def print(self):
        print("| "+self.fname," "*(10 - len(self.fname))+
              "|", self.lname," "*(10 - len(self.lname))+
              "|", self.email," "*(30 - len(self.email))+"|")
               
        
    def equals(self, obj1):
        if self.fname == obj1.fname:
            if self.lname == obj1.lname:
                if self.email == obj1.email:
                    return True
        return False


attendees1 = []
attendees2 = []

with open("data/attendees1.csv") as at1:
     csv_reader = csv.reader(at1, delimiter=",")
     for row in csv_reader:
         #print(row[0], row[1], row[2])
         attendees1.append(ppl(row[0], row[1], row[2]));

with open("data/attendees2.csv") as at2:
     csv_reader = csv.reader(at2, delimiter=",")
     for row in csv_reader:
         #print(row[0], row[1], row[2])
         attendees2.append(ppl(row[0], row[1], row[2]));

    
print("The list of all the people who attended the second bash and not the first.")
print("_"*60)
print("| First Name | Last Name  |"+" email"+" "*(30 - len(" email"))+" |")
print("_"*60)
for people1 in attendees2:
    for people2 in attendees1:
        if people1.equals(people2):
            people1.print()
print("_"*60)
