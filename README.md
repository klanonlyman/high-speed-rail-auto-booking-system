# high-speed-rail-auto-booking-system
Using voice identify verification code and booking 50% off ticket.
<h3>First, Follow is my method</h3>
<ol>
  <li> It will use manual method to download voice files of verification code and every file will labeled its answer.<br/>
  <li> Every voice file will split to four alphabet or number and then it assign to corresponding label.</li>
  <li> Crawler the voice and images from the web of hsr verification section. Then ,it will use DTW to identify which class they belong to.</li>
  <li> Building model and train it.</li>
  <li> Using model predict the verification code and booking ticket.</li>
</ol>


<h3>This section, I will detail descript how do I implement it</h3>
<ul>
  <li>you have to download some voice file from web of HSR, and then change their file name with corresponding code.(you can reference my folder, its name is 123)</li>
  <li>
    Because a voice file represent four alphabets or numbers , so we must divide it to corresponding word. Then, how do I do this thing?
    <ul>
      <li>
        <h3>Observe voice flies</h3>
        <p>
        You have to understand and observe every information of voice file. such as: every length of voice file is different、between various alphabet or number has an distinct signal in a voice file</p>
      <img src="https://user-images.githubusercontent.com/103729404/163662997-bc1701a7-7638-4bfb-b0d8-ce43cc48d5f4.png"/>
      <img src="https://user-images.githubusercontent.com/103729404/163663013-6e14c9a0-fb7c-4c93-a524-b26f147b1b44.png"/>
      </li>
      <li>
        <h3>Algorithem description</h3>
          <p>
          X[0:n] : amplitude or signal of a voice
          T : threshold of removing noisy <br/>
          W : window size <br/>
          Avg : average value of a range , this range is IN plus W <br/>
          D : if done equal to "True" then it is looking for starting position, otherwise it is looking for ending position<br/>
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
        <p>we will get amplitude of every word and store to a container of "dict". such as dict={"a":[amplitude],"b":[amplitude].....}</p>
        <img src="https://user-images.githubusercontent.com/103729404/163675589-eedea64e-77f5-49f6-be02-d1b458532b21.png"/>
        <img src="https://user-images.githubusercontent.com/103729404/163675596-5790b60c-0c2e-4ff4-98c1-52e33e948cf2.png"/>
      </li>
    </ul>
  </li>
  <li>
    <h3>Generate more datas</h3>
    <ul>
      <li>you have to wirte a crawler code for get a voice file.</li>
      <li>the voice file will devide to four word, but we don't known its label.(we use a container "source" to store it )</li>
      <li>calculate DTW value between "source" and "dict" and  we will get min value from certain word.that is answer</li>
      <li>it will record its answer on the excel.</li>
    </ul>
    above these descript you can reference "".
  </li>
</ul>
