# Exercise 8-7: Album
def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album
print(make_album('Pink Floyd', 'The Dark Side of the Moon'))
print(make_album('Tame Impala', 'Currents'))
print(make_album('Radiohead', 'OK Computer', 12))
