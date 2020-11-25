import json
import cv2
import csv
import numpy as np
from collections import defaultdict
from keras.models import load_model

#############################################
from face_detection import face_detect
from music_player import Music_Player
from weather import Weather_Api

#############################################

model = load_model('./file/save_model1.h5')

FACE = face_detect("./file/haarcascade_frontalface_alt.xml")  # haarcascade_frontalface_alt 파일 경로
WTH = Weather_Api()

face_expression = ['화남', '역겨움', '무서움', '행복', '무표정', '우울', '놀람']
face_expression_cnt = defaultdict(int)

cap = cv2.VideoCapture("./file/video.mp4")  # 비디오 경로

while True:
    success, img = cap.read()
    if not success:
        break
    faces, flag = FACE.detect_face(img)
    for person in faces:
        # cv2.imshow('person', person)
        person = np.asarray(person)
        person = person.astype('float32') / 255.0
        person = np.array([person])
        mood = face_expression[model.predict(person).argmax()]
        face_expression_cnt[mood] += 1
        # cv2.waitKey(1)

    if flag:
        mood = max(face_expression_cnt, key=lambda key: face_expression_cnt[key])
        # 얼굴인식해서 표정을 에측한 후에 mood에 저장한다.
        with open("./file/data_file.json", 'r', encoding='UTF-8') as file:
            data = json.load(file)

        file = open('exp_weather.csv', 'a', encoding='euc_kr', newline='')
        wr = csv.writer(file)
        current_weather = WTH.get_current_weather()
        current_weather = current_weather.split(' ')[-1]
        wr.writerow(['날씨', '표정'])
        wr.writerow([current_weather])
        file.close()

        choice = input('현재 기분은 %s 입니다. %s , %s, 현재날씨, 종료 중 하나를 고르세요. : ' % (mood, '노래듣기', '기분전환 추천받기'))

        if choice == '노래듣기':
            # 노래 틀어주기 (모두 동일 음악)
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
        elif choice == '기분전환 추천받기':
            if mood in data['todo']:
                print("현재 기분 %s 에는 아래 내용을 할 것을 추천합니다." % mood)
                for do in data['todo'][mood]:
                    print(do)
        elif choice == '현재날씨':
            print("현재 날씨는 %s 입니다." % current_weather)

        flag = False
