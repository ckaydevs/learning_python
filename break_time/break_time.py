import webbrowser
import time

no_of_breaks=3
breaks=0
print("This Program started on " + time.ctime())
while (breaks<no_of_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=450p7goxZqg")
    breaks+=1
