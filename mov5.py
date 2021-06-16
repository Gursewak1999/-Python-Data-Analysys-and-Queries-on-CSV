import movies

print("Count the number of movies released in the year 1989 and duration is more than 1½ hours")
print("|Sr.No.| Name"+" "*(102- len("Name"))+"| Year | Rat  |Runtime|")

countPtr = 0;
for mov in movies.movieAr:
    if mov.year == 1989 and mov.runtime//60 > 90:
        print(mov.toString())
        countPtr=countPtr+1
print("Number of Movies : ",countPtr)
