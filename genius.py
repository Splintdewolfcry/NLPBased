from lyricsgenius import Genius
GENIUS_API_TOKEN='5gB4JnAcdN7RgiEPaJiKBIYapOLm5eJFASTT2t6gMinrKotehCol6JlLuf7xh1sk'
genius = Genius(GENIUS_API_TOKEN)

song = genius.search_song("Nocturama", "Nick Cave & the Bad Seeds")

with open('song_lyrics.txt', 'w+', encoding='utf-8') as file:
    file.writelines(f'{song.lyrics} + \n')