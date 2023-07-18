from gtts import gTTS
import os

# อ่านข้อความจากไฟล์ word.txt
with open('word.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# เลือกภาษาให้กับ TTS
language = 'th'  # ภาษาไทย

# สร้างเสียงจากข้อความ
tts = gTTS(text=text, lang=language, slow=False)

# บันทึกไฟล์เสียงเป็น MP3
tts.save("output_docs.mp3")

# เล่นไฟล์เสียงที่สร้างขึ้น
os.system("start output_docs.mp3")
