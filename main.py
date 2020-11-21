from face_detection import face_detect
from music_player import Music_Player
# from keras.models import load_model

face = face_detect("./file/haarcascade_frontalface_alt.xml")  # haarcascade_frontalface_alt 파일 경로
face.detect_face()

# model = load_model('저장한 트레인된 모델 경로')

mood = '우울' # 얼굴인식해서 표정을 에측한 후에 mood에 저장한다. (현재는 우울만)

##### vlc에 실행될 수 있게 유튜브 동영상 url 넣기 ####
tracks = {'우울': [
    'https://r2---sn-n3cgv5qc5oq-bh2z7.googlevideo.com/videoplayback?expire=1605989910&ei=tiG5X62zIInC4wLbubbwDg&ip=1.229.96.174&id=o-ALt3wCBfa7yhapDxigKFwArOEjoQkgK1qNedLH01s9fk&itag=251&source=youtube&requiressl=yes&mh=9O&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2z7%2Csn-npoe7n7s&ms=au%2Conr&mv=m&mvi=2&pl=15&initcwndbps=1625000&vprv=1&mime=audio%2Fwebm&ns=xVDlzgnHNvLVCLdeSrlqwOkF&gir=yes&clen=5093601&dur=287.281&lmt=1586705539041211&mt=1605968196&fvip=2&keepalive=yes&c=WEB&txp=5531432&n=vf-bwvnGFLpWBqvR-&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgJIR60nViZYCboLkExl-MgWJGpt4oE-pRjYnVxWXgFl0CIQCDLyBWJu7lMvlsSVBWbxVDcURvvRSOVpZzw8NlvnweCQ%3D%3D&sig=AOq0QJ8wRAIgGsvKIP9ctftIPoK7yewIEWIOEermzifDqp4gmdsTlPACIGgAO8Ami5q8RKZrE7mJx_8VayzHoxCWdRnA13ZlfNhh&ratebypass=yes',
    'https://r2---sn-n3cgv5qc5oq-bh2sr.googlevideo.com/videoplayback?expire=1605990800&ei=MCW5X76sKMG-qAG-86SIAg&ip=1.229.96.174&id=o-AOO_UhLroLzXGpPgWD6iPS4LqhwbwTaSz7wb4662Vzv5&itag=251&source=youtube&requiressl=yes&mh=6h&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2sr%2Csn-npoeenek&ms=au%2Conr&mv=m&mvi=2&pl=15&gcr=kr&initcwndbps=1590000&vprv=1&mime=audio%2Fwebm&ns=ybGMkx5HMEMlQyKa4zLw_v4F&gir=yes&clen=5588675&dur=314.361&lmt=1574980067401665&mt=1605968916&fvip=2&keepalive=yes&c=WEB&txp=5531432&n=TWnUzPFa-xANua48y&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgaqe2umYJdUIa0_kSIIj3B_e0Cc3YnO1VlWDX6Jau8RcCIASEnlq4JoWhLxt7rSSKGvVt58j5CpkL5Osui6l5VDjg&sig=AOq0QJ8wRQIhAOyDf-caDzo6fOT-GP6hDHgD-xNzahckm85wegTBBkqLAiBlrhuSKOV2Sv7pSv5o7Z-u0V4OfUbQPS2jefy2eJw3vg==&ratebypass=yes']}


# 노래 틀어주기 (현재 우울밖에 없습니다.)
if mood == '우울':
    check = input('음악을 듣겠습니까? (예/아니오) : ')
    if check == '예':
        while True:
            input_ = input('음악 조정하기 : (실행/다음 음악/중지) ')
            player = Music_Player(tracks, mood=mood)

            if input_ == '실행':
                player.play_music()
            elif input_ == '다음 음악':
                player.stop_music()
                player.next_song()
            elif input_ == '중지':
                player.stop_music()
                break

