import cv2
import time


class face_detect:
    def __init__(self, path):
        self.base_time = int(time.strftime('%c', time.localtime(time.time()))[-7:-5])
        self.current_time = None
        self.cascade = cv2.CascadeClassifier(path)

    def extract_face(self, img, x, y, w, h):
        img = img[y:y + h, x:x + w, :] # x,y,w,h를 이용해서 얼굴만 나온곳만 오려낸다.
        img = cv2.resize(img, (48,48))
        return img

    # cascade 파일을 읽고 얼굴인식해 좌표값이 있는 리스트를 반환
    def load_cascade_file_n_coordinate(self,gray_img):
        face_list = self.cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))
        return face_list

    def detect_face(self,image_file):
        flag = False
        self.current_time = int(time.strftime('%c', time.localtime(time.time()))[-7:-5])
        people = []
        gray_img = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY) # 이미지를 회색으로 저장
        face_list = self.load_cascade_file_n_coordinate(gray_img) # face_list 에 얼굴 인식된것마다 좌표값 리스트
        if abs(self.base_time - self.current_time) % 10 == 0 and abs(self.base_time - self.current_time) != 0:
            flag = True
        if len(face_list) > 0:
            for face in face_list: # 인식된 얼굴 하나하나 당 죄표값을 알기위해 for문을 돌려준다.
                x, y, w, h = face # 좌표값
                face_img = self.extract_face(image_file,x,y,w,h) # 좌표값이랑 이미지 파일을 넣고 이미지에서 얼굴만 오려내 face_img에 저장한다.
                cv2.rectangle(image_file, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.imshow('img',image_file)
                cv2.waitKey(1)
                people.append(face_img)

        else:
            print("얼굴이 확인되지 않습니다.") # face_list에 반환된 좌표값이 없으면 출력

        return people, flag


if __name__ == '__main__':
    face = face_detect("./file/haarcascade_frontalface_alt.xml") # haarcascade_frontalface_alt 파일 경로
    # face.detect_face()
