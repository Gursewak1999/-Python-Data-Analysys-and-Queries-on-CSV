import movies

print("List the movie names and release year of all movies released before 1990 and do not have a null in the rating")
print("|Sr.No.| Name"+" "*(102- len("Name"))+"| Year | Rat  |")

print(type(movies.movieAr[0].year))
for mov in movies.movieAr:
    if (mov.year < 1990) and not ( mov.rating == float(0)):
        print(mov.printe(_n=1, _y=1, _ra=1))
