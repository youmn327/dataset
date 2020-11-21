import vlc
import time


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
        current_track_number = self.track_number
        playlist_size = len(self.playlist)
        if current_track_number <= playlist_size and self.track_number - 1 < self.maximum:
            self.play_music()

    def next_song(self):
        self.play_music()

    def stop_music(self):
        print('음악을 정지합니다.')
        self.player.stop()


if __name__ == '__main__':
    tracks = {'우울' : ['https://r2---sn-n3cgv5qc5oq-bh2z7.googlevideo.com/videoplayback?expire=1605989910&ei=tiG5X62zIInC4wLbubbwDg&ip=1.229.96.174&id=o-ALt3wCBfa7yhapDxigKFwArOEjoQkgK1qNedLH01s9fk&itag=251&source=youtube&requiressl=yes&mh=9O&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2z7%2Csn-npoe7n7s&ms=au%2Conr&mv=m&mvi=2&pl=15&initcwndbps=1625000&vprv=1&mime=audio%2Fwebm&ns=xVDlzgnHNvLVCLdeSrlqwOkF&gir=yes&clen=5093601&dur=287.281&lmt=1586705539041211&mt=1605968196&fvip=2&keepalive=yes&c=WEB&txp=5531432&n=vf-bwvnGFLpWBqvR-&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgJIR60nViZYCboLkExl-MgWJGpt4oE-pRjYnVxWXgFl0CIQCDLyBWJu7lMvlsSVBWbxVDcURvvRSOVpZzw8NlvnweCQ%3D%3D&sig=AOq0QJ8wRAIgGsvKIP9ctftIPoK7yewIEWIOEermzifDqp4gmdsTlPACIGgAO8Ami5q8RKZrE7mJx_8VayzHoxCWdRnA13ZlfNhh&ratebypass=yes']}
    MP = Music_Player(tracks)
    MP.play_music()