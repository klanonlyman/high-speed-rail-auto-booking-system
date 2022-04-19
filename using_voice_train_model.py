#!/usr/bin/env python
# coding: utf-8

# In[35]:


from scipy import signal
import wave
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import librosa
import collections
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization,LSTM,Embedding,SimpleRNN
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D, Conv1D, MaxPool1D,MaxPooling1D
from keras import regularizers, optimizers
class VOICE:
    def __init__(self):
        self.source_path="train_data\\"
        self.threshold=0.045
        self.window=500
        self.voice_feature_x=[]
        self.voice_feature_y=[]   
        self.n_fft=256
        self.model=None
        self.class_number=24
        self.number_to_word={0: 'T', 1: '7', 2: 'Z', 3: 'M', 4: 'Y', 5: 'C', 6: 'R', 7: 'H', 8: '9', 9: '3', 
                            10: 'Q', 11: 'F', 12: '4', 13: 'N', 14: '5', 15: 'A', 16: 'P', 17: '2', 18: 'K',19:'V',20:'G',21:'6',22:'D',23:'W'}
        self.word_to_number={'T':0,'7':1,'Z':2,'M':3,'Y':4,'C':5,'R':6,'H':7,'9':8,'3':9,
                             'Q':10,'F':11,'4':12,'N':13,'5':14,'A':15,'P':16,'2':17,'K':18,'V':19,'G':20,'6':21,'D':22,'W':23}
        self.epochs=50
        self.batchsize=32
        self.history=None
    def split_voice(self,voice,alphabet):
        for j in range(0,len(voice)):
            if abs(voice[j])<self.threshold:
                voice[j]=0
        data=[]
        label=[]
        done=True
        for j in range(0,len(voice)):
            avg=np.array(voice[j:j+self.window]).sum()
            if voice[j]!=0 and done:
                start=j
                done=False

            if not(done) and avg==0 and j-start>2500:
                done=True
                data.append(voice[start:j+1])
                label.append(alphabet[len(data)-1])
            if len(data)==4:
                break
        if done==False:
            data.append(voice[start:])
            label.append(alphabet[len(data)-1])
        return data,label
    def voice_preprocess(self):
        df=pd.read_csv(self.source_path+"label.csv")
        for i in range(0,len(df)):
            try:
                name=str(df.loc[i]['name'])[:-3]
                f = wave.open(self.source_path+name+'wav','rb')
                params = f.getparams()
                nchannels, sampwidth, framerate, nframes = params[:4]
                strData = f.readframes(nframes)
                waveData = np.fromstring(strData,dtype=np.int16)
                waveData = waveData*1.0/(max(abs(waveData)))
                label=str(df.loc[i]['label'])
                waveData,label=self.split_voice(waveData,label)
                for j in range(0,len(waveData)):
                    stft = np.abs(librosa.stft(waveData[j],n_fft=self.n_fft))
                    stft=np.mean(stft,axis=1)
                    self.voice_feature_x.append(stft)
                    temp=np.zeros((self.class_number)).astype("float32")
                    temp[self.word_to_number[label[j]]]=1.0
                    self.voice_feature_y.append(temp) 
            except:
                print("no exist")
    def building_model(self):
        self.model = Sequential()
        self.model.add(Conv1D(filters=32, kernel_size=1, input_shape=(int(self.n_fft/2)+1, 1),kernel_initializer='random_normal'))
        self.model.add(Activation('relu'))
        self.model.add(MaxPool1D(2))
        self.model.add(Flatten())
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dense(self.class_number))
        self.model.add(Activation('softmax'))
        self.model.summary()
        self.model.compile(loss="categorical_crossentropy",optimizer="Adam",metrics=['acc'])
    def train_model(self):     
        self.voice_feature_x=np.array(self.voice_feature_x)
        shapes=self.voice_feature_x.shape
        self.voice_feature_x=self.voice_feature_x.reshape((shapes[0],shapes[1],1))
        self.voice_feature_y=np.array(self.voice_feature_y)            
        self.history=self.model.fit(self.voice_feature_x,self.voice_feature_y,validation_split=0.3,epochs=self.epochs,
                               batch_size=self.batchsize,verbose=0)
        self.draw_chart()
    def draw_chart(self):
        history=self.history.history
        plt.figure()
        plt.title("accuracy")
        plt.plot(history['acc'])
        plt.plot(history['val_acc'])
        plt.legend(["train","test"],loc="upper right")
        plt.show()
        plt.figure()
        plt.title("loss")
        plt.plot(history['loss'])
        plt.plot(history['val_loss'])
        plt.legend(["train","test"],loc="upper right")
        plt.show() 
    def save_model(self):
        self.model.save("voice.h5")
V=VOICE()
V.voice_preprocess()
V.building_model()
V.train_model()
V.save_model()


# In[ ]:





# In[ ]:





# In[ ]:




