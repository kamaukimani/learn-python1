print("Hello Album class!!!!")
class Album:
    GENRES=["Hip-hop","Pop","Jazz"]
    album_count=0
    def __init__(self,genre,date):
        if self.check_genre(genre):
            self.increase_album_count()
            self.genre=genre
            self.release_date=date
    @classmethod
    def check_genre(cls,genre):
        print("The genre is in the list of GENRES")
        return genre in cls.GENRES
    @classmethod
    def increase_album_count(cls,increment=1):
        cls.album_count +=increment
        print(f"We have {cls.album_count} album(s)")

album=Album("Pop","2024-01-01")
new_album=Album("Hip-hop","2024-01-01")
album_three=Album("Rock","2024-01-01")
