from lyricsgenius import Genius

GENIUS_API_TOKEN='5gB4JnAcdN7RgiEPaJiKBIYapOLm5eJFASTT2t6gMinrKotehCol6JlLuf7xh1sk'
genius = Genius(access_token=GENIUS_API_TOKEN)
LYRICS_FILE = 'song_lyrics.txt'

# song = genius.search_song("Carmen", "George Bizet")
# song = genius.search_song("Caruso", "Lucio Dalla")
# song = genius.search_song("Tu vas me détruire", "Daniel Lavoie")

def search_the_song(song_itself, artist):
    return genius.search_song(song_itself, artist)

def write_song_lyrics(song_itself, artist, file=LYRICS_FILE):
    with open(file, 'w', encoding='utf-8') as lyrics:
        lyrics.writelines(search_the_song(song_itself, artist).lyrics)
    
def read_and_print_lyrics(file=LYRICS_FILE):
    with open(file, 'r', encoding='utf-8') as lyrics:
        file = lyrics.read()
        file = file.split(' Lyrics', 1)[-1]
        file = file.split('You might also likeEmbed', 1)[0]
        print(file)

        with open(LYRICS_FILE, "w", encoding='utf-8') as f:
            print(file, file=f)

def lyrics_bit(song_itself, artist):
    write_song_lyrics(song_itself, artist)
    read_and_print_lyrics()

try:
    print("""
[1]Carmen by George Bizet
[2]Caruso by Lucio Dalla
[3]Tu vas me détruire by Daniel Lavoie (Beni Mahvedeceksin)
[4]Farklı bir şarkı
            """)

    print("1, 2, 3 veya 4'e basın")

    user_input = input("Seçiminiz: ")
    if user_input == '':
        lyrics_bit("Caruso", "Lucio Dalla")
    
    if user_input == "1":
        lyrics_bit("Carmen", "George Bizet")

    if user_input == "2":
        lyrics_bit("Caruso", "Lucio Dalla")
    
    if user_input == "3":
        lyrics_bit("Tu vas me détruire", "Daniel Lavoie")
    
    if user_input == "4":
        song_name = input("Şarkının ismi nedir? + \n")
        artist_name = input("Sanatçının ismi nedir? + \n")

        lyrics_bit(song_name, artist_name)
except:
    raise ValueError("Şarkı bulunamadı")

# lyrics_bit(song=song_input, artist=artist_input)
