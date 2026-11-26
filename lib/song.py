class Song:
    """Represent a song and maintain in-memory library-wide totals."""

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    artist_count = artists_count

    def __init__(self, name, artist, genre):
        """Create a song and update the class-level aggregates."""
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total number of songs created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Record a genre once in the unique genre list."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Record an artist once in the unique artist list."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the number of songs recorded for a genre."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increment the number of songs recorded for an artist."""
        # Keep the original singular attribute working for existing lab tests.
        if cls.artist_count is not cls.artists_count:
            cls.artists_count = cls.artist_count
        cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1
        cls.artist_count = cls.artists_count
