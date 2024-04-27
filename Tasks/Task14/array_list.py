'''
This script creates an Album class with attributes album_name, number_of_songs, album_artist.
The script employs various sorting of the list of albums and searching at the end
'''

class Album:
    # initialising class
    def __init__(self, album, num_songs, artist):
        self.album_name = album
        self.number_of_songs = num_songs
        self.album_artitst = artist

    def __str__(self) -> str:
        return f'({self.album_name}, {self.album_artitst}, {self.number_of_songs})'

# creating instances of album class
happy = Album('Happy', 5, 'Denison Clark')
mega = Album('Mega', 8, 'Carey Wilson')
dance = Album('Dance', 3, 'K2 Plast')
avid = Album('Avid', 7, 'D2 Dilli')
century = Album('Century', 4, 'Harper May')

# list of all instances of album
album1 = [happy, mega, dance, avid, century]

# print out all albums in list album1
for x in  album1:
    print(x)

print('\n')
# print out sorted list of albums according to their number of songs
for x in sorted(album1, key=lambda album: album.number_of_songs):
    print(x)

print('\n')
# swap element at position 1 with element at position 2 and print it
album1[0], album1[1] = album1[1], album1[0]
for x in album1:
    print(x)

# Album2 creation
bar = Album('Bar', 7, 'Harry Pyles')
tame = Album('Tame', 3, 'Niko Logby')
revenge = Album('Revenge', 9, 'Bandy L')
heavy = Album('Heavy', 5, 'M2 Dilli')
money = Album('Money', 6, 'Nick Toss')

# creating album2
album2 = [bar, tame, revenge, heavy, money]
print('\n')

# printing album2
for x in album2:
    print(x)

# copy all albums in album1 into album2
album2 += album1

# add two additoinal albums to album2
album2.append(Album('Dark Side of the Moon', 9, 'Pink Floyd'))
album2.append(Album('Oops!... I Did It Again', 16, 'Britney Spears'))

# sort albums by album name alphabetically and print out
print('\n')
for x in sorted(album2, key = lambda album: album.album_name):
    print(x)

# search for album 'Dark Side of the Moon' and print out index
print('\n')
for i,x in enumerate(album2):
    if x.album_name == 'Dark Side of the Moon':
        print(f'"{x.album_name}" is found at index {i}')