import json
import cv2
import numpy
import time
import csv
# from keras.models import load_model

#############################################
from face_detection import face_detect
from music_player import Music_Player
from weather import Weather_Api
#############################################

# model = load_model('저장한 트레인된 모델 경로')
# mood = model.predict('img')

FACE = face_detect("./file/haarcascade_frontalface_alt.xml")  # haarcascade_frontalface_alt 파일 경로
WTH = Weather_Api()

file = open('exp_weather', 'w', encoding='UTF-8')
wr = csv.writer(file)

cap = cv2.VideoCapture("./file/video1.mp4") # 비디오 경로


while True:
    success, img = cap.read()
    if not success:
        break
    faces, flag = FACE.detect_face(img)
    for person in faces:
        pass

    if flag == True:
        mood = '우울'  # 얼굴인식해서 표정을 에측한 후에 mood에 저장한다. (현재는 우울만)
        with open("./file/data_file.json", 'r', encoding='UTF-8') as file:
            data = json.load(file)

        if abs(FACE.base_time - FACE.current_time) % 60 == 0:
            current_weather = WTH.get_current_weather()
            wr.writerow([mood, current_weather])

        # 노래 틀어주기 (현재 우울밖에 없습니다.)
        if mood in data['tracks']:
            check = input('음악을 듣겠습니까? (예/아니오) : ')
            if check == '예':
                player = Music_Player(data['tracks'], mood=mood)
                while True:
                    input_ = input('음악 조정하기 (실행/다음 음악/중지) : ')

                    if input_ == '실행':
                        player.play_music()
                    elif input_ == '다음 음악':
                        player.stop_music()
                        player.next_song()
                    elif input_ == '중지':
                        if not player.is_music_playing():
                            break
                        player.stop_music()
                        break
