# Exercise 8-8: User Albums
def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

while True: 
    print("\nPlease enter the artist and title of the album:")
    print("(enter 'q' at any time to quit)")
    artist = input("Artist: ")
    if artist == 'q':
        break
    title = input("Title: ")
    if title == 'q':
        break
    print(make_album(artist, title))
