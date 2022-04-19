#!/usr/bin/env python
# coding: utf-8

# In[8]:



from selenium import webdriver

import numpy as np
import time
import requests
import cv2
import pandas as pd
from keras.models import load_model
from requests import get
import wave
import time
import librosa
import time
import matplotlib.pyplot as plt
class visual_test:
    def __init__(self):
        self.model=load_model("voice.h5")
        self.number_to_word={0: 'T', 1: '7', 2: 'Z', 3: 'M', 4: 'Y', 5: 'C', 6: 'R', 7: 'H', 8: '9', 9: '3', 
                            10: 'Q', 11: 'F', 12: '4', 13: 'N', 14: '5', 15: 'A', 16: 'P', 17: '2', 18: 'K',19:'V',20:'G',21:'6',22:'D',23:'W'}
        self.url_one='https://irs.thsrc.com.tw/IMINT/?locale=tw'
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
        self.threshold=0.045
        self.window=500
        self.n_fft=256
    def get_voice(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url_one)
        cookies=driver.get_cookies()
        sound_url=driver.find_element_by_xpath("//*[@id='action']/tbody/tr/td/a[2]").get_attribute("href")
        img_url=driver.find_element_by_xpath("//*[@id='BookingS1Form_homeCaptcha_passCode']").get_attribute("src")
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/table/tbody/tr/td/input").click()
        driver.close()
        request = requests.Session()
        request.headers.update(self.headers)
        for cookie in cookies:
            request.cookies.set(cookie['name'], cookie['value'])
        response_sound=request.get(sound_url)
        with open("current_voice.wav", 'wb') as f:
            f.write(response_sound.content)
        response_img=request.get(img_url)
        with open("current_voice.jpg", 'wb') as f:
            f.write(response_img.content)
    def split_voice(self,voice):
        for j in range(0,len(voice)):
            if abs(voice[j])<self.threshold:
                voice[j]=0
        data=[]
        done=True
        for j in range(0,len(voice)):
            avg=np.array(voice[j:j+self.window]).sum()
            if voice[j]!=0 and done:
                start=j
                done=False

            if not(done) and avg==0 and j-start>2500:
                done=True
                data.append(voice[start:j+1])
            if len(data)==4:
                break
        if done==False:
            data.append(voice[start:])
        return data
    
    def predict_code(self):
        f = wave.open('current_voice.wav','rb')
        params = f.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]
        strData = f.readframes(nframes)
        waveData = np.fromstring(strData,dtype=np.int16)
        waveData = waveData*1.0/(max(abs(waveData)))
        waveData=self.split_voice(waveData)
        inputdata=[]
        for j in range(0,len(waveData)):
            stft = np.abs(librosa.stft(waveData[j],n_fft=self.n_fft))
            stft=np.mean(stft,axis=1)
            inputdata.append(stft)
        inputdata=np.array(inputdata)
        shapes=inputdata.shape
        inputdata=inputdata.reshape((shapes[0],shapes[1],1))
        predict=self.model.predict(inputdata)
        answer=""
        for i in range(0,len(predict)):
            label=self.number_to_word[np.argmax(predict[i])]
            answer+=label
        img = plt.imread('current_voice.jpg')
        plt.imshow(img)
        plt.title(answer)
        plt.axis('off')
        plt.show()
    
V=visual_test()
for i in range(0,10):
    V.get_voice()
    V.predict_code()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[39]:





# In[ ]:




