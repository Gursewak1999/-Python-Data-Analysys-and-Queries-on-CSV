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

    def toArray(self):
        ar = []
        ar.append(self.fname)
        ar.append(self.lname)
        ar.append(self.email)
        return ar
        
    def equals(self, obj1):
        if self.fname == obj1.fname:
            if self.lname == obj1.lname:
                if self.email == obj1.email:
                    return True
        return False


attendees1 = []
resultant  = []

with open("data/attendees1.csv") as at1:
     csv_reader = csv.reader(at1, delimiter=",")
     for row in csv_reader:
         #print(row[0], row[1], row[2])
         attendees1.append(ppl(row[0], row[1], row[2]));

with open("output/result.csv","w", newline='') as result:
    csv_reader = csv.writer(result)
    for people1 in attendees1:
        if people1.fname.startswith("A") and people1.email.startswith("a"):
            csv_reader.writerow(people1.toArray())
