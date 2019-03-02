from gtts import gTTs
import pyglet
import time, os
def tts(text, lang):
    file= gTTs(text = text, lang = lang)
    filename = '/tmp/temp.mp'
    file.save(filename)

    music = pyglet.media.load(filename, streaming = 0)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)
