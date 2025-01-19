import time

from threading import Thread, Lock
import sys

lock=Lock()

def animate_text(text, delay= 0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def song_lyric(lyric,delay,speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics=[
        ("Wherever You Go,", 0.08),
        ("That's Where",0.08),
        ("I'll Foooooooollllooow",0.1),
        ("Nobody's Promised", 0.13),
        ("Tomooooooooooooorroow",0.1),
        ("So I'ma Love You Every Night",0.07),
        ("Like it's the LAST NIGHT",0.06),
        ("Like it's the LAST NIGHT",0.12),
         ("-------------------",0.001),
        ("If The World was EEEENNNNDING",0.1),
        ("I'd Wanna Be NEXXXT To",0.1),
        ("YOOOOOOUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",0.1),
        ("-------------------",0.005),
        ("If the paaarty was ooover",0.1),
        ("And Our Time on Earth was Throooouuuuuuuuuuuuuuuuuuuuuuuuugh",0.11),
        ("I'd wanna hold you",0.13),
        ("Just for a while",0.13),
        ("And DIEEEEEE WITH A SMIIILEEEEEEE",0.15),
        ("If the World was Ending",0.12),
        ("I'd wanna be next to youuuuuuuuuuuuuuuu",0.12)
       ]
    delays= [0.4,0.5,0.6,1,1.3,1.4,1.6,1.7,1.9,2.1,2.3,2.4,2.5,2.6,2.7,2.8,3.1,4.0,4.1,4.2]

    threads = []
    for i in range(len(lyrics)):
        lyric,speed = lyrics[i]
        t= Thread(target=song_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()

