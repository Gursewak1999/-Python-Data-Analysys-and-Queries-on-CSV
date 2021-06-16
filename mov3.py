import movies

print("List the movie names and rating of all movies in which movie name contains the word “boys” or the word “wild”")
print("|Sr.No.| Name"+" "*(102- len("Name"))+"| Rat  |")

for mov in movies.movieAr:
    if "boys" in mov.name or "wild" in mov.name:
        print(mov.printe(_n=1, _ra=1))
