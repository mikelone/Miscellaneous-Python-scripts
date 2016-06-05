#Miscellaneous Python scripts 

##Author

Mikelone

Miscellaneous Python scripts i have used on projects over the years..

##File list

###BackgroundSubtractorMOG2.py  

openCV video capture to subtract the previous frames using BackgroundSubtractorMOG2 function

this creates a nice black and white effect .. 


###cnc2laser.py 

this converts inkscapes cnc gcode to laser cutter 

first it will delete all M3 and M5 from the files.

second it will place the M3 after penetration and places M5 before movement


###Color Tracking.py 

First it detects the color from the captured frame and creates a black and white effect which the white was the detected color and stores it under mask.

Second it merges the original frame to the mask and creates a moving character of the detected color.
 
###comPort.py 
 
this is the a simple communication script between python host to a serial device
 
used this to read information from a GPS device which uses baudrate 9600 .. 

###yahooUS_finance.py

shows 4 stock from yahoo finance on 4 graphs formant. shows the difference between the Dow and gold and the US dollar power shares.

##How to run the file

All the scripts were tested under python 2.7 

##Bugs

none for right now..
