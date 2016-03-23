import webbrowser
import time
tot_brks=3
brk_cnt=0
print("This program started on"+time.ctime())
while (brk_cnt<tot_brks):
    time.sleep(10) 
    webbrowser.open("https://www.youtube.com/watch?v=S72iG2IWEU8")
    brk_cnt=brk_cnt+1
