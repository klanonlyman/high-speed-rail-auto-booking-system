# high-speed-rail-auto-booking-system
Using voice identify verification code and booking 50% off ticket.
<h3>Follow is my method</h3>
<ol>
  <li> It will use manual method to download voice files of verification code and every file will labeled its answer.<br/>
  <li> Every voice file will split to four alphabet or number and then it assign to corresponding label.</li>
  <li> Crawler the voice and images from the web of hsr verification section. Then ,it will use DTW to identify which class they belong to.</li>
  <li> Building model and train it.</li>
  <li> Using model predict the verification code and booking ticket.</li>
</ol>


<h3>This section, I will detail descript how do I implement it</h3>
<ul>
  <li>you have to download some voice file from web of HSR, and then change their file names with corresponding code.(you can reference my folder, its name is "manual")</li>
  <li>
    Because a voice file represents four alphabets or numbers , so we must divide it into corresponding word. Then, how do I do this thing?
    <ul>
      <li>
        <h3>Observe voice flies</h3>
        <p>
        You have to understand and observe every information of the voice file. such as: the length of exch voice file is differen, and there are different signals in a voice file between different letters or numbers.</p>
      <img src="https://user-images.githubusercontent.com/103729404/163662997-bc1701a7-7638-4bfb-b0d8-ce43cc48d5f4.png"/>
      <img src="https://user-images.githubusercontent.com/103729404/163663013-6e14c9a0-fb7c-4c93-a524-b26f147b1b44.png"/>
      </li>
      <li>
        <h3>Algorithem description</h3>
          <p>
          X[0:n] : amplitude or signal of a voice file
          T : denoising Threshold <br/>
          W : window size <br/>
          Avg : average value of a range , this range is IN plus W <br/>
          D : if "D" equal to "True" then it is looking for starting position, otherwise it is looking for ending position<br/>
          ST : the starting position of each alphabet or number will be stored here<br/>
          EN : the ending position of each alphabet or number will be stored here<br/> 
          initialize : T=0.045; W=500; Avg=0; D=True; ST=[]; EN=[]; <br/> <br/>
          for i in 0 to n: <br/>
              &emsp;if X[i] > T then X[i]=0;<br/>
          for i in 0 to n: <br/>
              &emsp;Avg=X[i:i+W].sum(); <br/>
              &emsp;if X[i]!=0 and D!=False then i add to ST and D=False; <br/>
              &emsp;if avg==0 and D!=True and i-ST[len(ST)-1]>2500 then i add to EN and D=True; <br/>
              &emsp;if len(ST)==4: <br/>
                  &emsp;&emsp;break; <br/>
          if D==False: <br/>
             &emsp;n-1 add to ED; <br/>
           </p>
      </li>
      <li>
        <h3>Result</h3>
        <p>we will get the amplitude of each word and store into a container of "dict". such as: dict={"a":[amplitude],"b":[amplitude].....}</p>
        <img src="https://user-images.githubusercontent.com/103729404/163675589-eedea64e-77f5-49f6-be02-d1b458532b21.png"/>
        <img src="https://user-images.githubusercontent.com/103729404/163675596-5790b60c-0c2e-4ff4-98c1-52e33e948cf2.png"/>
      </li>
    </ul>
  </li>
  <li>
    <h3>Generate more datas</h3>
    <ul>
      <li>You have to wirte a crawler code for get a voice file.</li>
      <li>The voice file will be divided into four words, but we don't known its label.(we use a container "source" to store it)</li>
      <li>Calculate the DTW value between "source" and "dict", we will get the minmum value from a certain word. This is the answer</li>
      <li>It will record its answer on the excel.</li>
    </ul>
    On top of these descriptions, you can refer to "generate voice and image data.py".
  </li>
  <li>
    <h3>The model and preprocessing will be described below</h3>
    <ul>
      <li>
          How do I process voice for the input model?<br/>
          <ul>
          <li>Each voice is normalized to a range of -1~1.</li>
          <li>These voices will be divided into four sub-voices.</li>
          <li>Extract the features of the STFT for each sub-voices.</li>
          <li>Each word will be converted to the form of one-hot-encoder.</li>
          <li>The feature of STFT and the form of one-hot-encoder will be fed into the model and train it.</li>
          </ul>
      </li>
      <li>
          Model Architecture<br/>
          <img src="https://user-images.githubusercontent.com/103729404/163765459-87ad0b59-8257-4e64-83eb-853bcf693366.png"/>
      </li>
      <li><a href="https://www.bilibili.com/video/BV1f3411C7kb/?spm_id_from=333.788.recommend_more_video.4">This website</a> is the concept of vocie process, if you don't have any Knowledge about it ,then I suggest you to read it.</li>
    </ul>
  </li>
  <li>
    <h3>Experiment result</h3>
    <ul>
      <li>loss and accuracy</li>
      <img src="https://user-images.githubusercontent.com/103729404/163767551-2b651f64-2f8f-416f-9ac3-845a4b1431d7.png"/>
      <img src="https://user-images.githubusercontent.com/103729404/163767573-cc2b70a9-39a9-4871-95a8-1dc82262dcb5.png"/>
      <li>Testing model</li>
        <ul>
          <li>I will download a image file  and a voice file</li>
          <li>The model will predict it</li>
          <li>The predicted result will be show on the image such as the following:</li>
          <img src="https://user-images.githubusercontent.com/103729404/163789410-629631e9-1cf6-49b5-9b13-1101f85c4282.png"/>
        </ul>
    </ul>
  </li>
</ul>
