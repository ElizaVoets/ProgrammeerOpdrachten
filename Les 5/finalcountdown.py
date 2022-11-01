from time import sleep
import webbrowser

for i in range(1000, 0, -1):
    print(i)
    sleep(0.01)
    if i == 1:
        webbrowser.open_new("https://www.youtube.com/watch?v=fC7oUOUEEi4")