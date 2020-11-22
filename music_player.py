import vlc
import time
import collections

class Music_Player:
    def __init__(self, playlist, mood='우울'):
        self.instance = vlc.Instance('--verbose 0')
        self.playlist = playlist
        self.maximum = len(self.playlist[mood])
        self.track_number = -1
        self.mood = mood
        self.current_music = None

    def play(self, url):
        self.player = self.instance.media_player_new()
        media = self.instance.media_new(url)
        media.get_mrl()
        self.player.set_media(media)
        self.player.play()

        time.sleep(5)
        event_manager = self.player.event_manager()
        event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.end_callback)


    def play_music(self):
        self.track_number += 1
        if self.track_number < self.maximum:
            self.current_music = self.playlist[self.mood][0]
            music = self.playlist[self.mood].pop()

            self.play(music)

    def end_callback(self, event):
        if self.track_number - 1 < self.maximum:
            self.play_music()

    def next_song(self):
        self.play_music()

    def stop_music(self):
        print('음악을 정지합니다.')
        self.player.stop()

    def is_music_playing(self):
        return self.player.is_playing()

if __name__ == '__main__':
    tracks = {'우울' : ['','']}
    MP = Music_Player(tracks)
    MP.play_music()
