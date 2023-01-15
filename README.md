# Smart Attendance System
This code uses the OpenCV and face_recognition libraries to track attendance using facial recognition. It captures video feed from the computer's webcam and compares the faces in the current frame to a pre-existing dataset of known faces. If a match is found, the name of the person is displayed on the screen and their attendance is marked in a CSV file.

## Requirements
- OpenCV
- face_recognition
- numpy
- datetime

## Usage
- Save images of the individuals whose attendance you want to track in the 'StudentImages' folder. The image files should be named as the individual's name without spaces.
- Run the code, which will open the computer's webcam and start the facial recognition process.
- When a match is found, the person's name is displayed on the screen and their attendance is marked in a 'Attendance.csv' file with the current timestamp.

## Customization
You can add more images to the 'StudentImages' folder to expand the dataset of known faces. You can also modify the code to save the attendance data to a database or integrate it with an existing attendance system.

This code version has added a threshold to the facial recognition process. A threshold of 0.45 is set, you can adjust this value as you see fit. Lower value will make the match more strict and higher value will make the match more relaxed.

Note: The code uses os.startfile("C:\Program Files (x86)\Iriun Webcam\IriunWebcam.exe") to start a webcam software, you might have to change the path and the software name according to the software you are using.
