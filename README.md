# high-speed-rail-auto-booking-system
Using speech identify verification code and booking 50% off ticket.

Follow is my method:
   1. It will use manual method to download voice files of verification code and every file will labeled its answer.
   2. Every voice file will split to four alphabet or number and then it assign to corresponding label.
   3. Crawler more voices and images from the web of hsr verification section.
   4. These data will use DTW to identify which class they belong to.  
   5. Building model and train it.
   6. Using model predict the verification code and booking ticket.



This section, I will detail descript how do I implement:

   1. you have to download some voice from web of HSR, and then change their file name with corresponding code.(you can refernece my floder, its name is 123)
   2. Because a voice file represent four alphabets or numbers , so we must divide it to corresponding word. then how do I this thing?                       
      firsy, you have to understand and observe every inforamtion of voice file. such as: every length of voice file is different、sample_rate=8000、verious alphabet or number has a obvious single in a voice file.
      

               
