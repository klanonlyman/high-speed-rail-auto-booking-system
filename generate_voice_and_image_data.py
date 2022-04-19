#!/usr/bin/env python
# coding: utf-8

# In[2]:


import wave
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import signal
from requests import get
from bs4 import BeautifulSoup
from tslearn.metrics import dtw
import time
import csv
class pre_work:
    def __init__(self):
        self.data=[]
        self.label=[]
        self.threshold=0.045
        self.window=500
        self.file_path="manual"
        self.save_path="train_data\\"
        self.index=0
        self.wave_alphabet_number={}
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        if not(os.path.isfile(self.save_path+"label.csv")):
            with open(self.save_path+"label.csv",'a+',newline='') as writecsv:
                writer = csv.writer(writecsv)
                writer.writerow(["name","label"])
            
    def read_voice_file(self):
        file=os.listdir(self.file_path)
        for name in file:
            f = wave.open(self.file_path+'\\'+name,'rb')
            params = f.getparams()
            nchannels, sampwidth, framerate, nframes = params[:4]
            strData = f.readframes(nframes)
            waveData = np.fromstring(strData,dtype=np.int16)
            waveData = waveData*1.0/(max(abs(waveData)))
            self.data.append(waveData)
            self.label.append(name[:-4])
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
    def get_alphabet_number_wave(self):
        for i in range(0,len(self.data)):
            data,label=self.split_voice(self.data[i],self.label[i])
            for j in range(0,len(data)):
                if label[j] not in self.wave_alphabet_number:
                    self.wave_alphabet_number[label[j]]=data[j]
        print(self.wave_alphabet_number.keys())
    def produce_new_voice_data(self):
        form_url,sound_url,img_url,cookies=self.read_url()
        self.save_file(img_url,sound_url,cookies)
        with wave.open(self.save_path+str(self.index)+'.wav','rb') as f:
            params=f.getparams()
            nchannels,sampwidth,framerate, nframes = params[:4]
            strData=f.readframes(nframes)
        waveData=np.fromstring(strData,dtype=np.int16)
        waveData=waveData*1.0/(max(abs(waveData)))
        data,label=self.split_voice(waveData,['*','*','*','*'])
        answer=""
        for i in range(0,len(data)):
            min_v=float('inf')
            index=""
            for j in self.wave_alphabet_number:
                if len(self.wave_alphabet_number[j])!=0:
                    d=dtw(data[i],self.wave_alphabet_number[j])
                    if min_v>d:
                        index=j
                        min_v=d
            answer+=str(index)
        try:
            with open(self.save_path+"label.csv",'a+',newline='') as writecsv:
                writer = csv.writer(writecsv)
                writer.writerow([str(self.index)+'.jpg',answer])
        except:
            print("is exist")
    def read_url(self):
        url='https://irs.thsrc.com.tw/IMINT/?locale=tw'
        data={"locale":"tw"}
        response=get(url,params=data,headers=self.headers)
        html=BeautifulSoup(response.text,"html.parser")
        form_url="https://irs.thsrc.com.tw"+html.find("form")["action"]
        table=html.find("table",{"id":"action"})
        sound_url="https://irs.thsrc.com.tw"+table.find_all("a")[1]["href"]
        img_url=html.find("img",{"id":"BookingS1Form_homeCaptcha_passCode"})
        img_url="https://irs.thsrc.com.tw"+img_url["src"]
        print(img_url)
        cookies=response.cookies
        return form_url,sound_url,img_url,cookies
    def save_file(self,img_url,sound_url,cookies):
        self.index+=1
        response_img=get(img_url,headers=self.headers,cookies=cookies)
        with open(self.save_path+str(self.index)+".jpg", 'wb') as f:
            f.write(response_img.content)
        response_sound=get(sound_url,headers=self.headers,cookies=cookies)
        with open(self.save_path+str(self.index)+".wav", 'wb') as f:
            f.write(response_sound.content)
            
method=pre_work()
method.read_voice_file()
method.get_alphabet_number_wave()
for i in range(0,1000): #產生幾筆有LABEL的數據
    method.produce_new_voice_data()


# In[ ]:





# In[ ]:





# In[ ]:




