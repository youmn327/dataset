# Facial Expression 
Recommend some activities according to facial expression. (ex. 'sad' expression: play a song which make the person feel better)

## how it works
+ detect the face on the pictures or videos in real time by using haarcascade.
+ predict a facial expression with only face area on the pic and pre-trained model.
+ recommend some activities every minutes(It depends on the setting).
+ there are three choices
  * play music
  * show some activities
  * tell current weather

## requirments
+ vlc
+ opencv-python
+ tensorflow
+ keras
+ numpy
+ glob

## reference
https://www.kaggle.com/msambare/fer2013
