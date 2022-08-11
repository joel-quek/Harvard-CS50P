def song_decoder(song):
    x = song.replace("WUB", "")
    phrase = ""
    for word in x:
        phrase = phrase + " " + str(word)

    phrase = phrase.strip()
    return phrase 