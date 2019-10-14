import time
import webbrowser

counter = 0

while counter < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=KVGRN7Z7T1A")
    counter += 1
