# FilterPy
    This project is a Final Project to the course "Inforgrafia" 

## What is this?
    This project used mediapipe to detect the face and put a filter on it according to the user's choice
    At the same time, it contains an Emotion Detection model that detects the user's emotion and puts a filter on the face according to the emotion
    we use the webcam to detect the face and emotion
    To see the emotions we use 3 algorithms to detect the emotion
    1. EigenFace
        This algorithm is based on the PCA (Principal Component Analysis) technique and is used to recognize faces in images.
    2. FisherFace
        This algorithm is based on the LDA (Linear Discriminant Analysis) technique and is used to recognize faces in images.
    3. LBPHFace
        This algorithm is based on the Local Binary Patterns Histograms technique and is used to recognize faces in images.
    
    Certainly, we use the OpenCV library to detect the face and emotion
    We use the mediapipe library to detect the face and put a filter on it

    ## Architectury
        the project has 3 specifics folders
        1. Annotations
            This folder contains the annotations of the images used to put the filters on the face
        2. Assets
            This folder contains the images used to put the filters on the face
        3. Screenshots
            This folder contains the screenshots of the pictures that u took with the filters and in this part there are 2 mroe folders 
            3.1. multiples
                This folder contains the screenshots of the pictures that u took with the filters with a different name for each picture, the name follow this pattern:
                "YY"-"MM"-"DD"-"HH"-"MM"-"SS"-"MS".jpg
            3.2. Pruebas
                This folder is the same as the folder "multiples" but with the diffence that you can replace your image without the need for multiple pictures
        
        Then, there are 4 files in the root of the project
        1. facelBlendCommon.py
            This file contains the functions used to put the filters on the face and the functions used to detect the face
        2. facemeshTest.py
            This file contains the functions used to put the filters on the face and the functions used to detect the face

## Installation
    To install the project you need to have installed python 3.6 or higher and pip.
    To install the project you need to run the following command:
    pip install -r requirements.txt

## Install python
    We must install python on our computer, preferably the latest version of python.
    https://www.python.org/downloads/

    ![image](https://user-images.githubusercontent.com/68487005/146847869-57168d23-1423-47af-be04-c08530c43c2f.png)

## Install an IDE
    In this case we will use Visual Studio Code  
    https://code.visualstudio.com/download

    once installed we must add the python extensions in VSC
    ![image](https://user-images.githubusercontent.com/68487005/146848104-801fae20-a7ec-442a-8754-5b1866b5b7d4.png)

## Usage
    To run the project you must open the terminal and run the following command:
    python main.py

    

