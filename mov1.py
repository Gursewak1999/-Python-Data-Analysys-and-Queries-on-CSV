import movies

print("List of Movie Names and rating of all Movies with rating > 4.3")
print("|Sr.No.| Name"+" "*(102- len("Name"))+" |  Rat  |")

for mov in movies.movieAr:
    if(mov.rating>4.3):
        print(mov.printe(_n=1, _ra=1))
