import movies

print("List all movie names and release year for the movie names beginning with ‟A” and rating is null and release year is not between 1980 and 1995.")
print("|Sr.No.| Name"+" "*(102- len("Name"))+"| Year |")

for mov in movies.movieAr:
    if mov.name.startswith("A") and mov.rating == 0 and mov.year not in range(1980-1,1995):
        print(mov.printe(_n=1, _y=1))
