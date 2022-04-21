# high-speed-rail-auto-booking-system
Booking 50% off tickets using voice identify verification code.
<h3>Before running this project, you must note the following</h3>
<ul>
  <li>You must check or rebuild Anaconda's environment.</li>
  
      #GPU-GTX1080
      #open your CMD, and follow the steps below
      conda create --name test_env python=3.6
      activate test_env
      pip install numpy
      pip install pandas
      pip install matplotlib
      pip install requests
      pip install BeautifulSoup4
      pip install tslearn
      pip install scipy
      pip install librosa
      pip install selenium
      if your computer have to suport the GPU:
        pip install tensorflow-gpu==1.14.0
      else:
        pip install tensorflow==1.14.0
      pip install keras==2.2.2
      pip install h5py==2.10.0
      pip install opencv-python
  <li>Download "chromedriver.exe", you can refer this <a href="https://medium.com/@bob800530/selenium-1-%E9%96%8B%E5%95%9Fchrome%E7%80%8F%E8%A6%BD%E5%99%A8-21448980dff9">website</a></li>
</ul>

<h3>Program execution flow</h3>
<ul>
  <li>First, after excute "generate_voice_and_image_data.py", you will extend more labeled data in the "train_data" folder.</li>
  <li>Second,after excute "using_voice_train_model.py" , it will take the training data from that folder , then it will train a model and store it to "voice.h5" file.</li>
  <li>Third,after excute "using_voice_visual_test.py" , using visual's method verifies that model("voice.h5"), it will show a image and an answer.</li>
</ul>
<h3>I don't put the booking system program because of some legal issues. If you want this code , then you can send an e-mail to "NE6091027@gs.ncku.edu.tw"</h3>
