from face_detection import face_detect

face = face_detect("./file/haarcascade_frontalface_alt.xml")  # haarcascade_frontalface_alt 파일 경로
face.detect_face()

