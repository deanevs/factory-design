

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def song_serialize(self, ser):
        ser.start_object('song', self.song_id)
        ser.add_property('title', self.title)
        ser.add_property('artist', self.artist)






