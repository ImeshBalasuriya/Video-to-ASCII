import cv2
from time import sleep

frame_buff = []

#audio = pyglet.media.load("BadApple.mp4")

with open("ascii.txt", 'r') as file:
    frames = file.read()
    frame_buff = frames.split("\033[H")

input("Found ASCII dump. Ready to play. Press any key to start")

for i in range(1, 4):
    print(i)
    cv2.waitKey(1000)

print("\033[2J\033[H\033[?25l")

#audio.play()

for f in frame_buff:
    print(f + "\033[H")
    sleep(0.02901)


print("\033[H\033[?25h", end="")

