import cv2
import numpy as np
import sys

character_set = " .:-=+*#%@"
width = 200
frame_buff = []

def handle_args(args):
    print(args)


handle_args(sys.argv)

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('test.mkv')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video file")

total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
i = 0

    
# Read until video is completed
while(cap.isOpened()):
      
  # Capture frame-by-frame
  ret, frame = cap.read()

  #For each frame
  if ret == True:
      #Convert to grayscale
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      #Resize frame to fit terminal
      h, w = frame.shape

      ratio = width / w
      dim = (width, int(h * ratio))

      frame = cv2.resize(frame, dim)

      #Initialize ASCII frame
      asc_frame = ""

      #Load ASCII into image
      for x in range(0, len(frame), 2):
          for y in frame[x]:
              asc_frame += character_set[int(9 * y / 255)]
          asc_frame += "\n"

      frame_buff.append(asc_frame + "\033[H")
      #print("Extracting Frames: " + str(i) + "/" + str(total) + "\033[H")
      i += 1
   
  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Write to file
with open("ascii.txt", mode='w') as file:
    for frame in frame_buff:
        file.write(frame)

input("Done! Press ENTER to start playback")


print("\033[2J\033[H\033[?25l")

#Show the magic!
for f in frame_buff:
    print(f + "\033[H")
    cv2.waitKey(33)


print("\033[H\033[?25h", end="")