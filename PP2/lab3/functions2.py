movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
########### 1 task
def imdb_above(imdb):
    if imdb > 5.5:
        return True
    return False

print(f"imdb > 5.5: {imdb_above(movies[7]["imdb"])}")
print("----------------------------------")
#####################
# 2 task
def list_above(movies):
    for movie in movies:
        if movie["imdb"] > 5.5:
            print(movie["name"])
    

print("Sublist of movies that imdb above 5.5:")
list_above(movies)
print("----------------------------------")
###################
# 3 task
def categorycheck(needed_category, movies):
    for movie in movies:
        if needed_category == movie["category"]:
            print(movie["name"])

needed_category = "Suspense"
print(f"Movies under {needed_category} category: ")
categorycheck(needed_category, movies)
#####################
# 4 task
print("----------------------------------")
def average_imdb(movies):
    sum = 0
    count = 0
    for movie in movies:
        sum += movie["imdb"]
        count += 1
    return sum / count

print(f"The average IMDB score: {average_imdb(movies)}")
print("----------------------------------")
############################
# 5 task
def category_avg(needed_category, movies):
    sum = 0
    count = 0
    for movie in movies:
        if movie["category"] == needed_category:
            sum += movie["imdb"]
            count += 1
        
    return sum / count

needed_category = "Thriller"
print(f"The average IMDB score of {needed_category} category: {category_avg(needed_category, movies)}")