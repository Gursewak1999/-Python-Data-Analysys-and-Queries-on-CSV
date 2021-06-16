import csv

class movie:
    serial = 0
    name = ""
    year = 1900
    rating = 0.0
    runtime = 0000

    def __init__(self, row):
        #print(type(self.rating))
        if(row[0] == ""):
            self.serial = 0
        else:
            self.serial = int(row[0])
        
        self.name = (row[1])
        
        if row[2]=="":
            self.year = 0
        else:
            self.year = int(row[2])

        if row[3] == "":
            self.rating = float(0)
        else :
            self.rating = float(row[3])

        if row[4] == "":
            self.runtime = 0
        else:
            self.runtime = int(row[4])
		#print(type(self.rating))
	
    def general(self):
        self.rat=""
        self.serial = ""
        self.year = ""
        self.runtime =""
        
        if(self.serial == 0):
            self.serial = ""
        else:
            self.serial = str(self.serial)

        if self.year == 0:
            self.year = ""
        else:
            self.year = str(self.year)

        if self.runtime == 0:
            self.runtime = ""
        else:
            self.runtime = str(self.runtime)
            
        if self.rating == 0.0:
            self.rat="0"
        else:
            rat = str(self.rating)
	
    def toString(self):
        self.general()
        string = "| "+self.serial+" "*(5-len(self.serial))+"| "+self.name  +" "*(50-len(self.name))+"| "+self.year  +" |"+self.rat+" "*(3)+"| "+self.runtime+" "*(6-len(self.runtime))+" |"
        return string
    
    def printe(name=0,year=0, rating=0, runtime=0):
	self.general(self)
	toPrint = "| "+self.serial+" "*(5-len(self.serial))
	if name==1:
            toPrint=toPrint+"| "+self.name  +" "*(50-len(self.name))
	if year==1:
            toPrint=toPrint+"| "+self.year
	if rating==1:
            toPrint=toPrint+" |"+self.rat+" "*(3)
	if runtime==1:
            toPrint=toPrint+"| "+self.runtime+" "*(6-len(self.runtime))
        toPrint=toPrint+" |"			
	return toPrint;
	
        
movieAr = []

with open("data/dataset-movies.csv") as dataset:
    csv_read = csv.reader(dataset, delimiter=",")
    for row in csv_read:
        movieAr.append(movie(row))
		
		
