import cv2
from deepface import DeepFace
import numpy as np
import random

face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'  #getting a haarcascade xml file
face_cascade = cv2.CascadeClassifier()  #processing it for our project
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):  #adding a fallback event
    print("Error loading xml file")

video=cv2.VideoCapture(0)  #requesting the input from the webcam or camera

emotion_update_interval = 10  # Update the emotion display every 30 frames
frame_counter = 0
dominant_emotion = ""

# Define the counter and the number of times to choose the same image
counter = 0
choose_same_image_times = 4

while video.isOpened():  #checking if are getting video feed and using it
    _,frame = video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #changing the video to grayscale to make the face analysis work properly
    face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    
    for x,y,w,h in face:
      #making a try and except condition in case of any errors
      try:
          if frame_counter % emotion_update_interval == 0:
              analyze = DeepFace.analyze(frame,actions=['emotion'])  #we are using the analyze class from deepface and using ‘frame’ as input
              dominant_emotion = analyze[0]['dominant_emotion']  #here we will only get the dominant emotion
          #cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
          # Load the image to be overlayed on the frame
          if dominant_emotion == 'happy':
              if counter < choose_same_image_times:
                  counter += 1
              else:
                  image_path = random.choice(['emojis/happy1.png', 'emojis/happy2.png'])  # Choose the second image path
                  counter = 0
    
          elif dominant_emotion == 'sad':
              if counter < choose_same_image_times:
                  counter += 1
              else:
                  image_path = random.choice(['emojis/sad1.png', 'emojis/sad2.png'])  # Choose the second image path
                  counter = 0
              
          elif dominant_emotion == 'fear':
              if counter < choose_same_image_times:
                  counter += 1
              else:
                  image_path = random.choice(['emojis/fear1.png', 'emojis/fear2.png'])  # Choose the second image path
                  counter = 0
             
          elif dominant_emotion == 'disgust':
              if counter < choose_same_image_times:
                  counter += 1
              else:
                  image_path = random.choice(['emojis/disgust1.png', 'emojis/disgust2.png'])  # Choose the second image path
                  counter = 0
            
          elif dominant_emotion == 'angry':
              if counter < choose_same_image_times:
                  counter += 1
              else:
                  image_path = random.choice(['emojis/angry1.png', 'emojis/angry2.png'])  # Choose the second image path
                  counter = 0
             
          elif dominant_emotion == 'surprise':
              image_path = 'emojis/surprise1.png'
          else:
              image_path = 'emojis/neutral1.png'
          overlay = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
          resized_overlay = cv2.resize(overlay, (100, 100))
          # Overlay the PNG image onto the frame at the specified (x, y) position
          y_offset = y - 100
          x_offset = x - 50
          for c in range(0, 3):
              frame[y_offset:y_offset+resized_overlay.shape[0], x_offset:x_offset+resized_overlay.shape[1], c] = resized_overlay[:, :, c] * (resized_overlay[:, :, 3] / 255.0) + frame[y_offset:y_offset+resized_overlay.shape[0], x_offset:x_offset+resized_overlay.shape[1], c] * (1.0 - resized_overlay[:, :, 3] / 255.0)

      except:
          print("no face")
      
      #this is the part where we display the output to the user
      cv2.imshow('video', frame)
      key=cv2.waitKey(1) 
      if key==ord('q'):   # here we are specifying the key which will stop the loop and stop all the processes going
        break
      frame_counter += 1
video.release()
