# Circle-Detection-Using-OpenCv
Welcome to this simple program of Circle Detection. 
This program will outline circle shown which is the most appropriate.

_Steps Followed_
1) Video Capture : Opens a video capture object for the default camera
2) Circle Detection Loop :
   a) Reads a frame from the video capture
   b) Converts the frame to grayscale
   c) Applies guassian blur to grayscale frame
   d) Uses the HoughsCicrcles Function to detect circles in the blurred frame
