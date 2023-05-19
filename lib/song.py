class Song:
    count = 0
    genres = set()
    artists = {}
    genre_count = {}
    artist_count={}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artists:
            cls.artists[artist] += 1
        else:
            cls.artists[artist] = 1

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    def add_to_artist_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist]+=1
        else:
            cls.artist_count[artist]=1
    # @classmethod
    # def show_name(cls):
    #     print(cls.genres)
    #     print(cls.artists)
    #     print(cls.genre_count)


# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
# one_prob = Song("1 Problems", "Jay-Zu", "Rap")
# two_prob = Song("2 Problems", "Jay-Zu", "Hip Hop")

# print(Song.count)
# Song.show_name()
