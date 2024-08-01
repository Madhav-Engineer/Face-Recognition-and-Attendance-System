# Face-Recognition-and-Attendance-System
A face recognition and attendance system streamlines traditional attendance-taking by automatically identifying and recording student presence, making the process simpler, less tiring, and more convenient.


# Face Recognition Attendance System

## Introduction

In the realm of attendance systems, various methods exist, each with its own advantages and disadvantages. Among these, face recognition stands out as a particularly effective and fitting solution. Other methods, such as RFID and fingerprint recognition, present challenges:

- *RFID:* While convenient, anyone with the ID can mark attendance, making it unreliable.
- *Fingerprint Recognition:* Requires students to be in a queue, which can be time-consuming.
- *Voice Recognition:* Often lacks accuracy.
- *Iris Recognition:* Can reveal too much personal information.

*Face recognition* offers a balance between privacy, accuracy, and convenience. Digital images in this context are represented as \( f(x,y) = r(x,y) \times i(x,y) \) and can be visualized in both spatial grids and brightness quantization. The images can be black and white (8-bit pixels) or RGB (24-bit pixels).

## Project Overview

The project involves several key steps:

1. *Image Acquisition*
2. *Pre-processing*
3. *Segmentation*
4. *Description/Feature Selection*
5. *Recognition/Interpretation*
6. *Knowledge Base*

### Implementation Details

The system utilizes the following techniques:

- *HOG (Histogram of Oriented Gradients)*
- *Face Landmark Estimation*
- *DCNN (Deep Convolutional Neural Network)*
- *SVM (Support Vector Machine)*

## Steps to Follow

1. *Add Student Images:*
   - Ensure each student's image (in .jpg format) is added to the database, with the filename corresponding to the student's name. This database should be created by the user.

2. *Running the Code:*
   - Open the main code in your preferred IDE and execute it.

3. *Face Recognition Process:*
   - A window will appear that checks for known faces and displays the results.

4. *Database Update:*
   - The recognized faces are stored in an Excel database.


This project demonstrates the application of face recognition technology in streamlining the attendance process, balancing accuracy with user privacy.

There might be a chance that you might undergo an error related to the dlib and cmake during the installation of the face recognition library , this dlib should be carefully downloaded and installed according to the version of the python you use and the bit your computer is based on .

Thankyou have a nice day!
