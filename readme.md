This project is about using OpenCv library for human face detection and then recognizing the face by checking it in database whether if this face is present in database or not. If present, then give the name of person.

#requirements
Python 2.x
OpenCv 2.x
Numpy library
Sqlite database

#Initial Guideline 
-- install Python in its default location (i.e c:/python27).
--  then OpenCv download and extract. And then copy “cv2.pyd” file to “c:/python27/Lib/site-packages/” folder from “opencv/Build/python/2.7/x86” folder.
-- Use cmd as "run as administrator" and install numpy by "pip install numpy" to the folder "c:/python27/scripts/". This folder can be accessed by command “cd c:/python27/scripts/”.
-- Download Sqlite databse for creating database of many human faces.

#About project
-- "introToFaceDetection.py" program detects any human face appearing in laptop camera.
-- "dataSetCreater.py" program creates the dataset for training purpose.
-- "trainer.py" program trains the model for human face identity recognition using the dataset created earlier.
-- "detector.py" program now detects any new face exposed to camera and give the identity of the face if it is already present in the database.
