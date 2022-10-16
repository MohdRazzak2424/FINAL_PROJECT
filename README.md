# **volume control using hand gesture recognition python**
For the [Final Project of CS50x 2022](https://cs50.harvard.edu/x/2022/) of the Harvard-provided CS50 course, I developed this simple Python volume control using hand gesture recognition  .

##**Video Demo:** www.youtube.com


## CREATED by:

**MOHD RAZZAK**

### Description:

Interaction with the computer is one of the important challenges that the elderly and disabled people face in today's computer world. In recent years, hand gesture recognition has emerged as one of the most natural human-machine interactions in software development, especially to facilitate friendly and flexible human-computer interaction. This paper proposes a system architecture and software configuration to develop a real-time voice-controlled hand gesture on a Raspberry Pi equipped with a camera programmed in Python using the Open-Source Computer Vision (OpenCV) library. The main purpose of the hand gesture recognition system is to communicate between humans and computer systems in order to control voice. According to the experimental results, the hand movement detection system performs well when controlling the voice. This system is able to work in real-time for any individual.

## *Actually How is it work*:


This program can control the sound with the help of libraries available in Python by scanning 2 thumb and index finger.
If the distance between these 2 fingers decreases, the sound decreases, but if the distance between the fingers increases, the sound increases.
The sensor system scans each friend's hand together, but it considers the hand as controllable to enter the system later

__Here we are trying to process a video so that we can control the volume of the device with help of the camera using the tips of our thumb and index finger.__


## *Python Library Requirement*:-

**NumPy** is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.It also has functions for working in domain of linear algebra, fourier transform, and matrices

**Open-CV** OpenCV is a huge open-source library for computer vision, machine learning, and image processing

**Mediapipe:** Mediapipe is an open-source machine learning library of Google, which has some solutions for face recognition and gesture recognition and provides encapsulation of python. MediaPipe Hand is a high-fidelity hand and finger tracking solution. It uses machine learning (ML) to infer 21 key 3D hand information from just one frame. We can use it to extract the coordinates of the key points of the hand.

**Pycaw**: Python Audio Control Library it  is a Python library typically used in Programming Style, Reactive Programming applications. pycaw has no bugs, it has no vulnerabilities

**ctypes** ctypes is a Python package to create and manipulate C data types in Python, and to call functions in dynamic link libraries/shared dlls. It allows wrapping these libraries in pure Python.

**comtypes**  comtypes allows to define, call, and implement custom and dispatch-based COM interfaces in pure Python

### **Merits**:

- Easy to use
- Hassle-free
- Fun to use
- More interactive

### ~~Demerites~~:

- Cant be used for long-distance
- Sometimes not accurate
- Requires a high-quality camera
- May be confused when two palms are showing simulatanously

#### Installation Process -

- install `python v3.x`
- Run the command on window CMD `pip install mediapipe`

- Run the command `pip install opencv-python`

- Run the command `pip install comtypes`

- Run the command `pip install pycaw`

- Run the command  `pip install ctype`

-  After  all the dependancies and Requirement have been installed, run the command `python Main.py`







