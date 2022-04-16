# high-speed-rail-auto-booking-system
Using voice identify verification code and booking 50% off ticket.
<h3>First, Follow is my method</h3>
<ol>
  <li> It will use manual method to download voice files of verification code and every file will labeled its answer.<br/>
  <li> Every voice file will split to four alphabet or number and then it assign to corresponding label.</li>
  <li> Crawler more voices and images from the web of hsr verification section.</li>
  <li> These data will use DTW to identify which class they belong to.</li>
  <li> Building model and train it.</li>
  <li> Using model predict the verification code and booking ticket.</li>
</ol>


<h3>This section, I will detail descript how do I implement it</h3>
<ul>
  <li>you have to download some voice from web of HSR, and then change their file name with corresponding code.(you can refernece my floder, its name is 123)</li>
  <li>
    Because a voice file represent four alphabets or numbers , so we must divide it to corresponding word. then how do I this thing?
    <ul>
      <li>
        <h3>Abserve voice flie</h3>
        <p>
        you have to understand and observe every inforamtion of voice file. such as: every length of voice file is different、verious alphabet or number has a obvious single in a voice file</p>
      <img src="https://user-images.githubusercontent.com/103729404/163662997-bc1701a7-7638-4bfb-b0d8-ce43cc48d5f4.png"/>
      <img src="https://user-images.githubusercontent.com/103729404/163663013-6e14c9a0-fb7c-4c93-a524-b26f147b1b44.png"/>
      </li>
      <li>
        <h3>algorithem description</h3>
          <p>
          X[0:n] : amplitude or signal of a voice
          T : theshlod of removing noisy <br/>
          W : window size <br/>
          Avg : averge value of a range , that range is IN plus W <br/>
          D : if done equal to "True" then it is finding  start point , otherwise it is finding end point <br/>
          ST : every start position of alphabet or number will store here. <br/>
          EN : every end position of alphabet or number will store here. <br/>
          init T=0.045; W=500; Avg=0; D=True; ST=[]; EN=[]; <br/>
          for i in 0 to n: <br/>
              &emsp;if X[i] excceed T then X[i]=0;<br/>
          for i in 0 to n: <br/>
              &emsp;Avg=X[i:i+W].sum(); <br/>
              &emsp;if X[i]!=0 and D!=False then ST add to i and D=False; <br/>
              &emsp;if avg==0 and D!=True and i-ST[len(ST)-1]>2500 then EN add to i and D=True; <br/>
              &emsp;if len(ST)==4: <br/>
                  &emsp;&emsp;break; <br/>
          if D==False: <br/>
             &emsp;ED add to n-1; <br/>
           </p>
      </li>
      <li>
        <h3>Result</h3>
        <img src="https://user-images.githubusercontent.com/103729404/163675589-eedea64e-77f5-49f6-be02-d1b458532b21.png"/>
        <img src="https://user-images.githubusercontent.com/103729404/163675596-5790b60c-0c2e-4ff4-98c1-52e33e948cf2.png"/>
      </li>
    </ul>
  </li>
</ul>
