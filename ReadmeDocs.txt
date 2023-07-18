#ต้องติดตั้ง gTTS ก่อนใช้งาน โดยใช้คำสั่ง pip:

pip install gTTS

#import modul
from gtts import gTTS
import os

#Text transfer Speech
text = "สวัสดีครับ ยินดีต้อนรับสู่โลกของ Text-to-Speech!"

#import langauge : "th"
langauge = 'th'

#build sound by text
tts = gTTS(text=text, lang=language, slow=False)

#save files mp3
tts.save("output.mp3")

#play file for save
os.system("start output.mp3")