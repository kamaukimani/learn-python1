print("The Song class..........")
class Song:
    all=[]
    def __init__(self,name):
        self.name=name
        print(self)
        Song.add_song_to_all(self)
    @classmethod
    def add_song_to_all(cls,song):
        cls.all.append(song)
    @classmethod
    def show_song_names(cls):
        #print(list(cls.all))
        print([song.name for song in cls.all])

ninety_nine_problems=Song("99 problems")
thriller=Song("Thriller")
Song.show_song_names()