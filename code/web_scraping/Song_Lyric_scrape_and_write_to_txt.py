def lyrics_from_song(artist, song):
    song_title_intermediate = song.replace("'", "")
    song_title = '-'.join(song_title_intermediate.split())
    artist_name_intermediate = artist.replace("'", "")
    artist_name = '-'.join(artist_name_intermediate.split())
    page_url = "http://genius.com/" + artist_name + "-" + song_title + "-lyrics"
    page = requests.get(page_url)
    html = BeautifulSoup(page.text, "html.parser")
    [h.extract() for h in html('script')]
    lyrics=html.find("div", class_="lyrics").get_text()
    lyrics = re.sub("[\(\[].*?[\)\]]", "", lyrics)
    return lyrics

outF = open("artist5_song5.txt", "w")
outF.write(lyricsA)
outF.close()