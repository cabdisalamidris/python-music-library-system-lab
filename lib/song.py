class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """Initialize a Song instance with name, artist, and genre."""
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call class methods to update class attributes
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        """Increment the total count of songs."""
        Song.count += 1

    def add_to_genres(self):
        """Add genre to the genres list if it doesn't exist."""
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        """Add artist to the artists list if it doesn't exist."""
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        """Update genre_count dictionary for this song's genre."""
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        """Update artist_count dictionary for this song's artist."""
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1
