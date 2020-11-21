from face_detection import face_detect
from music_player import Music_Player
# from keras.models import load_model

face = face_detect("./file/haarcascade_frontalface_alt.xml")  # haarcascade_frontalface_alt 파일 경로
face.detect_face()

# model = load_model('저장한 트레인된 모델 경로')

mood = '우울' # 얼굴인식해서 표정을 에측한 후에 mood에 저장한다. (현재는 우울만)

##### vlc에 실행될 수 있게 유튜브 동영상 url 넣기 ####
tracks = {'우울': ['','']}


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

