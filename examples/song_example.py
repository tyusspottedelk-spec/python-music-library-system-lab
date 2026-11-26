from lib.song import Song

Song("Nights", "Frank Ocean", "R&B")
Song("Ivy", "Frank Ocean", "R&B")

print(f"Total songs: {Song.count}")
print(f"Genres: {Song.genres}")
print(f"Artists: {Song.artists}")
print(f"Songs by genre: {Song.genre_count}")
print(f"Songs by artist: {Song.artists_count}")
