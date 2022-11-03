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
            This file contains the landmarks of the face and the functions used to put the filters on the face
        3. applyF.py
            This file contains the functions used to detect the emotion and the functions used to put the filters on the face, the configuration of the webcam and the functions used to take the screenshots
        4. main.py
            this is a menu that contains the options to choose the filter and the emotion detection and is better to use this file to run the project because it has a better interface and we have a better control of the project
        
        next, there is a folder called "EmotionRecognition" that contains the files used to detect the emotion
        we have Data, Emojis, Models, CapturandoRostros, Entrenando and the main file
        1. Data
            This folder contains the images used to train the models with 4 subfolders
            1.1. happy
            1.2. angry
            1.3. sad
            1.4. sorprise
        2. Emojis
            we have just the emojis used to says the emotion
        3. Models
            This folder contains the models used to detect the emotion with the Data folder
        4. CapturandoRostros
            This folder contains the files used to capture the images to train the models, and in this file we have to change the name of the folder to the emotion we want to take the images, this file take 200 images for emotion
        5. Entrenando
            This folder contains the files used to train the models, and in this file we have to change the name of the folder to the emotion we want to train the model, this file train the model with 200 images for emotion
        6. main.py
            This file contains the functions used to detect the emotion and functions that detect if you are sad, happy, angry or sorprise and put next to us the emoji of the emotion that we are feeling

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

    then, we will see the menu of the project and see 2 options 
    emotion and filters
    Emotion
        This option is to detect the emotion and run the main file of the EmotionRecognition folder
    Filters
        This option will show us 2 options 
        apply filter
            This option is to run the main file of the project
        Face Mesh Test
            This option is to run the facemeshTest file of the project and show us the landmarks of the face

