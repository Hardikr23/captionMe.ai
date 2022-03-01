#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt


# In[2]:


def trainModel():
    model = keras.Sequential()

    # Convolutional layer and maxpool layer 1
    model.add(keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)))
    model.add(keras.layers.MaxPool2D(2,2))

    # Convolutional layer and maxpool layer 2
    model.add(keras.layers.Conv2D(64,(3,3),activation='relu'))
    model.add(keras.layers.MaxPool2D(2,2))

    # Convolutional layer and maxpool layer 3
    model.add(keras.layers.Conv2D(128,(3,3),activation='relu'))
    model.add(keras.layers.MaxPool2D(2,2))

    # Convolutional layer and maxpool layer 4
    model.add(keras.layers.Conv2D(128,(3,3),activation='relu'))
    model.add(keras.layers.MaxPool2D(2,2))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(512,activation='relu'))
    model.add(keras.layers.Dense(1,activation='sigmoid'))

    model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
    return model


# In[3]:


def predictImage(model, file_name, classification):
    xVal = ''
    image1 = image.load_img(file_name,target_size=(150,150))
    plt.imshow(image1)
    Y = image.img_to_array(image1)
    X = np.expand_dims(Y,axis=0)
    value = model.predict(X)
    print(value)
    if value == 1: 
        xVal = classification[1]
    elif value == 0:
        xVal = classification[0]
    return xVal


# In[4]:


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
train_set = train_datagen.flow_from_directory(
        os.getcwd() + '/../images/Train',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        os.getcwd() + '/../images/Test',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')


oceanTreesClass = ['Ocean', 'Trees']
test_set.class_indices


# In[5]:


oceanTrees = trainModel()
oceanTrees.fit(
        train_set,        
        epochs=10,
        validation_data=test_set,
        )


# In[6]:


# In[7]:


# print(predictImage(oceanTrees, '/Users/anahitabilimoria/Desktop/image.jpeg', oceanTreesClass))


# In[8]:


train_datagen1 = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen1 = ImageDataGenerator(rescale=1./255)
train_set1 = train_datagen1.flow_from_directory(
        os.getcwd() + '/../images/Train2',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')
test_set1 = test_datagen1.flow_from_directory(
        os.getcwd() + '/../images/Test2',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')

test_set1.class_indices
nightSunClass = ['Night', 'Sunkaset']


# In[9]:


nightSun = trainModel()    
nightSun.fit(
    train_set1,        
    epochs=10,
    validation_data=test_set1,
    )


# In[10]:


# print(predictImage(nightSun, '/Users/anahitabilimoria/Desktop/image.jpeg' , nightSunClass))


# In[11]:


from imageai.Detection import ObjectDetection
import os

def trainImageAI(filepath):
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
    detector.loadModel()

    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , filepath), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"])
        print()
    
    return detections


# In[12]:


def main_predict(filename):
    detections = trainImageAI(filename)
    predictedArr = [detection['name'].lower() for detection in detections]
    
    requiredName = {
        'beach_captions' : ['Ocean'],
        'sun_captions' : ['Sunkaset'],
        'trees_captions' : ['Trees'],
        'car_captions' : ['bicycle', 'car', 'motorcycle','airplane','bus','train','truck', 'boat'],
        'people_captions' : ['person'],
        'dog_captions' : ['dog'],
        'food_captions' : ['bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donot', 'cake']
    }
    
    nightSunPred = predictImage(nightSun, filename , nightSunClass)
    predictedArr.append(nightSunPred)
    
    oceanTreePred = predictImage(oceanTrees, filename , oceanTreesClass)
    predictedArr.append(oceanTreePred)
    
    predictionArr = list(set(predictedArr))
    finalArr = []
    for _ in predictionArr:
        for key, value in requiredName.items():
            if _ in requiredName[key]:
                finalArr.append(key)
    print(finalArr)
    print()
    return finalArr    

# In[ ]:




