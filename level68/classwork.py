class Movie:
    def __init__(self,movieTitle,director,year):
        self.movieTitle=movieTitle
        self.director=director
        self.year=year

    @classmethod
    def display_info(cls,movie):
        print(f"Movie: {movie.movieTitle}")
        print(f"Director: {movie.director}")
        print(f"Year: {movie.year}")

movie1=Movie("Inception","Christopher Nolan",2010)
Movie.display_info(movie1)

#2

class Profile:
    def __init__(self,username, creationDate):
        self.username=username
        self.creationDate=creationDate

    @staticmethod
    def get_user(username,creationDate):
        print(f"Username: {username}")
        print(f"Creation date: {creationDate}")

profile1=Profile("luka","2026-10-08")
Profile.get_user(profile1.username,profile1.creationDate)